# Caligine

A rule-based, multiplayer game engine, with a simple programming interface.

# Multiplayer

<img src='./docs/client-server-diagram.png' width='500px'/>

It's a client-server architecture. When you run a script, you also spin up an application server. A caligine-lang script allows you to declare named client objects. A client connects to the server specifying their (the client's) name, and it (the client) is  assigned an avatar accoriding to the script.

Under the hood, the client and server use websockets to communicate, for speed.

The client is responsible for sending events to the server (e.g. key presses) which are processed by the server. The server then produces the updated positions of the sprites and sends them back to the client, who simply redraws them on a canvas.

# Caligine Lang

The DSL (Domain Specific Language) developed for Caligine. It's like a conventional imperative programming language, but with a built-in game loop that accepts custom, universally quantified, rules. 

Because of this built-in game loop, a Caligine program does not terminate unless it is explicitly told to (using the "exit" keyword). The exit keyword is useful when the game is over (unless you want your players to go on playing forever, as in some mobile games, e.g. the "endless runner" genre).

The rules can contain universally quantified variables ("variables" in the sense of logic programming, e.g. Prolog). A rule is declared using the "when/then" keyword pair. You can check out some example programs in the [examples](./src/examples/) folder:

- [example of a rule without variables](./src/examples/test-when-statement-no-vars.txt)
- [example of a rule with one var](./src/examples/test-when-statement-with-one-var.txt)
- [example of a "full" game](./src/examples/example3.txt)
- [example of a multiplayer game (with two clients/avatars)](./src/examples/example.txt)
- [etc...](./src/examples/)

## Grammar

The grammar (syntax) of Caligine lang is expressed in a dialect of BNF, using [Lark](https://github.com/lark-parser/lark). You can read the [grammar here](./src/grammar.lark).

# Competitors

- https://www.construct.net/en

# Future

- adding explainability for easier debugging.
- my dream: writing games in full predicate logic.
- ... or even second-order logic, but that's crazy!!!
- alas, as some of you know, game engines as a whole may become obsolete in the future due to generative AI :-(...

