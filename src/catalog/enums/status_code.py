from enum import StrEnum


class ResponseCode(StrEnum):
    SUCCESS = "success"
    NOT_FOUND = "not_found"
    FAILED = "failed"