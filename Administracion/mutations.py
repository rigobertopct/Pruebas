import graphene
from graphene import Mutation

from .models import *


class NuevoDeporteMutation(Mutation):
    class Arguments:
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre):
        try:
            Deporte.objects.create(nombre=nombre)
            return NuevoDeporteMutation(success=True, error=None)
        except Exception as e:
            return NuevoDeporteMutation(success=False, error=str(e))


class NuevaDisciplinaMutation(Mutation):
    class Arguments:
        deporte = graphene.Int(required=True)
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, deporte):
        try:
            deporte = Deporte.objects.get(id=deporte)
            Disciplina.objects.create(nombre=nombre, deporte=deporte)
            return NuevaDisciplinaMutation(success=True, error=None)
        except Exception as e:
            return NuevaDisciplinaMutation(success=False, error=str(e))


class NuevoDepartamentoMutation(Mutation):
    class Arguments:
        siglas = graphene.String(required=True)
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, siglas):
        try:
            Departamento.objects.create(nombre=nombre, sigla=siglas)
            return NuevoDepartamentoMutation(success=True, error=None)
        except Exception as e:
            return NuevoDepartamentoMutation(success=False, error=str(e))


class NuevaAreaMutation(Mutation):
    class Arguments:
        siglas = graphene.String(required=True)
        nombre = graphene.String(required=True)
        departamento = graphene.Int(required=True)
        responsable = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, siglas, departamento, responsable):
        try:
            depa = Departamento.objects.get(id=departamento)
            user = User.objects.get(id=responsable)
            Area.objects.create(nombre=nombre, sigla=siglas, responsable=user, departamento=depa)
            return NuevaAreaMutation(success=True, error=None)
        except Exception as e:
            return NuevaAreaMutation(success=False, error=str(e))


class NuevoLugarMutation(Mutation):
    class Arguments:
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre):
        try:
            Lugar.objects.create(nombre=nombre)
            return NuevoLugarMutation(success=True, error=None)
        except Exception as e:
            return NuevoLugarMutation(success=False, error=str(e))


class NuevaEvaluacionMutation(Mutation):
    class Arguments:
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre):
        try:
            Evaluacion.objects.create(nombre=nombre)
            return NuevaEvaluacionMutation(success=True, error=None)
        except Exception as e:
            return NuevaEvaluacionMutation(success=False, error=str(e))


class EliminarDeporteMutation(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id):
        try:
            deporte = Deporte.objects.get(id=id)
            deporte.delete()
            return EliminarDeporteMutation(success=True, error=None)
        except Exception as e:
            return EliminarDeporteMutation(success=False, error=str(e))


class EliminarDisciplinaMutation(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id):
        try:
            disciplina = Disciplina.objects.get(id=id)
            disciplina.delete()
            return EliminarDisciplinaMutation(success=True, error=None)
        except Exception as e:
            return EliminarDisciplinaMutation(success=False, error=str(e))


class EliminarDepartamentoMutation(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id):
        try:
            departamento = Departamento.objects.get(id=id)
            departamento.delete()
            return EliminarDepartamentoMutation(success=True, error=None)
        except Exception as e:
            return EliminarDepartamentoMutation(success=False, error=str(e))


class EliminarAreaMutation(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id):
        try:
            area = Area.objects.get(id=id)
            area.delete()
            return EliminarAreaMutation(success=True, error=None)
        except Exception as e:
            return EliminarAreaMutation(success=False, error=str(e))


class EliminarLugarMutation(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id):
        try:
            lugar = Lugar.objects.get(id=id)
            lugar.delete()
            return EliminarLugarMutation(success=True, error=None)
        except Exception as e:
            return EliminarLugarMutation(success=False, error=str(e))


class EliminarEvaluacionMutation(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id):
        try:
            evaluacion = Evaluacion.objects.get(id=id)
            evaluacion.delete()
            return EliminarEvaluacionMutation(success=True, error=None)
        except Exception as e:
            return EliminarEvaluacionMutation(success=False, error=str(e))


class ActualizarDeporteMutation(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, id):
        try:
            deporte = Deporte.objects.get(id=id)
            deporte.nombre = nombre
            deporte.save()
            return ActualizarDeporteMutation(success=True, error=None)
        except Exception as e:
            return ActualizarDeporteMutation(success=False, error=str(e))


class ActualizarDisciplinaMutation(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        deporte = graphene.Int(required=True)
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, deporte, id):
        try:
            disciplina = Disciplina.objects.get(id=id)
            deporte = Deporte.objects.get(id=deporte)
            disciplina.deporte = deporte
            disciplina.nombre = nombre
            disciplina.save()
            return ActualizarDisciplinaMutation(success=True, error=None)
        except Exception as e:
            return ActualizarDisciplinaMutation(success=False, error=str(e))


