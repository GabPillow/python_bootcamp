class Vector:
    def __init__(self, random_param):
        self.values = random_param
        self.size = 0
    
    @property
    def values(self):
        return self._values
    
    @values.setter
    def values(self, rp):
        if not rp:
            raise AttributeError('No empty param')
        if isinstance(rp, list):
            for nbr in rp:
                if not isinstance(nbr, float):
                    raise TypeError('Number in list have to be float type')
            self._values = rp
        elif isinstance(rp, int):
            self._values = [float(i) for i in range(rp)]
        elif isinstance(rp, tuple):
            if len(rp) != 2:
                raise ValueError('Range can\'t be more than two numbers')
            self._values = [float(i) for i in range(rp[0], rp[1])]
        else:
            raise TypeError('Param have to be a list, int or tuple type')
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, rp):
        self._size = len(self.values)

    def __add__(self, obj):
        if not isinstance(obj, (Vector, int)):
            raise TypeError('Objects have to be int or Vector')
        if isinstance(obj, Vector):
            if obj.size != self.size:
                raise ValueError('Vector have to be the same size')
            return Vector([float(s + o) \
            for s, o in zip(self.values, obj.values)])
        else:
            return Vector([float(i + obj) for i in self.values])
    
    def __radd__(self, obj):
        if not isinstance(obj, (Vector, int)):
            raise TypeError('Objects have to be int or Vector')
        if isinstance(obj, Vector):
            if obj.size != self.size:
                raise ValueError('Vector have to be the same size')
            return Vector([float(s + o) \
            for s, o in zip(self.values, obj.values)])
        else:
            return Vector([float(i + obj) for i in self.values])
    
    def __sub__(self, obj):
        if not isinstance(obj, (Vector, int)):
            raise TypeError('Objects have to be int or Vector')
        if isinstance(obj, Vector):
            if obj.size != self.size:
                raise ValueError('Vector have to be the same size')
            return Vector([float(s - o) \
            for s, o in zip(self.values, obj.values)])
        else:
            return Vector([float(i - obj) for i in self.values])
    
    def __rsub__(self, obj):
        if not isinstance(obj, (Vector, int)):
            raise TypeError('Objects have to be int or Vector')
        if isinstance(obj, Vector):
            if obj.size != self.size:
                raise ValueError('Vector have to be the same size')
            return Vector([float(s - o) \
            for s, o in zip(self.values, obj.values)])
        else:
            return Vector([float(i - obj) for i in self.values])
    
    def __truediv__(self, obj):
        if not isinstance(obj, (Vector, int)):
            raise TypeError('Objects have to be int or Vector')
        if isinstance(obj, Vector):
            if obj.size != self.size:
                raise ValueError('Vector have to be the same size')
            return Vector([float(s / o) \
            for s, o in zip(self.values, obj.values)])
        else:
            return Vector([float(i / obj) for i in self.values])
    
    def __rtruediv__(self, obj):
        if not isinstance(obj, (Vector, int)):
            raise TypeError('Objects have to be int or Vector')
        if isinstance(obj, Vector):
            if obj.size != self.size:
                raise ValueError('Vector have to be the same size')
            return Vector([float(s / o) \
            for s, o in zip(self.values, obj.values)])
        else:
            return Vector([float(i / obj) for i in self.values])
    
    
    def __mul__(self, obj):
        if not isinstance(obj, (Vector, int)):
            raise TypeError('Objects have to be int or Vector')
        if isinstance(obj, Vector):
            if obj.size != self.size:
                raise ValueError('Vector have to be the same size')
            ret = 0
            for o, s in zip(obj.values, self.values):
                ret = int(o * s + ret)
            return ret
        else:
            return Vector([float(i * obj) for i in self.values])
        print('EFFECTIVEMENT')
    
    def __rmul__(self, obj):
        if not isinstance(obj, (Vector, int)):
            raise TypeError('Objects have to be int or Vector')
        if isinstance(obj, Vector):
            if obj.size != self.size:
                raise ValueError('Vector have to be the same size')
            ret = 0
            for o, s in zip(obj.values, self.values):
                ret = int(o * s + ret)
            return ret
        else:
            return Vector([float(i * obj) for i in self.values])
    
    def __str__(self):
        return 'Vector values: {}\nVector SIZE: {}'\
        .format(self.values, self.size)
    
    def __repr__(self):
        return '{}'.format(self.values)