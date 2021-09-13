from enum import Enum


class FailureType(Enum):
    # 401
    NOT_AUTHORIZED_ERROR = ("not_authorized_error", 401)

    # 409
    INTERNAL_ERROR = ("internal_error", 409)
    INVALID_REQUEST_ERROR = ("invalid_request_error", 409)
    NOT_IMPLEMENTED_ERROR = ("not_implemented_error", 409)
    POINT_NOT_ENOUGH_ERROR = ("point_not_enough_error", 409)
    EXTRACT_DATA_ERROR = ("extract_data_error", 409)
    GENERATE_DATA_ERROR = ("generate_data_error", 409)
    UPDATE_DATA_ERROR = ("update_data_error", 409)
    REMOVE_DATA_ERROR = ("remove_data_error", 409)
    UNAVAILABLE_USER_ERROR = ("unavailable_user_error", 409)

    # 409 (To be used)
    DUPLICATE_ERROR = ("duplicate_error", 409)
    ALREADY_DONE_ERROR = ("already_done_error", 409)
    AUTH_INVALID_ERROR = ("auth_invalid_error", 409)
    NOT_FOUND_ERROR = ("not_found_error", 409)
    TOO_MANY_REQUEST_ATTEMPT_ERROR = ("too_many_request_attempt_error", 409)

    # 409 (Matching Algorithm)
    MATCH_ALG_GROUPING_ERROR = ("match_alg_grouping_error", 409)
    MATCH_ALG_FILTERING_ERROR = ("match_alg_filtering_error", 409)
    MATCH_ALG_SCORING_ERROR = ("match_alg_scoring_error", 409)
    MATCH_ALG_MATCHING_ERROR = ("match_alg_matching_error", 409)
    MATCH_ALG_INTERNAL_ERROR = ("match_alg_internal_error", 409)

    # 422
    INPUT_PARAMETER_ERROR = ("input_parameter_error", 422)

    # 500 (legacy)
    LEGACY_PARSING_ERROR = ("parsing_error", 500)
    LEGACY_INTERNAL_ERROR = ("internal_error", 500)
    LEGACY_INVALID_REQUEST_ERROR = ("invalid_request_error", 500)
    LEGACY_NOT_AUTHORIZED_ERROR = ("not_authorized_error", 500)
    LEGACY_NOT_IMPLEMENTED_ERROR = ("not_implemented_error", 500)
    LEGACY_POINT_NOT_ENOUGH_ERROR = ("point_not_enough_error", 500)
    LEGACY_EXTRACT_DATA_ERROR = ("extract_data_error", 500)
    LEGACY_GENERATE_DATA_ERROR = ("generate_data_error", 500)
    LEGACY_UPDATE_DATA_ERROR = ("update_data_error", 500)
    LEGACY_REMOVE_DATA_ERROR = ("remove_data_error", 500)
    LEGACY_UNAVAILABLE_USER_ERROR = ("unavailable_user_error", 500)

    @property
    def error_name(self) -> str:
        """이 에러 타입을 나타내는 보편적인 설명문"""
        return self.value[0]

    @property
    def status_code(self) -> int:
        """이 에러 타입에 대응하는 http status code"""
        return self.value[1]
