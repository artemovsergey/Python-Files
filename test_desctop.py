from flask import Flask
app = Flask(__name__)


@app.route('/home/<user>')
def home(user):
	return 'Hello {}'.format(user)

#2 summa
@app.route('/page1/<par1>/<par2>')
def page1(par1,par2):

	return "Сумма {} и {}: {}".format(par1,par2,int(par1)+int(par2))

#3 конкатенация 3 строк
@app.route('/concat/<par1>/<par2>/<par3>')
def concat(par1,par2,par3):
	return "Конкатенация строк: {} {} {}".format(par1,par2,par3)

#4
@app.route('/download/<par1>')
def download(par1):
	f = open(par1)
	return f 





if __name__ == '__main__':
	app.run()

# должен быть пользователь (model)
# пользователь должен видеть UI (view)
# должно быть взаимодействие с данными




