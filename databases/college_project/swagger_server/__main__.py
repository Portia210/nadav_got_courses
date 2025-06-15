#!/usr/bin/env python3

import connexion
from swagger_server import encoder
from swagger_server.StudentManager import StudentManager

# deaulat docs route http://localhost:1234/college_api/ui/

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder

    # Instantiate StudentManager and add it to app config
    app.app.config['STUDENT_MANAGER'] = StudentManager()

    app.add_api('swagger.yaml', arguments={'title': 'College API'}, pythonic_params=True)
    app.run(host="0.0.0.0", port=1234)

if __name__ == '__main__':
    main()
