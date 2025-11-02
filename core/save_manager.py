from init import *

class SaveManager:
    """A class for managing (optionally encrypted) save-slots as JSON storage."""

    def __init__(self, logger=None) -> None:
        """
        Initialize the save system. Creates directories & slotfile if missing.

        Args:
        - logger (Logger): Optional logger for warnings & errors.
        - directory (str): Path where save data is stored.
        """
        self.logger = logger
        self.directory = "data/saves/"
        self.slotfile = "slots.dat"
        self.slots: dict[str, bytes] = {}
        self._slotkey = b"OCqZTMHYWLh1DoCrXUDoI1hU6G9PwS03apyMKMCGBx4="
        self._setup()

    def set_directory(self, path: str) -> None:
        """
        Change save directory and reinitialize the system.

        Args:
        - path (str): New directory path.
        """
        self.directory = path if path.endswith("/") else path + "/"
        self._setup()
    
    def generate_encryption_key(self) -> bytes:
        """
        Generate a new encryption key for encrypted slots.

        Returns:
        - bytes: Generated encryption key.
        """
        return Fernet.generate_key()

    def set_encryption_key(self, slot: str, encryption_key: bytes) -> bool:
        """
        Set/replace the encryption key for a slot and re-encrypt existing data.

        Args:
        - slot (str): Slot name.
        - encryption_key (bytes): New key (b"" disables encryption).

        Returns:
        - bool: True on success, False on failure.
        """
        try:
            # Sichere den alten Schlüssel
            old_key = self.slots.get(slot, b"")
            old_path = self._get_slot_path(slot)
            
            # Stelle sicher dass der Slot existiert
            if slot not in self.slots:
                if self.logger: self.logger.warning(f"Slot '{slot}' missing, auto-created")
                self._create_slot(slot)
                data = {}
            else:
                # Lade mit altem Schlüssel
                if os.path.exists(old_path):
                    with open(old_path, "rb") as f:
                        raw_data = f.read()
                    try:
                        if old_key == b"":
                            # War unverschlüsselt (JSON)
                            data = json.loads(raw_data.decode('utf-8'))
                        else:
                            # War verschlüsselt
                            data = json.loads(Fernet(old_key).decrypt(raw_data).decode())
                    except Exception as e:
                        if self.logger: self.logger.error(f"Could not decrypt old data: {e}")
                        return False
                else:
                    data = {}

            # Setze neuen Schlüssel und speichere Slot-Informationen
            self.slots[slot] = encryption_key
            self._save_slotfile()

            # Lösche alte Datei
            if os.path.exists(old_path):
                try:
                    os.remove(old_path)
                except Exception as e:
                    if self.logger: self.logger.warning(f"Could not remove old save file: {e}")

            # Schreibe mit neuem Schlüssel
            self._write_raw(slot, data)

            if self.logger: 
                if encryption_key == b"":
                    self.logger.info(f"Encryption disabled for slot '{slot}', saved as JSON")
                else:
                    self.logger.info(f"New encryption key set for slot '{slot}'")
            return True
            
        except Exception as e:
            if self.logger: self.logger.error(f"set_encryption_key failed: {e}")
            return False

    def save(self, key: str, value, slot: str = "save") -> bool:
        """
        Save a value to a slot under the given key.

        Args:
        - key (str): Json key name.
        - value (any): Any JSON-serializable object.
        - slot (str): Slot name.

        Returns:
        - bool: True on success.
        """
        if slot not in self.slots:
            if self.logger: self.logger.info(f"Slot '{slot}' missing, auto-created")
            self._create_slot(slot)

        data = self._load_raw(slot)
        data[key] = value
        self._write_raw(slot, data)
        return True

    def load(self, key: str, slot: str = "save", default=None):
        """
        Load a value from a slot.

        Args:
        - key (str): Json key name.
        - default: Value returned if key not found.
        - slot (str): Slot name.

        Returns:
        - any: Stored value or default.
        """
        if slot not in self.slots:
            if self.logger: self.logger.warning(f"Slot '{slot}' missing.")
            return default

        data = self._load_raw(slot)
        return data.get(key, default)

    def delete_slot(self, slot: str) -> bool:
        """
        Delete a slot including its file.

        Args:
        - slot (str): Slot name.

        Returns:
        - bool: True if deleted, False if not found.
        """
        if slot in self.slots:
            del self.slots[slot]
            path = self.directory + slot + ".dat"
            if os.path.exists(path):
                os.remove(path)
            self._save_slotfile()
            if self.logger: self.logger.info(f"Slot deleted: {slot}")
            return True

        if self.logger: self.logger.warning(f"Delete failed, slot not found: {slot}")
        return False
    
    def get_slots(self) -> list[str]:
        """
        Get a list of all existing slot names.

        Returns:
        - list[str]: List of slot names.
        """
        return list(self.slots.keys())
    
    def _setup(self) -> None:
        try:
            os.makedirs(self.directory, exist_ok=True)
            if not os.path.exists(self.directory + self.slotfile):
                self._create_slot("save", b"")
                self._save_slotfile()
                if self.logger: self.logger.info("Slotfile created with default slot")
            else:
                self._load_slotfile()
        except Exception as e:
            if self.logger: self.logger.error(f"Setup failed: {e}")

    def _create_slot(self, name: str, key: bytes = b"") -> None:
        self.slots[name] = key
        self._save_slotfile()

    def _encrypt(self, data: dict, key: bytes) -> bytes:
        try:
            if key == b"":
                return json.dumps(data, indent=4, ensure_ascii=False).encode("utf-8")
            
            encoded = json.dumps(data).encode()
            return Fernet(key).encrypt(encoded)
        except Exception as e:
            if self.logger: self.logger.error(f"Encrypt failed: {e}")
            return b""

    def _decrypt(self, data: bytes, key: bytes) -> dict:
        try:
            if data == b"": return {}
            if key == b"": 
                return json.loads(data.decode("utf-8"))
            
            return json.loads(Fernet(key).decrypt(data).decode())
        except Exception as e:
            if self.logger: self.logger.error("Decrypt failed (wrong key/corrupt data)")
            return {}

    def _get_slot_path(self, slot: str) -> str:
        is_encrypted = self.slots.get(slot, b"") != b""
        extension = ".dat" if is_encrypted else ".json"
        return self.directory + slot + extension

    def _load_raw(self, slot: str) -> dict:
        path = self._get_slot_path(slot)
        if not os.path.exists(path):
            alt_ext = ".dat" if path.endswith(".json") else ".json"
            alt_path = self.directory + slot + alt_ext
            if os.path.exists(alt_path):
                path = alt_path
            else:
                return {}
        
        try:
            with open(path, "rb") as file:
                raw = file.read()
            return self._decrypt(raw, self.slots.get(slot, b""))
        except Exception as e:
            if self.logger: self.logger.error(f"Load failed: {e}")
            return {}

    def _write_raw(self, slot: str, data: dict) -> None:
        path = self._get_slot_path(slot)
        alt_ext = ".dat" if path.endswith(".json") else ".json"
        alt_path = self.directory + slot + alt_ext
        if os.path.exists(alt_path):
            try:
                os.remove(alt_path)
            except Exception:
                if self.logger: self.logger.warning(f"Could not remove old save file: {alt_path}")
        
        try:
            raw = self._encrypt(data, self.slots.get(slot, b""))
            with open(path, "wb") as f:
                f.write(raw)
        except Exception as e:
            if self.logger: self.logger.error(f"Write failed: {e}")

    def _save_slotfile(self) -> None:
        try:
            payload = {n: k.decode() for n, k in self.slots.items()}
            fullpath = self.directory + self.slotfile
            raw = self._encrypt(payload, self._slotkey)
            with open(fullpath, "wb") as f:
                f.write(raw)
        except Exception as e:
            if self.logger: self.logger.error(f"Save slotfile failed: {e}")

    def _load_slotfile(self) -> None:
        try:
            fullpath = self.directory + self.slotfile
            if not os.path.exists(fullpath):
                self.slots = {}
                return
            with open(fullpath, "rb") as f:
                raw = f.read()
            j = self._decrypt(raw, self._slotkey) if raw else {}
            self.slots = {n: (k.encode() if k else b"") for n, k in j.items()}
        except Exception as e:
            if self.logger: self.logger.error(f"Load slotfile failed: {e}")
