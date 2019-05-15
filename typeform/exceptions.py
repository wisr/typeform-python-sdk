class TypeFormError(Exception):
    def __init__(self, response_body):
        """
        Raises for typeform specific errors. Returns a typeform error code as well
        as a description of the error.
        """
        super().__init__(response_body)
        if isinstance(response_body, dict):
            self.code = response_body.get("code", None)
            self.description = response_body.get("description", None)
            self.field = response_body.get("field", None)
        else:
            raise Exception(response_body)
