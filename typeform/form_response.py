from .form_question import FormQuestion


class FormResponse(object):
    __slots__ = ['_token', '_completed', '_answers', '_hidden', '_metadata']

    def __init__(self, token=None, completed=None, answers=None, hidden=None, metadata=None):
        self._token = token
        self._completed = bool(completed)
        self._answers = answers
        self._hidden = hidden
        self._metadata = metadata

    @property
    def completed(self):
        return self._completed

    @property
    def answers(self):
        return self._answers

    @property
    def hidden(self):
        return self._hidden

    @property
    def metadata(self):
        return self._metadata

    @property
    def token(self):
        return self._token

    def __repr__(self):
        return 'FormResponse(token={token!r})'.format(token=self.token)


class FormResponses(object):
    __slots__ = ['_stats', '_responses', '_questions']

    def __init__(self, stats=None, responses=None, questions=None):
        self._stats = stats

        self._responses = []
        if responses:
            self._responses = [
                FormResponse(**resp) for resp in responses
            ]

        self._questions = []
        if questions:
            self._questions = [
                FormQuestion(**question) for question in questions
            ]

    @property
    def responses(self):
        return self._responses

    @property
    def stats(self):
        return self._stats

    @property
    def questions(self):
        return self._questions

    def __repr__(self):
        return (
            'FormResponses(questions={questions!r}, responses={responses!r})'
            .format(questions=len(self.questions), responses=len(self.responses))
        )
