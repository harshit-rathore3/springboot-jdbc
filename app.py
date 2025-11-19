# import os
# import hashlib
# import config
# from flask_cors import CORS, cross_origin
# from flask import Flask, request, Blueprint
# from pymongo import MongoClient
# from flasgger import Swagger
# from App import create_app
# # from training_module.dependancy_graph.routes import dependancy_prefix
# # from flask_caching import Cache


# # blueprint_prefix = Blueprint('prefix', __name__, url_prefix='/api')

# folder_name = 'prompt_storage'
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)
#     print(f"The folder '{folder_name}' has been created.")
# else:
#     print(f"The folder '{folder_name}' already exists.")


# # ############################ HELPER API ############################
# # @blueprint_prefix.get("/")
# # @cross_origin(supports_credentials=True)
# # def root():
# #     return {"server running": "true"}, 200



from flask import Flask
import config
from flask_cors import CORS
import os
from training_module.dependancy_graph.routes import dependancy_prefix
from training_module.custom_test.routes import custom_test_bp
from training_module.vulnerability_check.routes import vulnerability_check_bp
from training_module.feedback.routes import feedback_bp
from training_module.unit_test.routes import unit_test_bp
from training_module.bulk_conversion.routes import bulk_conversion_prefix
from training_module.module_conversion.routes import module_conversion
from training_module.php_upgradation.routes import php_upgrade

from coding_standards.al_suggestions.routes import ai_suggestion_bp
from coding_standards.code_profile_management.routes import code_profile_management_bp
from coding_standards.project_management.routes import project_management_bp
from coding_standards.webpack_management.routes import webpack_management_bp
from coding_standards.github_integration.routes import github_intergration_bp
from coding_standards.others.routes import others_bp
from coding_standards.architecture_design.routes import arch_design



def create_app():
    app = Flask(__name__)
    config.cache.init_app(app)

    app.config['CACHE_TYPE'] = 'RedisCache'
    app.config['CACHE_REDIS_HOST'] = config.REDIS_HOST  # Replace with your Redis server address
    app.config['CACHE_REDIS_PORT'] = 6379
    app.config['CACHE_REDIS_DB'] = config.REDIS_DB
    # app.config['CACHE_REDIS_URL'] = config.REDIS_URL
    app.config['CACHE_REDIS_PASSWORD'] = config.REDIS_PASSWORD

    app.register_blueprint(dependancy_prefix, url_prefix='/api')
    app.register_blueprint(custom_test_bp, url_prefix='/api')
    app.register_blueprint(vulnerability_check_bp, url_prefix='/api')
    app.register_blueprint(feedback_bp, url_prefix='/api')
    app.register_blueprint(ai_suggestion_bp, url_prefix='/api')
    app.register_blueprint(code_profile_management_bp, url_prefix='/api')
    app.register_blueprint(project_management_bp, url_prefix='/api')
    app.register_blueprint(webpack_management_bp, url_prefix='/api')
    app.register_blueprint(github_intergration_bp, url_prefix='/api')
    app.register_blueprint(unit_test_bp, url_prefix='/api')
    app.register_blueprint(others_bp, url_prefix='/api')
    app.register_blueprint(bulk_conversion_prefix,url_prefix='/api')
    app.register_blueprint(arch_design, url_prefix='/api')
    app.register_blueprint(module_conversion, url_prefix='/api')
    app.register_blueprint(php_upgrade, url_prefix='/api')
    return app


if __name__ == "__main__":
    app = create_app()

    folder_name = 'prompt_storage'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"The folder '{folder_name}' has been created.")
    else:
        print(f"The folder '{folder_name}' already exists.")

    CORS(app, support_credentials=True)
    app.run("0.0.0.0", port=5002, debug=True, use_reloader=False)
