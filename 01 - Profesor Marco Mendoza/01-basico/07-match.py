#este match esta basado en un funcion precreada para sitios webs de estado del servidor
def http_error(status):
    match status:
        case 400:
            return 'Solicitud incorrecta'
        case 404:
            return 'no encontrado'
        case 418:
            return 'Soy una tetera'
        case _:
            return 'Algo anda mal en internet'
print(http_error(418))