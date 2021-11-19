class Foo:
    def __init__(self):
        print('In Foo')
        self.foo = 'foo'

    def addY(self):
        print("ADD IN FOO")


class Bar:
    def __init__(self, bar):
        print('In Bar')
        self.bar = bar

    def add(self):
        print("ADD IN BAR")


class FooBar(Foo, Bar):
    def __init__(self, bar='bar'):
        print('In FooBar')
        super().__init__()  # this calls all constructors up to Foo
        super(Foo, self).__init__(bar)  # this calls all constructors after Foo up # to Bar

    def addX(self):
        print("ADD IN FOOBAR")


class FooBar2(Foo, Bar):
    def __init__(self, bar='bar'):
        print('In FooBar2')
        Foo.__init__(self)  # explicit calls without super
        Bar.__init__(self, bar)


print("Executing foobar")
foobar = FooBar()
foobar.add()
print("Executing foobar2")
foobar = FooBar2()
