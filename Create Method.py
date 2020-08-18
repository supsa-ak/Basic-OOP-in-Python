class hello:
  def __init__(g,a):
    g.data = a

  def show(g):
    print(g.data)

#if method is init then
x=hello("ball")
y=hello("boss")

x.show() #objectname.method
y.show() #objectname.method
