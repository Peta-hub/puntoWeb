from django.shortcuts import redirect


def no_es_admin(vista):
    def interna(request, pk=''):
        if not request.user.is_superuser:
            return redirect('clientes')
        return vista(request, pk)
    return interna

def no_admin(vista):
    def interna(request):
        if not request.user.is_superuser:
            return redirect('clientes')
        return vista(request)
    return interna