class ActualizarDepartamentoMutation(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        siglas = graphene.String(required=True)
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, siglas, id):
        try:
            departamento = Departamento.objects.get(id=id)
            departamento.sigla = siglas
            departamento.nombre = nombre
            departamento.save()
            return ActualizarDepartamentoMutation(success=True, error=None)
        except Exception as e:
            return ActualizarDepartamentoMutation(success=False, error=str(e))


class ActualizarAreaMutation(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        siglas = graphene.String(required=True)
        nombre = graphene.String(required=True)
        departamento = graphene.Int(required=True)
        responsable = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, siglas, departamento, responsable, id):
        try:
            user = User.objects.get(id=responsable)
            depa = Departamento.objects.get(id=departamento)
            area = Area.objects.get(id=id)
            area.nombre = nombre
            area.sigla = siglas
            area.departamento = depa
            area.responsable = user
            area.save()
            return ActualizarAreaMutation(success=True, error=None)
        except Exception as e:
            return ActualizarAreaMutation(success=False, error=str(e))


class ActualizarLugarMutation(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, id):
        try:
            lugar = Lugar.objects.get(id=id)
            lugar.nombre = nombre
            lugar.save()
            return ActualizarLugarMutation(success=True, error=None)
        except Exception as e:
            return ActualizarLugarMutation(success=False, error=str(e))


class ActualizarEvaluacionMutation(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, id):
        try:
            evaluacion = Evaluacion.objects.get(id=id)
            evaluacion.nombre = nombre
            evaluacion.save()
            return ActualizarEvaluacionMutation(success=True, error=None)
        except Exception as e:
            return ActualizarEvaluacionMutation(success=False, error=str(e))

class NuevoIndicador(Mutation):
    class Arguments:
        indicador = graphene.String(required=True)
        servicio = graphene.Int(required=True)        
        unidad = graphene.String(required=False)        
               
    
    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, indicador, servicio, unidad):
        try:
            item_indicador = indicador
            item_servicio = Servicios.objects.get(id=servicio)
            item_unidad = unidad
            Indicadores.objects.create(indicador=item_indicador, servicio=item_servicio,unidad=item_unidad) 
            return NuevoIndicador(success=True, errors=None)
        except Exception as e:
            return NuevoIndicador(success=False, errors=str(e))

class ActualizarIndicador(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        indicador = graphene.String(required=False)
        unidad = graphene.String(required=False)
        servicio = graphene.Int(required=False)           
                  
    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, indicador,unidad, servicio,id):
        try:
            item = Indicadores.objects.get(id=id)           
            item_servicio = Servicios.objects.get(id=servicio)            
            item.unidad = unidad
            item.servicio = item_servicio
            item.indicador = indicador
            item.save()
            return ActualizarIndicador(success=True, errors=None)
        except Exception as e:
            return ActualizarIndicador(success=False, errors=str(e))

class EliminarIndicador(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Indicadores.objects.get(id=id)
            item.delete()
            return EliminarIndicador(success=True, errors=None)
        except Exception as e:
            return EliminarIndicador(success=False, errors=str(e))


class NuevoServicio(Mutation):
    class Arguments:
        nombre = graphene.String()
        simbolo = graphene.String()
        objetivo = graphene.String()
        area = graphene.Int()

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, simbolo, objetivo, area):
        try:
            item_area = Area.objects.get(id=area)
            Servicios.objects.create(nombre=nombre, simbolo=simbolo, objetivo=objetivo, area=item_area)
            return NuevoServicio(success=True, errors=None)
        except Exception as e:
            return NuevoServicio(success=False, errors=str(e))


class ActualizarServicio(Mutation):
    class Arguments:
        nombre = graphene.String()
        simbolo = graphene.String()
        objetivo = graphene.String()
        area = graphene.Int()
        id = graphene.Int()

    success = graphene.Boolean()
    errors = graphene.String()
    
