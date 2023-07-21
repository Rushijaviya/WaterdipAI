from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
)
from .models import TaskTable
from .serializers import TaskSerializer

# Create your views here.

class TaskView(APIView):
    def post(self,request):
        tasks = self.request.data.get('tasks')
        if tasks:
            res= []
            for task in tasks:
                obj = TaskTable.objects.create(title=task['title'],is_completed=task['is_completed'])
                res.append({'id':obj.id})
            return Response({'tasks':res},status=HTTP_201_CREATED)
        
        title = self.request.data.get('title')
        obj = TaskTable.objects.create(title=title)
        return Response({'id':obj.id},status=HTTP_201_CREATED)
    
    def get(self,request,id=None):
        if id:
            try:
                data = TaskTable.objects.get(id=id)
                data = TaskSerializer(data).data
                return Response(data,status=HTTP_200_OK)
            except:
                return Response({'error': "There is no task at that id"},status=HTTP_404_NOT_FOUND)
        
        data = TaskTable.objects.all()
        data = TaskSerializer(data,many=True).data
        return Response({'tasks':data},status=HTTP_200_OK)
    
    def delete(self,request,id=None):
        tasks = self.request.data.get('tasks')
        if tasks:
            for task in tasks:
                try:
                    task_query =  TaskTable.objects.get(id=task['id'])
                    task_query.delete()
                except:
                    pass
            return Response(status=HTTP_204_NO_CONTENT)
        
        try:
            task_query =  TaskTable.objects.get(id=id)
            task_query.delete()
        except:
            pass
        return Response(status=HTTP_204_NO_CONTENT)
    
    def put(self,request,id=None):
        try:
            task_query =  TaskTable.objects.get(id=id)
        except:
            return Response({'error': "There is no task at that id"},status=HTTP_404_NOT_FOUND)
        title = self.request.data.get('title')
        is_completed = self.request.data.get('is_completed')
        task_query.title = title
        task_query.is_completed = is_completed
        task_query.save()
        return Response(status=HTTP_204_NO_CONTENT)