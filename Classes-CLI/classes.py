class X:
    def __init__(self, name):
        self.name = name
        self.count_a = 0
        self.count_b = 0
        self.count_c = 0
        print("Object name:", self.name)

    def execute(self, dict, type):
        if type=='A':
            self.count_a += 1
            print("A type called:", self.count_a)
        if type=='B':
            self.count_b += 1
            print("B type called:", self.count_b)
        if type=='C':
            self.count_c += 1
            print("C type called:", self.count_c)
        print("Object name:", self.name)
        print(dict)

    def shutdown(self):
        print("Object name:", self.name)


class A(X):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.count = 0
        print("Class name: A")

    def execute(self, dict):
        super().execute(dict, 'A')
        print("Class name: A")
        self.count += 1
        print("Object called times:", self.count)

    def shutdown(self):
        super().shutdown()
        print("Class name: A")


class B(X):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.count = 0
        print("Class name: B")

    def execute(self, dict):
        super().execute(dict, 'B')
        print("Class name: B")
        self.count += 1
        print("Object called times:", self.count)

    def shutdown(self):
        super().shutdown()
        print("Class name: B")


class C(X):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.count = 0
        print("Class name: C")

    def execute(self, dict):
        super().execute(dict, 'C')
        print("Class name: C")
        self.count += 1
        print("Object called times:", self.count)

    def shutdown(self):
        super().shutdown()
        print("Class name: C")