class EliminarServicio(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Servicios.objects.get(id=id)
            item.delete()
            return EliminarServicio(success=True, errors=None)
        except Exception as e:
            return EliminarServicio(success=False, errors=str(e))



class NuevoDeportista(Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        edad = graphene.Int(required=True)
        peso = graphene.Decimal(required=True)
        estatura = graphene.Decimal(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, edad, peso, estatura):
        try:
            Deportista.objects.create(nombre=nombre, edad=edad, peso=peso, estatura=estatura)
            return NuevoDeportista(success=True, errors=None)
        except Exception as e:
            return NuevoDeportista(success=False, errors=str(e))


class ActualizarDeportista(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nombre = graphene.String(required=True)
        edad = graphene.Int(required=True)
        peso = graphene.Decimal(required=True)
        estatura = graphene.Decimal(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, edad, peso, estatura, id):
        try:
            item = Deportista.objects.get(id=id)
            item.nombre = nombre
            item.edad = edad
            item.peso = peso
            item.estatura = estatura
            item.save()
            return ActualizarDeportista(success=True, errors=None)
        except Exception as e:
            return ActualizarDeportista(success=False, errors=str(e))


class EliminarDeportista(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Deportista.objects.get(id=id)
            item.delete()
            return EliminarDeportista(success=True, errors=None)
        except Exception as e:
            return EliminarDeportista(success=False, errors=str(e))

class NuevaPrueba(Mutation):
    class Arguments:
        fecha = graphene.Date(required=True)
        deporte = graphene.Int(required=True)
        deportista = graphene.Int(required=True)
        servicio = graphene.Int(required=True)
        lugar = graphene.Int(required=True)
        evaluacion = graphene.Int(required=False)
        resultado = graphene.String(required=True)
        observaciones = graphene.String(required=True)
        valoracion = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, fecha, deporte, deportista, servicio, lugar,
               evaluacion, resultado, observaciones, valoracion):
        try:
            Prueba.objects.create(fecha=fecha,
                                  deporte=deporte, deportista=deportista,
                                  servicio=servicio,lugar=lugar,
                                  evaluacion=evaluacion,observaciones=observaciones,
                                  valoracion=valoracion, resultado=resultado)
            return NuevaPrueba(success=True, errors=None)
        except Exception as e:
            return NuevaPrueba(success=False, errors=str(e))


class ActualizarPrueba(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        fecha = graphene.Date(required=True)
        deporte = graphene.Int(required=True)
        deportista = graphene.Int(required=True)
        lugar = graphene.Int(required=True)
        servicio = graphene.Int(required=True)
        evaluacion = graphene.Int(required=True)
        observaciones = graphene.String(required=False)
        valoracion = graphene.String(required=False)
        resultado = graphene.String(required=False)

    success = graphene.Boolean() 
    errors = graphene.String()

    def mutate(self, info, fecha, deporte, deportista, lugar,
               servicio, evaluacion, observaciones, valoracion, resultado,id):
        try:
            item = Prueba.objects.get(id=id)
            item_deporte = Deporte.objects.get(id=deporte)
            item_deportista = Deportista.objects.get(id=deportista)
            item_lugar = Lugar.objects.get(id=lugar)
            item_servicio = Servicios.objects.get(id=servicio)
            item_evaluacion = Evaluacion.objects.get(id=evaluacion)
            item.fecha = fecha
            item.deporte = item_deporte
            item.deportista = item_deportista
            item.lugar = item_lugar
            item.servicio = item_servicio
            item.evaluacion = item_evaluacion
            item.observaciones = observaciones
            item.valoracion = valoracion
            item.resultado = resultado
            item.save()
            return ActualizarPrueba(success=True, errors=None)
        except Exception as e:
            return ActualizarPrueba(success=False, errors=str(e))


class EliminarPrueba(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Prueba.objects.get(id=id)
            item.delete()
            return EliminarPrueba(success=True, errors=None)
        except Exception as e:
            return EliminarPrueba(success=False, errors=str(e))



class Mutation(graphene.ObjectType):
    nuevo_deporte = NuevoDeporteMutation.Field()
    nueva_disciplina = NuevaDisciplinaMutation.Field()
    nuevo_departamento = NuevoDepartamentoMutation.Field()
    nueva_area = NuevaAreaMutation.Field()
    nuevo_lugar = NuevoLugarMutation.Field()
    nueva_evaluacion = NuevaEvaluacionMutation.Field()
    actualizar_deporte = ActualizarDeporteMutation.Field()
    actualizar_disciplina = ActualizarDisciplinaMutation.Field()
    actualizar_departamento = ActualizarDepartamentoMutation.Field()
    actualizar_area = ActualizarAreaMutation.Field()
    actualizar_lugar = ActualizarLugarMutation.Field()
    actualizar_evaluacion = ActualizarEvaluacionMutation.Field()
    eliminar_deporte = EliminarDeporteMutation.Field()
    eliminar_disciplina = EliminarDisciplinaMutation.Field()
    eliminar_departamento = EliminarDepartamentoMutation.Field()
    eliminar_area = EliminarAreaMutation.Field()
    eliminar_lugar = EliminarLugarMutation.Field()
    eliminar_evaluacion = EliminarEvaluacionMutation.Field()
    nuevoIndicador = NuevoIndicador.Field()
    actualizarIndicador = ActualizarIndicador.Field()
    eliminarIndicador = EliminarIndicador.Field()
    nuevoServicio = NuevoServicio.Field()
    actualizarServicio = ActualizarServicio.Field()
    eliminarServicio = EliminarServicio.Field()
    nuevoDeportista = NuevoDeportista.Field()
    actualizarDeportista = ActualizarDeportista.Field()
    eliminarDeportista = EliminarDeportista.Field()
    nuevaPrueba = NuevaPrueba.Field()
    actualizarPrueba = ActualizarPrueba.Field()
    eliminarPrueba = EliminarPrueba.Field()

