def addfn(x=1,y=2):
    return x+y

class Dispatcher:
    CMDS = {}

    def reg(self, cmd, fn):
        if cmd == 'add':
            self.CMDS[cmd] = addfn

    def run(self):
        while True:
            cmd = input('plz input your command ').strip()
            if cmd == 'quit':
                return
            self.CMDS.get(cmd, self.defaultfn)()

    def defaultfn(self):
        print('unknow command')


if __name__ == '__main__':
    dis = Dispatcher()
    dis.run()
    print(dis.CMDS)
    print(dis.__dict__)
