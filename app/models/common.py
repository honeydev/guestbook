

class BaseModel:

    SELECT_ONE_SELECTION_MAX_LEN = 1

    def select_one(self, query: str) -> dict:
        raise NotImplementedError(
            'select_all must be implemented in child class'
        )

    def create_one(self, query: str) -> dict:
        raise NotImplementedError(
            'select_all must be implemented in child class'
        )

    def _merge_headers_with_notes(self, query_result: dict) -> tuple:
        headers: dict = query_result['headers']
        values: list = query_result['values']
        return tuple(map(lambda row: dict(zip(headers, row)), values))


class ModelException(Exception):
    """ Model level common exception. """


class ModelNotFoundException(Exception):
    """ Not found row in db exception. """
