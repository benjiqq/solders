from typing import List, Optional, Sequence, Tuple, Union

from solders.hash import Hash
from solders.instruction import CompiledInstruction, Instruction
from solders.keypair import Keypair
from solders.message import Message, MessageV0
from solders.null_signer import NullSigner
from solders.presigner import Presigner
from solders.pubkey import Pubkey
from solders.signature import Signature

Signer = Union[Keypair, Presigner, NullSigner]

class Transaction:
    def __init__(
        self,
        from_keypairs: Sequence[Signer],
        message: Message,
        recent_blockhash: Hash,
    ) -> None: ...
    @property
    def signatures(self) -> List[Signature]: ...
    @signatures.setter
    def signatures(self, signatures: Sequence[Signature]) -> None: ...
    @property
    def message(self) -> Message: ...
    @staticmethod
    def new_unsigned(message: Message) -> "Transaction": ...
    @staticmethod
    def new_with_payer(
        instructions: Sequence[Instruction],
        payer: Optional[Pubkey] = None,
    ) -> "Transaction": ...
    @staticmethod
    def new_signed_with_payer(
        instructions: Sequence[Instruction],
        payer: Optional[Pubkey],
        signing_keypairs: Sequence[Signer],
        recent_blockhash: Hash,
    ) -> "Transaction": ...
    @staticmethod
    def new_with_compiled_instructions(
        from_keypairs: Sequence[Signer],
        keys: Sequence[Pubkey],
        recent_blockhash: Hash,
        program_ids: Sequence[Pubkey],
        instructions: Sequence[CompiledInstruction],
    ) -> "Transaction": ...
    @staticmethod
    def populate(
        message: Message, signatures: Sequence[Signature]
    ) -> "Transaction": ...
    def data(self, instruction_index: int) -> bytes: ...
    def key(self, instruction_index: int, accounts_index: int) -> Optional[Pubkey]: ...
    def signer_key(
        self, instruction_index: int, accounts_index: int
    ) -> Optional[Pubkey]: ...
    def message_data(self) -> bytes: ...
    def sign(self, keypairs: Sequence[Signer], recent_blockhash: Hash) -> None: ...
    def partial_sign(
        self,
        keypairs: Sequence[Signer],
        recent_blockhash: Hash,
    ) -> None: ...
    def verify(self) -> None: ...
    def verify_and_hash_message(self) -> Hash: ...
    def verify_with_results(self) -> List[bool]: ...
    def get_signing_keypair_positions(
        self,
        pubkeys: Sequence[Pubkey],
    ) -> List[Optional[int]]: ...
    def replace_signatures(
        self, signers: Sequence[Tuple[Pubkey, Signature]]
    ) -> None: ...
    def is_signed(self) -> bool: ...
    def uses_durable_nonce(self) -> Optional[CompiledInstruction]: ...
    def sanitize(self) -> None: ...
    def __bytes__(self) -> bytes: ...
    @staticmethod
    def default() -> "Transaction": ...
    @staticmethod
    def from_bytes(data: bytes) -> "Transaction": ...
    def __richcmp__(self, other: "Transaction", op: int) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def get_nonce_pubkey_from_instruction(
        self, ix: CompiledInstruction
    ) -> Optional[Pubkey]: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "Transaction": ...

class Legacy:
    Legacy: "Legacy"
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...

class VersionedTransaction:
    def __init__(
        self,
        message: Union[Message, MessageV0],
        keypairs: Sequence[Signer],
    ) -> None: ...
    @property
    def signatures(self) -> List[Signature]: ...
    @signatures.setter
    def signatures(self, signatures: Sequence[Signature]) -> None: ...
    @property
    def message(self) -> Message: ...
    @staticmethod
    def populate(
        message: Union[Message, MessageV0], signatures: Sequence[Signature]
    ) -> "VersionedTransaction": ...
    def verify_and_hash_message(self) -> Hash: ...
    def verify_with_results(self) -> List[bool]: ...
    def sanitize(self) -> None: ...
    def version(self) -> TransactionVersion: ...
    def into_legacy_transaction(self) -> Optional[Transaction]: ...
    def __bytes__(self) -> bytes: ...
    @staticmethod
    def default() -> "VersionedTransaction": ...
    @staticmethod
    def from_bytes(data: bytes) -> "VersionedTransaction": ...
    def __richcmp__(self, other: "VersionedTransaction", op: int) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "VersionedTransaction": ...
    @staticmethod
    def from_legacy(tx: Transaction) -> "VersionedTransaction": ...
    def uses_durable_nonce(self) -> bool: ...

class SanitizeError(Exception): ...
class TransactionError(Exception): ...

TransactionVersion = Union[Legacy, int]
