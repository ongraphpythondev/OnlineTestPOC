from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from TestApp.permissions import IsAuthenticatedExaminer, IsAuthenticatedExaminee
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, RetrieveAPIView, \
    UpdateAPIView

from exam.models import Exam, Question, Option, Test, Answer
from exam.serializers import ExamSerializer, QuestionSerializer, OptionSerializer, TestSerializer, \
    AnswerSerializer


class ExamCreateView(CreateAPIView):
    permission_classes = (IsAuthenticatedExaminer,)
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['examiner'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ExamListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ExamSerializer

    def get_queryset(self):
        me = self.request.GET.get('me')
        uid = self.request.GET.get('id')
        if me:
            Exam.objects.filter(examiner=self.request.user)
        elif uid:
            Exam.objects.filter(examiner__id=uid)
        else:
            return Exam.objects.all()


class QuestionCreateView(CreateAPIView):
    permission_classes = (IsAuthenticatedExaminer,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class OptionCreateView(CreateAPIView):
    permission_classes = (IsAuthenticatedExaminer,)
    serializer_class = OptionSerializer
    queryset = Option.objects.all()


class TestCreateView(CreateAPIView):
    permission_classes = (IsAuthenticatedExaminee,)
    serializer_class = TestSerializer
    queryset = Test.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AnswerCreateView(CreateAPIView):
    permission_classes = (IsAuthenticatedExaminee,)
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
