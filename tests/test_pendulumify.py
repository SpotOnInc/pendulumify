# -*- coding: utf-8 -*-

import datetime
import pendulum
from decimal import Decimal
from pendulumify import pendulumify


def isInstanceOfPendulum(arg):
    return isinstance(arg, pendulum.Pendulum)


def test_dictionary():
    d = pendulumify({
        'example': datetime.datetime.now(),
        'donottouch': 'safe',
    })

    assert isInstanceOfPendulum(d.get('example'))
    assert d.get('donottouch') == 'safe'

    @pendulumify
    def wrapped():
        return {
            'example': datetime.datetime.now(),
            'donottouch': 'safe',
        }

    assert isInstanceOfPendulum(wrapped().get('example'))
    assert wrapped().get('donottouch') == 'safe'


def test_nested_dictionary():
    d = pendulumify({
        'inner': {
            'example': datetime.datetime.now(),
            'donottouch': 'safe',
        },
    })

    assert isInstanceOfPendulum(d.get('inner').get('example'))
    assert d.get('inner').get('donottouch') == 'safe'

    @pendulumify
    def wrapped():
        return {
            'inner': {
                'example': datetime.datetime.now(),
                'donottouch': 'safe',
            },
        }

    assert isInstanceOfPendulum(wrapped().get('inner').get('example'))
    assert wrapped().get('inner').get('donottouch') == 'safe'


def test_list():
    d = pendulumify([datetime.datetime.now()])

    assert isInstanceOfPendulum(d[0])

    @pendulumify
    def wrapped():
        return [datetime.datetime.now()]

    assert isInstanceOfPendulum(wrapped()[0])


def test_nested_list():
    d = pendulumify([[datetime.datetime.now()]])

    assert isInstanceOfPendulum(d[0][0])

    @pendulumify
    def wrapped():
        return [[datetime.datetime.now()]]

    assert isInstanceOfPendulum(wrapped()[0][0])


def test_set():
    d = pendulumify(set([datetime.datetime.now()]))

    assert isInstanceOfPendulum(d.pop())

    @pendulumify
    def wrapped():
        return set([datetime.datetime.now()])

    assert isInstanceOfPendulum(wrapped().pop())


def test_nested_set():
    d = pendulumify(set([frozenset([datetime.datetime.now()])]))

    assert isInstanceOfPendulum(next(iter(d.pop())))

    @pendulumify
    def wrapped():
        return set([frozenset([datetime.datetime.now()])])

    assert isInstanceOfPendulum(next(iter(wrapped().pop())))


def test_function():
    d = pendulumify(lambda: datetime.datetime.now())

    assert isInstanceOfPendulum(d())

    @pendulumify
    def wrapped():
        def inner():
            return datetime.datetime.now()

        return inner

    assert isInstanceOfPendulum(wrapped()())


def test_generator():
    try:
        xrange
    except NameError:
        xrange = range

    d = pendulumify((datetime.datetime.now() for x in xrange(0, 10)))

    for x in d:
        assert isInstanceOfPendulum(x)

    @pendulumify
    def wrapped():
        def my_gen():
            for x in xrange(0, 10):
                yield datetime.datetime.now()

        return my_gen()

    for x in wrapped():
        assert isInstanceOfPendulum(x)


def test_dictionary_from_generator():
    try:
        xrange
    except NameError:
        xrange = range

    d = pendulumify(
        ({'val': datetime.datetime.now()} for x in xrange(0, 10))
    )

    for x in d:
        assert isInstanceOfPendulum(x.get('val'))

    @pendulumify
    def wrapped():
        def my_gen():
            for x in xrange(0, 10):
                yield {'val': datetime.datetime.now()}

        return my_gen()

    for x in wrapped():
        assert isInstanceOfPendulum(x.get('val'))


def test_passthrough_numbers():
    myint = 1
    myfloat = 1.1
    mydec = Decimal('1.1')

    ret = pendulumify({
        'int': myint,
        'float': myfloat,
        'decimal': mydec,
    })

    assert ret.get('int') == myint
    assert ret.get('float') == myfloat
    assert ret.get('decimal') == mydec
