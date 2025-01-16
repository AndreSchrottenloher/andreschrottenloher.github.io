from hashlib import sha256, md5, sha1
from random import randrange


def md_hash_1(message_blocks, initial_value=0x12345678):
    """
    Args:
        message_blocks: list of message blocks as 64-bit integers
        initial_value (int): initial value as 32-bit integer

    Returns:
        int: hash of the message as a 32-bit integer.
    """
    chaining_value = initial_value

    for block in message_blocks:
        data = chaining_value.to_bytes(4, 'little') + block.to_bytes(8, 'little')
        chaining_value = int(sha256(data).hexdigest()[:8], 16)  # Use first 32 bits

    return chaining_value


def md_hash_2(message_blocks, initial_value=0x87654321):
    chaining_value = initial_value

    for block in message_blocks:
        data = chaining_value.to_bytes(4, 'little') + block.to_bytes(8, 'little')
        chaining_value = int(md5(data).hexdigest()[:8], 16)  # Use first 32 bits

    return chaining_value



def md_hash_3(message_blocks, initial_value=0x12345678):
    chaining_value = initial_value
    for block in message_blocks:
        data = chaining_value.to_bytes(4, 'little') + block.to_bytes(8, 'little')
        chaining_value = int(sha256(data).hexdigest()[:5], 16)
    return chaining_value


def md_hash_4(message_blocks, initial_value=0x87654321):
    chaining_value = initial_value
    for block in message_blocks:
        data = chaining_value.to_bytes(4, 'little') + block.to_bytes(8, 'little')
        chaining_value = int(md5(data).hexdigest()[:5], 16)
    return chaining_value




