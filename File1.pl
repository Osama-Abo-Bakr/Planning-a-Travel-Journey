% Final project
% Knowledge base
place('Cairo').
place('Alex').
place('Read sea').
place('Aswan').
place('Menofia').
place('Hurgada').
place('Matrouh').
place('Port said').
place('Sainai').
place('Luxor').

transport(car).
transport(train).
transport(plane).

connection('Cairo','Alex',car).
connection('Cairo','Read sea',plane).
connection('Cairo','Aswan',train).
connection('Cairo','Menofia',car).
connection('Cairo','Hurgada',plane).
connection('Cairo','Matrouh',train).
connection('Cairo','Port said',plane).
connection('Cairo','Sainai',plane).
connection('Cairo','Luxor',train).

connection('Alex','Cairo',car).
connection('Alex','Read sea',plane).
connection('Alex','Aswan',train).
connection('Alex','Menofia',car).
connection('Alex','Hurgada',plane).
connection('Alex','Matrouh',train).
connection('Alex','Port said',plane).
connection('Alex','Sainai',plane).
connection('Alex','Luxor',plane).

connection('Read sea','Cairo',plane).
connection('Read sea','Alex',plane).
connection('Read sea','Aswan',train).
connection('Read sea','Hurgada',car).
connection('Read sea','Matrouh',plane).
connection('Read sea','Port said',car).
connection('Read sea','Sainai',car).
connection('Read sea','Luxor',train).

connection('Aswan','Cairo',train).
connection('Aswan','Alex',train).
connection('Aswan','Read sea',train).
connection('Aswan','Hurgada',train).
connection('Aswan','Matrouh',plane).
connection('Aswan','Port said',plane).
connection('Aswan','Sainai',plane).
connection('Aswan','Luxor',car).

connection('Menofia','Cairo',car).
connection('Menofia','Alex',car).

connection('Hurgada','Cairo',plane).
connection('Hurgada','Alex',plane).
connection('Hurgada','Read sea',car).
connection('Hurgada','Aswan',train).
connection('Hurgada','Port said',car).
connection('Hurgada','Sainai',car).
connection('Hurgada','Luxor',train).

connection('Matrouh','Cairo',train).
connection('Matrouh','Alex',train).
connection('Matrouh','Read sea',plane).
connection('Matrouh','Aswan',plane).
connection('Matrouh','Hurgada',plane).
connection('Matrouh','Port said',plane).
connection('Matrouh','Sainai',plane).
connection('Matrouh','Luxor',plane).

connection('Port said','Cairo',plane).
connection('Port said','Alex',plane).
connection('Port said','Read sea',car).
connection('Port said','Aswan',plane).
connection('Port said','Hurgada',car).
connection('Port said','Matrouh',plane).
connection('Port said','Sainai',car).
connection('Port said','Luxor',plane).

connection('Sainai','Cairo',plane).
connection('Sainai','Alex',plane).
connection('Sainai','Read sea',car).
connection('Sainai','Aswan',plane).
connection('Sainai','Hurgada',car).
connection('Sainai','Matrouh',plane).
connection('Sainai','Port said',car).
connection('Sainai','Luxor',plane).

connection('Luxor','Cairo',train).
connection('Luxor','Alex',plane).
connection('Luxor','Read sea',train).
connection('Luxor','Aswan',car).
connection('Luxor','Hurgada',train).
connection('Luxor','Matrouh',plane).
connection('Luxor','Port said',plane).
connection('Luxor','Sainai',plane).

% Rules for direct travel
can_travel_directly(Start, End, Transport) :-
    connection(Start, End, Transport).

% Rules for indirect travel
can_travel_indirectly(Start, End, Transports) :-
    connection(Start, Intermediate, Transport1),
    can_travel_directly(Intermediate, End, Transport2),
    Transports = [Transport1,Intermediate, Transport2].

% Predicate to check if it is possible to travel between two places (direct or indirect)
can_travel(Start, End, Transports) :-
    can_travel_directly(Start, End, Transports),
    writeln('Direct connection available!'),
    writeln(Transports).

can_travel(Start, End, Transports) :-
    can_travel_indirectly(Start, End, Transports),
    writeln('Indirect connection available!'),
    writeln( Transports).

% Predicate to check if an operation is compliant with the database
is_compliant(Operation) :-
    call(Operation), !, write('Operation is compliant.'), nl.
is_compliant(_) :-
    write('Operation is not compliant.'), nl.