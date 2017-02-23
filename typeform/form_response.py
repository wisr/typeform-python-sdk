from .form_answer import FormAnswer
from .form_question import FormQuestion


class FormResponse(object):
    __slots__ = ['_token', '_completed', '_answers', '_hidden', '_metadata', '_questions']

    def __init__(self, token=None, completed=None, answers=None, hidden=None, metadata=None, questions=None):
        self._token = token
        self._completed = bool(completed)
        self._hidden = hidden
        self._metadata = metadata
        self._questions = questions

        self._answers = []
        for question_id, answer in answers.items():
            question = self.get_question(question_id)
            self._answers.append(
                FormAnswer(answer=answer, question=question.question, question_id=question.id)
            )

    @property
    def questions(self):
        return self._questions

    def get_question(self, id):
        if not self.questions:
            return None

        for question in self.questions:
            if question.id == id:
                return question

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

        self._questions = []
        if questions:
            self._questions = [
                FormQuestion(**question) for question in questions
            ]

        self._responses = []
        if responses:
            self._responses = [
                FormResponse(
                    token=resp.get('token'),
                    completed=resp.get('completed'),
                    hidden=resp.get('hidden'),
                    metadata=resp.get('metadata'),
                    answers=resp.get('answers'),
                    questions=self._questions,
                )
                for resp in responses
            ]

    def get_question(self, id):
        if not self.questions:
            return None

        for question in self.questions:
            if question.id == id:
                return question

    @property
    def responses(self):
        return self._responses

    def get_response(self, token):
        if not self.responses:
            return None

        for response in self.responses:
            if response.token == token:
                return response

    @property
    def stats(self):
        return self._stats

    @property
    def questions(self):
        return self._questions

    def __getitem__(self, idx):
        return self.responses[idx]

    def __len__(self):
        return len(self.responses)

    def __iter__(self):
        return iter(self.responses)

    def __repr__(self):
        return (
            'FormResponses(questions={questions!r}, responses={responses!r})'
            .format(questions=len(self.questions), responses=len(self.responses))
        )
