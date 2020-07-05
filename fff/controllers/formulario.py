import web

render = web.template.render("fff/views/")

class Formulario():

    def GET(self):
      try:
        return render.formu()
      except Exception as e:
        return "Error " + str(e.args)
