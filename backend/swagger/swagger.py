from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status

get_params = [
	openapi.Parameter(
        "page",
        openapi.IN_QUERY,
        description="page",
        type=openapi.FORMAT_DATE,
        default=""
    )
]

@swagger_auto_schema(
operation_id='Create a document',
operation_description='Create a document by providing file and s3_key',
anual_parameters=[
                openapi.Parameter('file', openapi.IN_FORM, type=openapi.TYPE_FILE, description='Document to be uploaded'),
                openapi.Parameter('s3_key', openapi.IN_FORM, type=openapi.TYPE_STRING, description='S3 Key of the Document '
                                                                                                   '(folders along with name)')
            ],
responses={
                status.HTTP_200_OK: openapi.Response(
                    'Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'doc_id': openapi.Schema(type=openapi.TYPE_STRING, description='Document ID'),
                        'mime_type': openapi.Schema(type=openapi.TYPE_STRING, description='Mime Type of the Document'),
                        'version_id': openapi.Schema(type=openapi.TYPE_STRING, description='S3 version ID of the document')
                    })
                )
            }
)