% Knowledge Base
city('Cairo').
city('Alexandria').
city('Red Sea').
city('Luxor').
city('Aswan').
city('Menofia').
city('Hurghada').
city('Matrouh').
city('Port Said').
city('Sinai').

transport(car).
transport(train).
transport(plane).

% Define direct travel routes
travel('Cairo', 'Alexandria', car).
travel('Cairo', 'Red Sea', plane).
travel('Cairo', 'Luxor', train).
travel('Cairo', 'Menofia', car).
travel('Cairo', 'Hurghada', plane).
travel('Cairo', 'Matrouh', train).
travel('Cairo', 'Sinai', plane).

travel('Alexandria', 'Cairo', car).
travel('Alexandria', 'Red Sea', plane).
travel('Alexandria', 'Luxor', plane).
travel('Alexandria', 'Aswan', train).
travel('Alexandria', 'Menofia', car).
travel('Alexandria', 'Hurghada', plane).
travel('Alexandria', 'Matrouh', train).
travel('Alexandria', 'Port Said', plane).
travel('Alexandria', 'Sinai', plane).

travel('Red Sea', 'Cairo', plane).
travel('Red Sea', 'Alexandria', plane).
travel('Red Sea', 'Luxor', train).
travel('Red Sea', 'Hurghada', car).
travel('Red Sea', 'Matrouh', plane).
travel('Red Sea', 'Sinai', car).

travel('Aswan', 'Cairo', train).
travel('Aswan', 'Alexandria', train).
travel('Aswan', 'Luxor', car).
travel('Aswan', 'Matrouh', plane).
travel('Aswan', 'Port Said', plane).
travel('Aswan', 'Sinai', plane).

can_travel_directly(Start, End, Transport) :-
    travel(Start, End, Transport).

can_travel_indirectly(Start, End, Transports) :-
    travel(Start, Intermediate, Transport1),
    can_travel_directly(Intermediate, End, Transport2),
    Transports = [Transport1, Intermediate, Transport2].

can_travel(Start, End, Transports) :-
    can_travel_directly(Start, End, Transports),
    writeln('Direct connection available!'),
    writeln(Transports).

can_travel(Start, End, Transports) :-
    can_travel_indirectly(Start, End, Transports),
    writeln('Indirect connection available!'),
    writeln(Transports).

is_compliant(Operation) :-
    call(Operation), !, write('Operation is compliant.'), nl.
is_compliant(_) :-
    write('Operation is not compliant.'), nl.
