from flask import Flask

app = Flask(__name__)


module_info = {
    "aerospike": {
        "devops": {
            "v1.0.1": "s3: aerospike-devops-v1-0-1.tar.gz",
            "v1.0.2": "s3: aerospike-devops-v1-0-2.tar.gz"
        },
        "develop": {
            "v1.0.1": "s3: aerospike-develop-v1-0-1.tar.gz"
        }
    },
    "auth": {
        "devops": {
            "v1.0.1": "s3: auth-devops-v1-0-1.tar.gz",
            "v1.0.2": "s3: auth-devops-v1-0-2.tar.gz"
        },
        "develop": {
            "v1.0.1": "s3: auth-develop-v1-0-1.tar.gz"
        }
    }
}


@app.route("/tfmodules")
def all_map():
    return module_info


@app.route("/tfmodules/<module_name>")
def modules(module_name):
    if module_info.get(module_name):
        module_map = module_info.get(module_name)
        return module_map
    else:
        return "Error finding {}".format(module_name)


@app.route("/tfmodules/<module_name>/<provider>")
def providers(module_name, provider):
    if module_info.get(module_name):
        if module_info.get(module_name).get(provider):
            module_map = module_info.get(module_name).get(provider)
            return module_map
        else:
            return "Error finding {}/{}".format(module_name, provider)
    else:
        return "Error finding {}".format(module_name)


@app.route("/tfmodules/<module_name>/<provider>/<version>")
def user_info(module_name, provider, version):
    if module_info.get(module_name):
        if module_info.get(module_name).get(provider):
            if module_info.get(module_name).get(provider).get(version):
                module_map = module_info.get(module_name).get(provider).get(version)
                return module_map
            else:
                return "Error finding {}/{}/{}".format(module_name, provider, version)
        else:
            return "Error finding {}/{}".format(module_name, provider)
    else:
        return "Error finding {}".format(module_name)


@app.errorhandler(404)
def page_not_found(e):
    return "Invalid request"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
