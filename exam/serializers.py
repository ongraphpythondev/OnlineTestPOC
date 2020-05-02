from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from exam.models import Exam, Question, Answer, Test, Option


class OptionSerializer(ModelSerializer):

    def validate_question(self, value):
        if value not in Question.objects.filter(exam__examiner=self.context.get('request').user):
            raise serializers.ValidationError("Can Only Add options to own exam's questions")
        return value

    class Meta:
        model = Option
        fields = '__all__'


class QuestionSerializer(ModelSerializer):

    def validate_exam(self, value):
        if value not in self.context.get('request').user.exams.all():
            raise serializers.ValidationError("Can Only Add questions to own exams")
        return value

    class Meta:
        model = Question
        fields = '__all__'


class ExamSerializer(ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
