def init(data):
    data[ 'first' ] = {}
    data[ 'middle' ] = {}
    data[ 'last' ] = {}


def lookup(data, label, name):
    return data[ label ].get ( name )


def store(data, full_name):
    names = full_name.split ()
    if len ( names ) == 2: names.insert ( 1, '' )
    labels = 'first', 'middle', 'last'
    for label, name in zip ( labels, names ):
        people = lookup ( data, labels, name )
        if people:
            people.append ( full_name )
        else:
            data[ label ][ name ] = [ full_name ]

Mynames = {}
init(Mynames)
store(Mynames,'Magnus Lie Heland')
lookup(Mynames,'middle', 'Lie')

# store(MyNames,'Robin Hood')
# store(MyNames,'Robin Locksley')
# lookup(MyNames,'first', 'Robin')
