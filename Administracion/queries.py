import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType

from .models import *


class DeportesType(DjangoObjectType):
    class Meta:
        model = Deporte
        fields = '__all__'


class DisciplinaType(DjangoObjectType):
    class Meta:
        model = Disciplina
        fields = '__all__'


class DepartamentoType(DjangoObjectType):
    class Meta:
        model = Departamento
        fields = '__all__'


class AreaType(DjangoObjectType):
    class Meta:
        model = Area
        fields = '__all__'


class ServicioType(DjangoObjectType):
    class Meta:
        model = Servicios
        fields = '__all__'


class EvaluacionType(DjangoObjectType):
    class Meta:
        model = Evaluacion
        fields = '__all__'


class LugarType(DjangoObjectType):
    class Meta:
        model = Lugar
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class IndicadoresType(DjangoObjectType):
    class Meta:
        model = Indicadores
        fields = '__all__'
        
class Query(object):
    user_por_nombre = graphene.List(UserType, name=graphene.String())
    deportes_por_nombre = graphene.List(DeportesType, name=graphene.String())
    disciplina_por_nombre = graphene.List(DisciplinaType, name=graphene.String())
    departamento_por_nombre = graphene.List(DepartamentoType, name=graphene.String())
    area_por_nombre = graphene.List(AreaType, name=graphene.String())
    servicio_por_nombre = graphene.List(ServicioType, name=graphene.String())
    evaluacion_por_nombre = graphene.List(EvaluacionType, name=graphene.String())
    lugar_por_nombre = graphene.List(LugarType, name=graphene.String())
    all_deportes = graphene.List(DeportesType)
    all_disciplina = graphene.List(DisciplinaType)
    all_departamento = graphene.List(DepartamentoType)
    all_area = graphene.List(AreaType)
    all_servicio = graphene.List(ServicioType)
    all_evaluacion = graphene.List(EvaluacionType)
    all_lugar = graphene.List(LugarType)
    all_users = graphene.List(UserType)
    disciplina_por_deporte = graphene.List(DisciplinaType, deporte=graphene.Int())
    area_por_departamento = graphene.List(AreaType, departamento=graphene.Int())
    servicio_por_area = graphene.List(ServicioType, area=graphene.Int())
    indicadores = graphene.List(IndicadoresType, name=graphene.String())

    def resolve_user_por_nombre(self, info, name):
        if name == "":
            return User.objects.all()
        else:
            return User.objects.filter(
                Q(username__icontains=name) |
                Q(first_name__icontains=name) |
                Q(last_name__icontains=name) |
                Q(email__icontains=name)
            )

    def resolve_deportes_por_nombre(self, info, name):
        if name == "":
            return Deporte.objects.all()
        else:
            return Deporte.objects.filter(nombre__icontains=name)

    def resolve_disciplina_por_nombre(self, info, name):
        if name == "":
            return Disciplina.objects.all()
        else:
            return Disciplina.objects.filter(
                Q(nombre__icontains=name) |
                Q(deporte__nombre__icontains=name)
            )

    def resolve_departamento_por_nombre(self, info, name):
        if name == "":
            return Departamento.objects.all()
        else:
            return Departamento.objects.filter(nombre__icontains=name)

    def resolve_area_por_nombre(self, info, name):
        if name == "":
            return Area.objects.all()
        else:
            return Area.objects.filter(
                Q(nombre__icontains=name) |
                Q(departamento__nombre__icontains=name)
            )

    def resolve_servicio_por_nombre(self, info, name):
        if name == "":
            return Servicios.objects.all()
        else:
            return Servicios.objects.filter(
                Q(nombre__icontains=name) |
                Q(area__nombre__icontains=name)
            )

    def resolve_evaluacion_por_nombre(self, info, name):
        if name == "":
            return Evaluacion.objects.all()
        else:
            return Evaluacion.objects.filter(nombre__icontains=name)

    def resolve_lugar_por_nombre(self, info, name):
        if name == "":
            return Lugar.objects.all()
        else:
            return Lugar.objects.filter(nombre__icontains=name)

    def resolve_all_deportes(self, info):
        return Deporte.objects.all()

    def resolve_all_disciplina(self, info):
        return Disciplina.objects.all()

    def resolve_all_departamento(self, info):
        return Departamento.objects.all()

    def resolve_all_area(self, info):
        return Area.objects.all()

    def resolve_all_servicio(self, info):
        return Servicios.objects.all()

    def resolve_all_evaluacion(self, info):
        return Evaluacion.objects.all()

    def resolve_all_lugar(self, info):
        return Lugar.objects.all()

    def resolve_disciplina_por_deporte(self, info, deporte):
        return Disciplina.objects.filter(deporte_id=deporte)

    def resolve_area_por_departamento(self, info, departamento):
        return Area.objects.filter(departamento_id=departamento)

    def resolve_servicio_por_area(self, info, area):
        return Servicios.objects.filter(area_id=area)

    def resolve_all_users(self, info):
        return User.objects.all()
    
                
    def resolve_indicadores(self, info, name):
        if name == "":
            return Indicadores.objects.all()
        else:
            return Indicadores.objects.filter(
                Q(indicador__icontains=name) |
                Q(unidad__icontains=name) |
                Q(servicio__nombre__icontains=name)

            )
