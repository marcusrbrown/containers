# containers

> My collection of Dockerfiles, docker-compose files, and related scripts.

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/your-username/your-repo/Your-Workflow-Name)
![Docker Pulls](https://img.shields.io/docker/pulls/your-image-name)
![GitHub Release](https://img.shields.io/github/v/release/marcusrbrown/containers)

## Overview

This repository contains a collection of Dockerfiles for various purposes. It also includes automation tools and workflows for managing the Dockerfiles.

## Features

- Automated Dockerfile generation via `generate_dockerfiles.py`.
- GitHub Actions workflows for linting, building, and releasing Docker images.
- Devcontainer settings for a Docker-in-Docker development environment.

## Usage

### Dockerfile Generation

To generate a new Dockerfile, you can use the `generate_dockerfiles.py` script:

```bash
python generate_dockerfiles.py --base_image debian --python_version 3.9
```

### Building Docker Images

Use the following command to build a Docker image from a Dockerfile:

```bash
docker build -t your-image-name .
```

### GitHub Actions Workflows

- Dockerfile Generation Workflow: Manually triggered to generate a new Dockerfile and raise a Pull Request.
- Docker Release Workflow: Triggered on push to `main` or manually, to build and release Docker images.

## Contributing

Please read the [CONTRIBUTING.md](repo/CONTRIBUTING.md) for details on how to contribute to this repository.

## License

This project is licensed under the MIT License. See the [LICENSE.md](repo/LICENSE.md) file for details.

## Badges

[![Docker Build](https://img.shields.io/docker/cloud/build/your-docker-hub-username/your-repo-name)](https://hub.docker.com/r/your-docker-hub-username/your-repo-name/builds)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/marcusrbrown/containers/build-publish.yaml?branch=main)](https://github.com/marcusrbrown/containers/actions)
[![GitHub Release](https://img.shields.io/github/v/release/marcusrbrown/containers)](https://github.com/marcusrbrown/containers/releases)
[![License](https://img.shields.io/github/license/marcusrbrown/containers)](LICENSE.md)

## Prerequisite Software

- Python 3.x: For running Python scripts.
- Node.js: For running JavaScript-based linting tools.
- Docker: For building and testing Docker images.

## Setup Instructions

### Python Setup

1. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### package.json Setup

1. Install the required Node.js packages:

   ```bash
   npm install
   ```

## Usage Instructions

### Invoking Scripts Individually

1. Generate Dockerfiles:

   ```bash
   python scripts/generate_dockerfiles.py
   ```

2. Collect Docker Metrics:

   ```bash
   python scripts/collect_docker_metrics.py
   ```

### Using scripts CLI

You can also use the `scripts` CLI to invoke the above scripts:

```bash
python scripts/cli.py --script generate_dockerfiles
```

For more options, run:

```bash
python scripts/cli.py --help
```


---

# Changelog

All notable changes to this project will be documented here.


---

# The MIT License (MIT)

Copyright (c) 2023 Marcus R. Brown <contact@marcusrbrown.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


---

BSD 3-Clause License

Copyright (c) 2013-2024, Kim Davies and contributors.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


---

Command-line parsing library

This module is an optparse-inspired command-line parsing library that:

    - handles both optional and positional arguments
    - produces highly informative usage messages
    - supports parsers that dispatch to sub-parsers

The following is a simple usage example that sums integers from the
command-line and writes the result to a file::

    parser = argparse.ArgumentParser(
        description='sum the integers at the command line')
    parser.add_argument(
        'integers', metavar='int', nargs='+', type=int,
        help='an integer to be summed')
    parser.add_argument(
        '--log', default=sys.stdout, type=argparse.FileType('w'),
        help='the file where the sum should be written')
    args = parser.parse_args()
    args.log.write('%s' % sum(args.integers))
    args.log.close()

The module contains the following public classes:

    - ArgumentParser -- The main entry point for command-line parsing. As the
        example above shows, the add_argument() method is used to populate
        the parser with actions for optional and positional arguments. Then
        the parse_args() method is invoked to convert the args at the
        command-line into an object with attributes.

    - ArgumentError -- The exception raised by ArgumentParser objects when
        there are errors with the parser's actions. Errors raised while
        parsing the command-line are caught by ArgumentParser and emitted
        as command-line messages.

    - FileType -- A factory for defining types of files to be created. As the
        example above shows, instances of FileType are typically passed as
        the type= argument of add_argument() calls.

    - Action -- The base class for parser actions. Typically actions are
        selected by passing strings like 'store_true' or 'append_const' to
        the action= argument of add_argument(). However, for greater
        customization of ArgumentParser actions, subclasses of Action may
        be defined and passed as the action= argument.

    - HelpFormatter, RawDescriptionHelpFormatter, RawTextHelpFormatter,
        ArgumentDefaultsHelpFormatter -- Formatter classes which
        may be passed as the formatter_class= argument to the
        ArgumentParser constructor. HelpFormatter is the default,
        RawDescriptionHelpFormatter and RawTextHelpFormatter tell the parser
        not to change the formatting for help text, and
        ArgumentDefaultsHelpFormatter adds information about argument defaults
        to the help.

All other classes in this module are considered implementation details.
(Also note that HelpFormatter and RawDescriptionHelpFormatter are only
considered public as object names -- the API of the formatter objects is
still considered an implementation detail.)

Abstract base class that provides __repr__.

    The __repr__ method returns a string in the format::
        ClassName(attr=name, attr=name, ...)
    The attributes are determined either by a class-level attribute,
    '_kwarg_names', or by inspecting the instance __dict__.
    
Formatter for generating usage messages and argument help strings.

    Only the name of this class is considered a public API. All the methods
    provided by the class are considered an implementation detail.
    
Help message formatter which retains any formatting in descriptions.

    Only the name of this class is considered a public API. All the methods
    provided by the class are considered an implementation detail.
    
Help message formatter which retains formatting of all help text.

    Only the name of this class is considered a public API. All the methods
    provided by the class are considered an implementation detail.
    
Help message formatter which adds default values to argument help.

    Only the name of this class is considered a public API. All the methods
    provided by the class are considered an implementation detail.
    
An error from creating or using an argument (optional or positional).

    The string value of this exception is the message, augmented with
    information about the argument that caused it.
    
An error from trying to convert a command line string to a type.
Information about how to convert command line strings to Python objects.

    Action objects are used by an ArgumentParser to represent the information
    needed to parse a single argument from one or more strings from the
    command line. The keyword arguments to the Action constructor are also
    all attributes of Action instances.

    Keyword Arguments:

        - option_strings -- A list of command-line option strings which
            should be associated with this action.

        - dest -- The name of the attribute to hold the created object(s)

        - nargs -- The number of command-line arguments that should be
            consumed. By default, one argument will be consumed and a single
            value will be produced.  Other values include:
                - N (an integer) consumes N arguments (and produces a list)
                - '?' consumes zero or one arguments
                - '*' consumes zero or more arguments (and produces a list)
                - '+' consumes one or more arguments (and produces a list)
            Note that the difference between the default and nargs=1 is that
            with the default, a single value will be produced, while with
            nargs=1, a list containing a single value will be produced.

        - const -- The value to be produced if the option is specified and the
            option uses an action that takes no values.

        - default -- The value to be produced if the option is not specified.

        - type -- The type which the command-line arguments should be converted
            to, should be one of 'string', 'int', 'float', 'complex' or a
            callable object that accepts a single string argument. If None,
            'string' is assumed.

        - choices -- A container of values that should be allowed. If not None,
            after a command-line argument has been converted to the appropriate
            type, an exception will be raised if it is not a member of this
            collection.

        - required -- True if the action must always be specified at the
            command line. This is only meaningful for optional command-line
            arguments.

        - help -- The help string describing the argument.

        - metavar -- The name to be used for the option's argument with the
            help string. If None, the 'dest' value will be used as the name.
    
Factory for creating file object types

    Instances of FileType are typically passed as type= arguments to the
    ArgumentParser add_argument() method.

    Keyword Arguments:
        - mode -- A string indicating how the file is to be opened. Accepts the
            same values as the builtin open() function.
        - bufsize -- The file's desired buffer size. Accepts the same values as
            the builtin open() function.
    
Simple object for storing attributes.

    Implements equality by attribute names and values, and provides a simple
    string representation.
    

        add_argument(dest, ..., name=value, ...)
        add_argument(option_string, option_string, ..., name=value, ...)
        
Object for parsing command line strings into Python objects.

    Keyword Arguments:
        - prog -- The name of the program (default: sys.argv[0])
        - usage -- A usage message (default: auto-generated from arguments)
        - description -- A description of what the program does
        - epilog -- Text following the argument descriptions
        - parents -- Parsers whose arguments should be copied into this one
        - formatter_class -- HelpFormatter class for printing help messages
        - prefix_chars -- Characters that prefix optional arguments
        - fromfile_prefix_chars -- Characters that prefix files containing
            additional arguments
        - argument_default -- The default value for all arguments
        - conflict_handler -- String indicating how to handle conflicts
        - add_help -- Add a -h/-help option
    
The "version" argument to ArgumentParser is deprecated. 
Please use 
"add_argument(..., action='version', version="N", ...)" 
instead
error(message: string)

        Prints a usage message incorporating the message to stderr and
        exits.

        If you override this in a subclass, it should not return -- it
        should either exit or raise an exception.
        

---


    Base abstract class used for mess detection plugins.
    All detectors MUST extend and implement given methods.
    

        Determine if given character should be fed in.
        

        The main routine to be executed upon character.
        Insert the logic in witch the text would be considered chaotic.
        

        Permit to reset the plugin to the initial state.
        

        Compute the chaos ratio based on what your feed() has seen.
        Must NOT be lower than 0.; No restriction gt 0.
        

    Detect messy CJK text that probably means nothing.
    

    Determine if two Unicode range seen next to each other can be considered as suspicious.
    

    Compute a mess ratio given a decoded bytes sequence. The maximum threshold does stop the computation earlier.
    

---


Expose version


---


    Given a raw bytes sequence, return the best possibles charset usable to render str objects.
    If there is no results, it is a strong indicator that the source is binary/not text.
    By default, the process will extract 5 blocks of 512o each to assess the mess and coherence of a given sequence.
    And will give up a particular code page after 20% of measured mess. Those criteria are customizable at will.

    The preemptive behavior DOES NOT replace the traditional detection workflow, it prioritize a particular code page
    but never take it for granted. Can improve the performance.

    You may want to focus your attention to some code page or/and not others, use cp_isolation and cp_exclusion for that
    purpose.

    This function will strip the SIG in the payload/sequence every time except on UTF-16, UTF-32.
    By default the library does not setup any handler other than the NullHandler, if you choose to set the 'explain'
    toggle to True it will alter the logger configuration to add a StreamHandler that is suitable for debugging.
    Custom logging format and handler can be set manually.
    

    Same thing than the function from_bytes but using a file pointer that is already ready.
    Will not close the file pointer.
    

    Same thing than the function from_bytes but with one extra step. Opening and reading given file path in binary mode.
    Can raise IOError.
    

    Detect if the given input (file, bytes, or path) points to a binary file. aka. not a string.
    Based on the same main heuristic algorithms and default kwargs at the sole exception that fallbacks match
    are disabled to be stricter around ASCII-compatible but unlikely to be a string.
    

---


    chardet legacy method
    Detect the encoding of the given byte string. It should be mostly backward-compatible.
    Encoding name will match Chardet own writing whenever possible. (Not on encoding name unsupported by it)
    This function is deprecated and should be used to migrate your project easily, consult the documentation for
    further information. Not planned for removal.

    :param byte_str:     The byte sequence to examine.
    :param should_rename_legacy:  Should we rename legacy encodings
                                  to their more modern equivalents?
    

---


        Implemented to make sorted available upon CharsetMatches items.
        

        Encoding name are known by many name, using this could help when searching for IBM855 when it's listed as CP855.
        

        Return the complete list of possible languages found in decoded sequence.
        Usually not really useful. Returned list may be empty even if 'language' property return something != 'Unknown'.
        

        Most probable language found in decoded sequence. If none were detected or inferred, the property will return
        "Unknown".
        

        Original untouched bytes.
        

        The complete list of encoding that output the exact SAME str result and therefore could be the originating
        encoding.
        This list does include the encoding available in property 'encoding'.
        

        Method to get re-encoded bytes payload using given target encoding. Default to UTF-8.
        Any errors will be simply ignored by the encoder NOT replaced.
        

        Retrieve the unique SHA256 computed using the transformed (re-encoded) payload. Not the original one.
        

    Container with every CharsetMatch items ordered by default from most probable to the less one.
    Act like a list(iterable) but does not implements all related methods.
    

        Retrieve a single item either by its position or encoding name (alias may be used here).
        Raise KeyError upon invalid index or encoding not present in results.
        

        Insert a single match. Will be inserted accordingly to preserve sort.
        Can be inserted as a submatch.
        

        Simply return the first match. Strict equivalent to matches[0].
        

        Redundant method, call the method best(). Kept for BC reasons.
        

---


    Return associated unicode ranges in a single byte code page.
    

    Return inferred languages used with a unicode range.
    

    Single-byte encoding language association. Some code page are heavily linked to particular language(s).
    This function does the correspondence.
    

    Multi-byte encoding language association. Some code page are heavily linked to particular language(s).
    This function does the correspondence.
    

    Determine main aspects from a supported language if it contains accents and if is pure Latin.
    

    Return associated languages associated to given characters.
    

    Determine if a ordered characters list (by occurrence from most appearance to rarest) match a particular language.
    The result is a ratio between 0. (absolutely no correspondence) and 1. (near perfect fit).
    Beware that is function is not strict on the match in order to ease the detection. (Meaning close match is 1.)
    

    Given a decoded text sequence, return a list of str. Unicode range / alphabet separation.
    Ex. a text containing English/Latin with a bit a Hebrew will return two items in the resulting list;
    One containing the latin letters and the other hebrew.
    

    This function merge results previously given by the function coherence_ratio.
    The return type is the same as coherence_ratio.
    

    We shall NOT return "English—" in CoherenceMatches because it is an alternative
    of "English". This function only keeps the best match and remove the em-dash in it.
    

    Detect ANY language that can be identified in given sequence. The sequence will be analysed by layers.
    A layer = Character extraction by alphabets/ranges.
    

---



---


Charset-Normalizer
~~~~~~~~~~~~~~
The Real First Universal Charset Detector.
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, This package is trying to resolve the issue by taking a new approach.
All IANA character set names for which the Python core library provides codecs are supported.

Basic usage:
   >>> from charset_normalizer import from_bytes
   >>> results = from_bytes('Bсеки човек има право на образование. Oбразованието!'.encode('utf_8'))
   >>> best_guess = results.best()
   >>> str(best_guess)
   'Bсеки човек има право на образование. Oбразованието!'

Others methods and usages are available - see the full documentation
at <https://github.com/Ousret/charset_normalizer>.
:copyright: (c) 2021 by Ahmed TAHRI
:license: MIT, see LICENSE for more details.


---



---


    Retrieve the Unicode range official name from a single character.
    

    Extract using ASCII-only decoder any specified encoding in the first n-bytes.
    

    Verify is a specific encoding is a multi byte one based on it IANA name
    

    Identify and extract SIG/BOM in given sequence.
    
Returns the Python normalized encoding name (Not the IANA official name).

    Determine if two code page are at least 80% similar. IANA_SUPPORTED_SIMILAR dict was generated using
    the function cp_similarity.
    

---



---

Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".

    Credit goes to (c) https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
    
Factory for creating file object types

    Instances of FileType are typically passed as type= arguments to the
    ArgumentParser add_argument() method.

    Keyword Arguments:
        - mode -- A string indicating how the file is to be opened. Accepts the
            same values as the builtin open() function.
        - bufsize -- The file's desired buffer size. Accepts the same values as
            the builtin open() function.
        - encoding -- The file's encoding. Accepts the same values as the
            builtin open() function.
        - errors -- A string indicating how encoding and decoding errors are to
            be handled. Accepts the same value as the builtin open() function.

    Backported from CPython 3.12
    

    CLI assistant using ARGV and ArgumentParser
    :param argv:
    :return: 0 if everything is fine, anything else equal trouble
    

---



---



---

Initialize the scanner.

---



---



---



---

Block special attributes/methods from being set in a newly created
        object, to prevent user-controlled methods from being called during
        deserialization

---



---



---



---



---



---


    Scan a YAML stream and produce scanning tokens.
    

    Parse a YAML stream and produce parsing events.
    

    Parse the first YAML document in a stream
    and produce the corresponding representation tree.
    

    Parse all YAML documents in a stream
    and produce corresponding representation trees.
    

    Parse the first YAML document in a stream
    and produce the corresponding Python object.
    

    Parse all YAML documents in a stream
    and produce corresponding Python objects.
    

    Parse the first YAML document in a stream
    and produce the corresponding Python object.

    Resolve all tags except those known to be
    unsafe on untrusted input.
    

    Parse all YAML documents in a stream
    and produce corresponding Python objects.

    Resolve all tags except those known to be
    unsafe on untrusted input.
    

    Parse the first YAML document in a stream
    and produce the corresponding Python object.

    Resolve only basic YAML tags. This is known
    to be safe for untrusted input.
    

    Parse all YAML documents in a stream
    and produce corresponding Python objects.

    Resolve only basic YAML tags. This is known
    to be safe for untrusted input.
    

    Parse the first YAML document in a stream
    and produce the corresponding Python object.

    Resolve all tags, even those known to be
    unsafe on untrusted input.
    

    Parse all YAML documents in a stream
    and produce corresponding Python objects.

    Resolve all tags, even those known to be
    unsafe on untrusted input.
    

    Emit YAML parsing events into a stream.
    If stream is None, return the produced string instead.
    

    Serialize a sequence of representation trees into a YAML stream.
    If stream is None, return the produced string instead.
    

    Serialize a representation tree into a YAML stream.
    If stream is None, return the produced string instead.
    

    Serialize a sequence of Python objects into a YAML stream.
    If stream is None, return the produced string instead.
    

    Serialize a Python object into a YAML stream.
    If stream is None, return the produced string instead.
    

    Serialize a sequence of Python objects into a YAML stream.
    Produce only basic YAML tags.
    If stream is None, return the produced string instead.
    

    Serialize a Python object into a YAML stream.
    Produce only basic YAML tags.
    If stream is None, return the produced string instead.
    

    Add an implicit scalar detector.
    If an implicit scalar value matches the given regexp,
    the corresponding tag is assigned to the scalar.
    first is a sequence of possible initial characters or None.
    

    Add a path based resolver for the given tag.
    A path is a list of keys that forms a path
    to a node in the representation tree.
    Keys can be string values, integers, or None.
    

    Add a constructor for the given tag.
    Constructor is a function that accepts a Loader instance
    and a node object and produces the corresponding Python object.
    

    Add a multi-constructor for the given tag prefix.
    Multi-constructor is called for a node if its tag starts with tag_prefix.
    Multi-constructor accepts a Loader instance, a tag suffix,
    and a node object and produces the corresponding Python object.
    

    Add a representer for the given type.
    Representer is a function accepting a Dumper instance
    and an instance of the given data type
    and producing the corresponding representation node.
    

    Add a representer for the given type.
    Multi-representer is a function accepting a Dumper instance
    and an instance of the given data type or subtype
    and producing the corresponding representation node.
    

    The metaclass for YAMLObject.
    

    An object that can dump itself to a YAML stream
    and load itself from a YAML stream.
    

        Convert a representation node to a Python object.
        

        Convert a Python object to a representation node.
        

---



---



---



---



---



---

Execute exactly this copy of pip, within a different environment.

This file is named as it is, to ensure that this module can't be imported via
an import statement.


---

This is an internal API only meant for use by pip's own console scripts.

    For additional details, see https://github.com/pypa/pip/issues/7498.
    

---



---


pip._vendor is for vendoring dependencies of pip to prevent needing pip to
depend on something external.

Files inside of pip._vendor should be considered immutable and should only be
updated to versions from upstream.


---

Special type indicating an unconstrained type.
        - Any is compatible with every type.
        - Any assumed to have all methods.
        - All values assumed to be instances of Any.
        Note that all the above statements are true from the point of view of
        static type checkers. At runtime, Any should not be used with instance
        checks.
        
This decorator can be used to indicate to type checkers that
        the decorated method cannot be overridden, and decorated class
        cannot be subclassed. For example:

            class Base:
                @final
                def done(self) -> None:
                    ...
            class Sub(Base):
                def done(self) -> None:  # Error reported by type checker
                    ...
            @final
            class Leaf:
                ...
            class Other(Leaf):  # Error reported by type checker
                ...

        There is no runtime checking of these properties. The decorator
        sets the ``__final__`` attribute to ``True`` on the decorated object
        to allow runtime introspection.
        
An internal helper for Literal creation: flatten Literals among parameters
\
                           A type that can be used to indicate to type checkers
                           that the corresponding value has a value literally equivalent
                           to the provided parameter. For example:

                               var: Literal[4] = 4

                           The type checker understands that 'var' is literally equal to
                           the value 4 and no other value.

                           Literal[...] cannot be subclassed. There is no runtime
                           checking verifying that the parameter is actually a value
                           instead of a type.
Decorator for overloaded functions/methods.

        In a stub file, place two or more stub definitions for the same
        function in a row, each decorated with @overload.  For example:

        @overload
        def utf8(value: None) -> None: ...
        @overload
        def utf8(value: bytes) -> bytes: ...
        @overload
        def utf8(value: str) -> bytes: ...

        In a non-stub file (i.e. a regular .py file), do the same but
        follow it with an implementation.  The implementation should *not*
        be decorated with @overload.  For example:

        @overload
        def utf8(value: None) -> None: ...
        @overload
        def utf8(value: bytes) -> bytes: ...
        @overload
        def utf8(value: str) -> bytes: ...
        def utf8(value):
            # implementation goes here

        The overloads for a function can be retrieved at runtime using the
        get_overloads() function.
        
Return all defined overloads for *func* as a sequence.
Clear all overloads in the registry.
Allow instance and class checks for special stdlib modules.
        The abc and functools modules indiscriminately call isinstance() and
        issubclass() on the whole MRO of a user class, which may contain protocols.
        
Raise TypeError if `arg` is not an instance of `type`
        in `issubclass(arg, <protocol>)`.

        In most cases, this is verified by type.__subclasscheck__.
        Checking it again unnecessarily would slow down issubclass() checks,
        so, we don't perform this check unless we absolutely have to.

        For various error paths, however,
        we want to ensure that *this* error message is shown to the user
        where relevant, rather than a typing.py-specific error message.
        
Mark a protocol class as a runtime protocol.

        Such protocol can be used with isinstance() and issubclass().
        Raise TypeError if applied to a non-protocol class.
        This allows a simple-minded structural check very similar to
        one trick ponies in collections.abc such as Iterable.

        For example::

            @runtime_checkable
            class Closable(Protocol):
                def close(self): ...

            assert isinstance(open('/some/file'), Closable)

        Warning: this will check only the presence of the required methods,
        not their type signatures!
        
An ABC with one abstract method __int__.
An ABC with one abstract method __float__.
An ABC with one abstract method __complex__.
An ABC with one abstract method __bytes__.

        An ABC with one abstract method __abs__ that is covariant in its return type.
        

        An ABC with one abstract method __round__ that is covariant in its return type.
        
The type of the NoDefault singleton.
The type of the NoExtraItems singleton.
Create new typed dict class object.

            This method is called when TypedDict is subclassed,
            or when TypedDict is instantiated. This way
            TypedDict supports all three syntax forms described in its docstring.
            Subclasses and instances of TypedDict return actual dictionaries.
            
A simple typed namespace. At runtime it is equivalent to a plain dict.

        TypedDict creates a dictionary type such that a type checker will expect all
        instances to have a certain set of keys, where each key is
        associated with a value of a consistent type. This expectation
        is not checked at runtime.

        Usage::

            class Point2D(TypedDict):
                x: int
                y: int
                label: str

            a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
            b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check

            assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')

        The type info can be accessed via the Point2D.__annotations__ dict, and
        the Point2D.__required_keys__ and Point2D.__optional_keys__ frozensets.
        TypedDict supports an additional equivalent form::

            Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})

        By default, all keys must be present in a TypedDict. It is possible
        to override this by specifying totality::

            class Point2D(TypedDict, total=False):
                x: int
                y: int

        This means that a Point2D TypedDict can have any of the keys omitted. A type
        checker is only expected to support a literal False or True as the value of
        the total argument. True is the default, and makes all items defined in the
        class body be required.

        The Required and NotRequired special forms can also be used to mark
        individual keys as being required or not required::

            class Point2D(TypedDict):
                x: int  # the "x" key must always be present (Required is the default)
                y: NotRequired[int]  # the "y" key can be omitted

        See PEP 655 for more details on Required and NotRequired.
        
Check if an annotation is a TypedDict class

        For example::
            class Film(TypedDict):
                title: str
                year: int

            is_typeddict(Film)  # => True
            is_typeddict(Union[list, str])  # => False
        
Assert (to the type checker) that the value is of the given type.

        When the type checker encounters a call to assert_type(), it
        emits an error if the value is not of the specified type::

            def greet(name: str) -> None:
                assert_type(name, str)  # ok
                assert_type(name, int)  # type checker error

        At runtime this returns the first argument unchanged and otherwise
        does nothing.
        
Strips Annotated, Required and NotRequired from a given type.
Return type hints for an object.

        This is often the same as obj.__annotations__, but it handles
        forward references encoded as string literals, adds Optional[t] if a
        default value equal to None is set and recursively replaces all
        'Annotated[T, ...]', 'Required[T]' or 'NotRequired[T]' with 'T'
        (unless 'include_extras=True').

        The argument may be a module, class, method, or function. The annotations
        are returned as a dictionary. For classes, annotations include also
        inherited members.

        TypeError is raised if the argument is not of a type that can contain
        annotations, and an empty dictionary is returned if no annotations are
        present.

        BEWARE -- the behavior of globalns and localns is counterintuitive
        (unless you are familiar with how eval() and exec() work).  The
        search order is locals first, then globals.

        - If no dict arguments are passed, an attempt is made to use the
          globals from obj (or the respective module's globals for classes),
          and these are also used as the locals.  If the object does not appear
          to have globals, an empty dictionary is used.

        - If one dict argument is passed, it is used for both globals and
          locals.

        - If two dict arguments are passed, they specify globals and
          locals, respectively.
        
detects Union[..., None] pattern
Runtime representation of an annotated type.

        At its core 'Annotated[t, dec1, dec2, ...]' is an alias for the type 't'
        with extra annotations. The alias behaves like a normal typing alias,
        instantiating is the same as instantiating the underlying type, binding
        it to types is also the same.
        
Add context specific metadata to a type.

        Example: Annotated[int, runtime_check.Unsigned] indicates to the
        hypothetical runtime_check module that this type is an unsigned int.
        Every other consumer of this type can ignore this metadata and treat
        this type as int.

        The first argument to Annotated must be a valid type (and will be in
        the __origin__ field), the remaining arguments are kept as a tuple in
        the __extra__ field.

        Details:

        - It's an error to call `Annotated` with less than two arguments.
        - Nested Annotated are flattened::

            Annotated[Annotated[T, Ann1, Ann2], Ann3] == Annotated[T, Ann1, Ann2, Ann3]

        - Instantiating an annotated type is equivalent to instantiating the
        underlying type::

            Annotated[C, Ann1](5) == C(5)

        - Annotated can be used as a generic type alias::

            Optimized = Annotated[T, runtime.Optimize()]
            Optimized[int] == Annotated[int, runtime.Optimize()]

            OptimizedList = Annotated[List[T], runtime.Optimize()]
            OptimizedList[int] == Annotated[List[int], runtime.Optimize()]
        
Get the unsubscripted version of a type.

        This supports generic types, Callable, Tuple, Union, Literal, Final, ClassVar
        and Annotated. Return None for unsupported types. Examples::

            get_origin(Literal[42]) is Literal
            get_origin(int) is None
            get_origin(ClassVar[int]) is ClassVar
            get_origin(Generic) is Generic
            get_origin(Generic[T]) is Generic
            get_origin(Union[T, int]) is Union
            get_origin(List[Tuple[T, T]][int]) == list
            get_origin(P.args) is P
        
Get type arguments with all substitutions performed.

        For unions, basic simplifications used by Union constructor are performed.
        Examples::
            get_args(Dict[str, int]) == (str, int)
            get_args(int) == ()
            get_args(Union[int, Union[T, int], str][int]) == (int, str)
            get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
            get_args(Callable[[], T][int]) == ([], int)
        
Special marker indicating that an assignment should
        be recognized as a proper type alias definition by type
        checkers.

        For example::

            Predicate: TypeAlias = Callable[..., bool]

        It's invalid when used anywhere except as in the example above.
        
Special marker indicating that an assignment should
        be recognized as a proper type alias definition by type
        checkers.

        For example::

            Predicate: TypeAlias = Callable[..., bool]

        It's invalid when used anywhere except as in the example
        above.
Mixin for TypeVarLike defaults.
Type variable.
Mixin to indicate that object should not be copied.
The args for a ParamSpec object.

        Given a ParamSpec object P, P.args is an instance of ParamSpecArgs.

        ParamSpecArgs objects have a reference back to their ParamSpec:

        P.args.__origin__ is P

        This type is meant for runtime introspection and has no special meaning to
        static type checkers.
        
The kwargs for a ParamSpec object.

        Given a ParamSpec object P, P.kwargs is an instance of ParamSpecKwargs.

        ParamSpecKwargs objects have a reference back to their ParamSpec:

        P.kwargs.__origin__ is P

        This type is meant for runtime introspection and has no special meaning to
        static type checkers.
        
Parameter specification.
Parameter specification variable.

        Usage::

           P = ParamSpec('P')

        Parameter specification variables exist primarily for the benefit of static
        type checkers.  They are used to forward the parameter types of one
        callable to another callable, a pattern commonly found in higher order
        functions and decorators.  They are only valid when used in ``Concatenate``,
        or s the first argument to ``Callable``. In Python 3.10 and higher,
        they are also supported in user-defined Generics at runtime.
        See class Generic for more information on generic types.  An
        example for annotating a decorator::

           T = TypeVar('T')
           P = ParamSpec('P')

           def add_logging(f: Callable[P, T]) -> Callable[P, T]:
               '''A type-safe decorator to add logging to a function.'''
               def inner(*args: P.args, **kwargs: P.kwargs) -> T:
                   logging.info(f'{f.__name__} was called')
                   return f(*args, **kwargs)
               return inner

           @add_logging
           def add_two(x: float, y: float) -> float:
               '''Add two numbers together.'''
               return x + y

        Parameter specification variables defined with covariant=True or
        contravariant=True can be used to declare covariant or contravariant
        generic types.  These keyword arguments are valid, but their actual semantics
        are yet to be decided.  See PEP 612 for details.

        Parameter specification variables can be introspected. e.g.:

           P.__name__ == 'T'
           P.__bound__ == None
           P.__covariant__ == False
           P.__contravariant__ == False

        Note that only parameter specification variables defined in global scope can
        be pickled.
        
For converting None to type(None), and strings to ForwardRef.
Used in conjunction with ``ParamSpec`` and ``Callable`` to represent a
        higher order function which adds, removes or transforms parameters of a
        callable.

        For example::

           Callable[Concatenate[int, P], int]

        See PEP 612 for detailed information.
        
Used in conjunction with ``ParamSpec`` and ``Callable`` to represent a
        higher order function which adds, removes or transforms parameters of a
        callable.

        For example::

           Callable[Concatenate[int, P], int]

        See PEP 612 for detailed information.
        
Special typing form used to annotate the return type of a user-defined
        type guard function.  ``TypeGuard`` only accepts a single type argument.
        At runtime, functions marked this way should return a boolean.

        ``TypeGuard`` aims to benefit *type narrowing* -- a technique used by static
        type checkers to determine a more precise type of an expression within a
        program's code flow.  Usually type narrowing is done by analyzing
        conditional code flow and applying the narrowing to a block of code.  The
        conditional expression here is sometimes referred to as a "type guard".

        Sometimes it would be convenient to use a user-defined boolean function
        as a type guard.  Such a function should use ``TypeGuard[...]`` as its
        return type to alert static type checkers to this intention.

        Using  ``-> TypeGuard`` tells the static type checker that for a given
        function:

        1. The return value is a boolean.
        2. If the return value is ``True``, the type of its argument
        is the type inside ``TypeGuard``.

        For example::

            def is_str(val: Union[str, float]):
                # "isinstance" type guard
                if isinstance(val, str):
                    # Type of ``val`` is narrowed to ``str``
                    ...
                else:
                    # Else, type of ``val`` is narrowed to ``float``.
                    ...

        Strict type narrowing is not enforced -- ``TypeB`` need not be a narrower
        form of ``TypeA`` (it can even be a wider form) and this may lead to
        type-unsafe results.  The main reason is to allow for things like
        narrowing ``List[object]`` to ``List[str]`` even though the latter is not
        a subtype of the former, since ``List`` is invariant.  The responsibility of
        writing type-safe type guards is left to the user.

        ``TypeGuard`` also works with type variables.  For more information, see
        PEP 647 (User-Defined Type Guards).
        
Special typing form used to annotate the return type of a user-defined
        type guard function.  ``TypeGuard`` only accepts a single type argument.
        At runtime, functions marked this way should return a boolean.

        ``TypeGuard`` aims to benefit *type narrowing* -- a technique used by static
        type checkers to determine a more precise type of an expression within a
        program's code flow.  Usually type narrowing is done by analyzing
        conditional code flow and applying the narrowing to a block of code.  The
        conditional expression here is sometimes referred to as a "type guard".

        Sometimes it would be convenient to use a user-defined boolean function
        as a type guard.  Such a function should use ``TypeGuard[...]`` as its
        return type to alert static type checkers to this intention.

        Using  ``-> TypeGuard`` tells the static type checker that for a given
        function:

        1. The return value is a boolean.
        2. If the return value is ``True``, the type of its argument
        is the type inside ``TypeGuard``.

        For example::

            def is_str(val: Union[str, float]):
                # "isinstance" type guard
                if isinstance(val, str):
                    # Type of ``val`` is narrowed to ``str``
                    ...
                else:
                    # Else, type of ``val`` is narrowed to ``float``.
                    ...

        Strict type narrowing is not enforced -- ``TypeB`` need not be a narrower
        form of ``TypeA`` (it can even be a wider form) and this may lead to
        type-unsafe results.  The main reason is to allow for things like
        narrowing ``List[object]`` to ``List[str]`` even though the latter is not
        a subtype of the former, since ``List`` is invariant.  The responsibility of
        writing type-safe type guards is left to the user.

        ``TypeGuard`` also works with type variables.  For more information, see
        PEP 647 (User-Defined Type Guards).
        
Special typing form used to annotate the return type of a user-defined
        type narrower function.  ``TypeIs`` only accepts a single type argument.
        At runtime, functions marked this way should return a boolean.

        ``TypeIs`` aims to benefit *type narrowing* -- a technique used by static
        type checkers to determine a more precise type of an expression within a
        program's code flow.  Usually type narrowing is done by analyzing
        conditional code flow and applying the narrowing to a block of code.  The
        conditional expression here is sometimes referred to as a "type guard".

        Sometimes it would be convenient to use a user-defined boolean function
        as a type guard.  Such a function should use ``TypeIs[...]`` as its
        return type to alert static type checkers to this intention.

        Using  ``-> TypeIs`` tells the static type checker that for a given
        function:

        1. The return value is a boolean.
        2. If the return value is ``True``, the type of its argument
        is the intersection of the type inside ``TypeIs`` and the argument's
        previously known type.

        For example::

            def is_awaitable(val: object) -> TypeIs[Awaitable[Any]]:
                return hasattr(val, '__await__')

            def f(val: Union[int, Awaitable[int]]) -> int:
                if is_awaitable(val):
                    assert_type(val, Awaitable[int])
                else:
                    assert_type(val, int)

        ``TypeIs`` also works with type variables.  For more information, see
        PEP 742 (Narrowing types with TypeIs).
        
Special typing form used to annotate the return type of a user-defined
        type narrower function.  ``TypeIs`` only accepts a single type argument.
        At runtime, functions marked this way should return a boolean.

        ``TypeIs`` aims to benefit *type narrowing* -- a technique used by static
        type checkers to determine a more precise type of an expression within a
        program's code flow.  Usually type narrowing is done by analyzing
        conditional code flow and applying the narrowing to a block of code.  The
        conditional expression here is sometimes referred to as a "type guard".

        Sometimes it would be convenient to use a user-defined boolean function
        as a type guard.  Such a function should use ``TypeIs[...]`` as its
        return type to alert static type checkers to this intention.

        Using  ``-> TypeIs`` tells the static type checker that for a given
        function:

        1. The return value is a boolean.
        2. If the return value is ``True``, the type of its argument
        is the intersection of the type inside ``TypeIs`` and the argument's
        previously known type.

        For example::

            def is_awaitable(val: object) -> TypeIs[Awaitable[Any]]:
                return hasattr(val, '__await__')

            def f(val: Union[int, Awaitable[int]]) -> int:
                if is_awaitable(val):
                    assert_type(val, Awaitable[int])
                else:
                    assert_type(val, int)

        ``TypeIs`` also works with type variables.  For more information, see
        PEP 742 (Narrowing types with TypeIs).
        
A special form representing the value that results from the evaluation
        of a type expression. This value encodes the information supplied in the
        type expression, and it represents the type described by that type expression.

        When used in a type expression, TypeForm describes a set of type form objects.
        It accepts a single type argument, which must be a valid type expression.
        ``TypeForm[T]`` describes the set of all type form objects that represent
        the type T or types that are assignable to T.

        Usage:

            def cast[T](typ: TypeForm[T], value: Any) -> T: ...

            reveal_type(cast(int, "x"))  # int

        See PEP 747 for more information.
        
A special form representing the value that results from the evaluation
        of a type expression. This value encodes the information supplied in the
        type expression, and it represents the type described by that type expression.

        When used in a type expression, TypeForm describes a set of type form objects.
        It accepts a single type argument, which must be a valid type expression.
        ``TypeForm[T]`` describes the set of all type form objects that represent
        the type T or types that are assignable to T.

        Usage:

            def cast[T](typ: TypeForm[T], value: Any) -> T: ...

            reveal_type(cast(int, "x"))  # int

        See PEP 747 for more information.
        
Represents an arbitrary literal string.

        Example::

          from pip._vendor.typing_extensions import LiteralString

          def query(sql: LiteralString) -> ...:
              ...

          query("SELECT * FROM table")  # ok
          query(f"SELECT * FROM {input()}")  # not ok

        See PEP 675 for details.

        
Used to spell the type of "self" in classes.

        Example::

          from typing import Self

          class ReturnsSelf:
              def parse(self, data: bytes) -> Self:
                  ...
                  return self

        
The bottom type, a type that has no members.

        This can be used to define a function that should never be
        called, or a function that never returns::

            from pip._vendor.typing_extensions import Never

            def never_call_me(arg: Never) -> None:
                pass

            def int_or_str(arg: int | str) -> None:
                never_call_me(arg)  # type checker error
                match arg:
                    case int():
                        print("It's an int")
                    case str():
                        print("It's a str")
                    case _:
                        never_call_me(arg)  # ok, arg is of type Never

        
A special typing construct to mark a key of a total=False TypedDict
        as required. For example:

            class Movie(TypedDict, total=False):
                title: Required[str]
                year: int

            m = Movie(
                title='The Matrix',  # typechecker error if key is omitted
                year=1999,
            )

        There is no runtime checking that a required key is actually provided
        when instantiating a related TypedDict.
        
A special typing construct to mark a key of a TypedDict as
        potentially missing. For example:

            class Movie(TypedDict):
                title: str
                year: NotRequired[int]

            m = Movie(
                title='The Matrix',  # typechecker error if key is omitted
                year=1999,
            )
        
A special typing construct to mark a key of a total=False TypedDict
        as required. For example:

            class Movie(TypedDict, total=False):
                title: Required[str]
                year: int

            m = Movie(
                title='The Matrix',  # typechecker error if key is omitted
                year=1999,
            )

        There is no runtime checking that a required key is actually provided
        when instantiating a related TypedDict.
        
A special typing construct to mark a key of a TypedDict as
        potentially missing. For example:

            class Movie(TypedDict):
                title: str
                year: NotRequired[int]

            m = Movie(
                title='The Matrix',  # typechecker error if key is omitted
                year=1999,
            )
        
A special typing construct to mark an item of a TypedDict as read-only.

        For example:

            class Movie(TypedDict):
                title: ReadOnly[str]
                year: int

            def mutate_movie(m: Movie) -> None:
                m["year"] = 1992  # allowed
                m["title"] = "The Matrix"  # typechecker error

        There is no runtime checking for this property.
        
A special typing construct to mark a key of a TypedDict as read-only.

        For example:

            class Movie(TypedDict):
                title: ReadOnly[str]
                year: int

            def mutate_movie(m: Movie) -> None:
                m["year"] = 1992  # allowed
                m["title"] = "The Matrix"  # typechecker error

        There is no runtime checking for this propery.
        
\
Type unpack operator.

The type unpack operator takes the child types from some container type,
such as `tuple[int, str]` or a `TypeVarTuple`, and 'pulls them out'. For
example:

  # For some generic class `Foo`:
  Foo[Unpack[tuple[int, str]]]  # Equivalent to Foo[int, str]

  Ts = TypeVarTuple('Ts')
  # Specifies that `Bar` is generic in an arbitrary number of types.
  # (Think of `Ts` as a tuple of an arbitrary number of individual
  #  `TypeVar`s, which the `Unpack` is 'pulling out' directly into the
  #  `Generic[]`.)
  class Bar(Generic[Unpack[Ts]]): ...
  Bar[int]  # Valid
  Bar[int, str]  # Also valid

From Python 3.11, this can also be done using the `*` operator:

    Foo[*tuple[int, str]]
    class Bar(Generic[*Ts]): ...

The operator can also be used along with a `TypedDict` to annotate
`**kwargs` in a function signature. For instance:

  class Movie(TypedDict):
    name: str
    year: int

  # This function expects two keyword arguments - *name* of type `str` and
  # *year* of type `int`.
  def foo(**kwargs: Unpack[Movie]): ...

Note that there is only some runtime checking of this operator. Not
everything the runtime allows may be accepted by static type checkers.

For more information, see PEP 646 and PEP 692.

Type variable tuple.
Type variable tuple.

        Usage::

            Ts = TypeVarTuple('Ts')

        In the same way that a normal type variable is a stand-in for a single
        type such as ``int``, a type variable *tuple* is a stand-in for a *tuple*
        type such as ``Tuple[int, str]``.

        Type variable tuples can be used in ``Generic`` declarations.
        Consider the following example::

            class Array(Generic[*Ts]): ...

        The ``Ts`` type variable tuple here behaves like ``tuple[T1, T2]``,
        where ``T1`` and ``T2`` are type variables. To use these type variables
        as type parameters of ``Array``, we must *unpack* the type variable tuple using
        the star operator: ``*Ts``. The signature of ``Array`` then behaves
        as if we had simply written ``class Array(Generic[T1, T2]): ...``.
        In contrast to ``Generic[T1, T2]``, however, ``Generic[*Shape]`` allows
        us to parameterise the class with an *arbitrary* number of type parameters.

        Type variable tuples can be used anywhere a normal ``TypeVar`` can.
        This includes class definitions, as shown above, as well as function
        signatures and variable annotations::

            class Array(Generic[*Ts]):

                def __init__(self, shape: Tuple[*Ts]):
                    self._shape: Tuple[*Ts] = shape

                def get_shape(self) -> Tuple[*Ts]:
                    return self._shape

            shape = (Height(480), Width(640))
            x: Array[Height, Width] = Array(shape)
            y = abs(x)  # Inferred type is Array[Height, Width]
            z = x + x   #        ...    is Array[Height, Width]
            x.get_shape()  #     ...    is tuple[Height, Width]

        
Reveal the inferred type of a variable.

        When a static type checker encounters a call to ``reveal_type()``,
        it will emit the inferred type of the argument::

            x: int = 1
            reveal_type(x)

        Running a static type checker (e.g., ``mypy``) on this example
        will produce output similar to 'Revealed type is "builtins.int"'.

        At runtime, the function prints the runtime type of the
        argument and returns it unchanged.

        
Assert to the type checker that a line of code is unreachable.

        Example::

            def int_or_str(arg: int | str) -> None:
                match arg:
                    case int():
                        print("It's an int")
                    case str():
                        print("It's a str")
                    case _:
                        assert_never(arg)

        If a type checker finds that a call to assert_never() is
        reachable, it will emit an error.

        At runtime, this throws an exception when called.

        
Decorator that marks a function, class, or metaclass as providing
        dataclass-like behavior.

        Example:

            from pip._vendor.typing_extensions import dataclass_transform

            _T = TypeVar("_T")

            # Used on a decorator function
            @dataclass_transform()
            def create_model(cls: type[_T]) -> type[_T]:
                ...
                return cls

            @create_model
            class CustomerModel:
                id: int
                name: str

            # Used on a base class
            @dataclass_transform()
            class ModelBase: ...

            class CustomerModel(ModelBase):
                id: int
                name: str

            # Used on a metaclass
            @dataclass_transform()
            class ModelMeta(type): ...

            class ModelBase(metaclass=ModelMeta): ...

            class CustomerModel(ModelBase):
                id: int
                name: str

        Each of the ``CustomerModel`` classes defined in this example will now
        behave similarly to a dataclass created with the ``@dataclasses.dataclass``
        decorator. For example, the type checker will synthesize an ``__init__``
        method.

        The arguments to this decorator can be used to customize this behavior:
        - ``eq_default`` indicates whether the ``eq`` parameter is assumed to be
          True or False if it is omitted by the caller.
        - ``order_default`` indicates whether the ``order`` parameter is
          assumed to be True or False if it is omitted by the caller.
        - ``kw_only_default`` indicates whether the ``kw_only`` parameter is
          assumed to be True or False if it is omitted by the caller.
        - ``frozen_default`` indicates whether the ``frozen`` parameter is
          assumed to be True or False if it is omitted by the caller.
        - ``field_specifiers`` specifies a static list of supported classes
          or functions that describe fields, similar to ``dataclasses.field()``.

        At runtime, this decorator records its arguments in the
        ``__dataclass_transform__`` attribute on the decorated object.

        See PEP 681 for details.

        
Indicate that a method is intended to override a method in a base class.

        Usage:

            class Base:
                def method(self) -> None:
                    pass

            class Child(Base):
                @override
                def method(self) -> None:
                    super().method()

        When this decorator is applied to a method, the type checker will
        validate that it overrides a method with the same name on a base class.
        This helps prevent bugs that may occur when a base class is changed
        without an equivalent change to a child class.

        There is no runtime checking of these properties. The decorator
        sets the ``__override__`` attribute to ``True`` on the decorated object
        to allow runtime introspection.

        See PEP 698 for details.

        
Indicate that a class, function or overload is deprecated.

        When this decorator is applied to an object, the type checker
        will generate a diagnostic on usage of the deprecated object.

        Usage:

            @deprecated("Use B instead")
            class A:
                pass

            @deprecated("Use g instead")
            def f():
                pass

            @overload
            @deprecated("int support is deprecated")
            def g(x: int) -> int: ...
            @overload
            def g(x: str) -> int: ...

        The warning specified by *category* will be emitted at runtime
        on use of deprecated objects. For functions, that happens on calls;
        for classes, on instantiation and on creation of subclasses.
        If the *category* is ``None``, no warning is emitted at runtime.
        The *stacklevel* determines where the
        warning is emitted. If it is ``1`` (the default), the warning
        is emitted at the direct caller of the deprecated object; if it
        is higher, it is emitted further up the stack.
        Static type checker behavior is not affected by the *category*
        and *stacklevel* arguments.

        The deprecation message passed to the decorator is saved in the
        ``__deprecated__`` attribute on the decorated object.
        If applied to an overload, the decorator
        must be after the ``@overload`` decorator for the attribute to
        exist on the overload as returned by ``get_overloads()``.

        See PEP 702 for details.

        
Check correct count for parameters of a generic cls (internal helper).

        This gives a nice error message in case of count mismatch.
        
Check correct count for parameters of a generic cls (internal helper).

        This gives a nice error message in case of count mismatch.
        
Collect all type variable contained in types in order of
        first appearance (lexicographic order). For example::

            _collect_type_vars((T, List[S, T])) == (T, S)
        
Collect all type variables and parameter specifications in args
        in order of first appearance (lexicographic order).

        For example::

            assert _collect_parameters((T, Callable[P, T])) == (T, P)
        
Typed version of namedtuple.

        Usage::

            class Employee(NamedTuple):
                name: str
                id: int

        This is equivalent to::

            Employee = collections.namedtuple('Employee', ['name', 'id'])

        The resulting class has an extra __annotations__ attribute, giving a
        dict that maps field names to types.  (The field names are also in
        the _fields attribute, which is part of the namedtuple API.)
        An alternative equivalent functional syntax is also accepted::

            Employee = NamedTuple('Employee', [('name', str), ('id', int)])
        
Base class for classes that implement the buffer protocol.

        The buffer protocol allows Python objects to expose a low-level
        memory buffer interface. Before Python 3.12, it is not possible
        to implement the buffer protocol in pure Python code, or even
        to check whether a class implements the buffer protocol. In
        Python 3.12 and higher, the ``__buffer__`` method allows access
        to the buffer protocol from Python code, and the
        ``collections.abc.Buffer`` ABC allows checking whether a class
        implements the buffer protocol.

        To indicate support for the buffer protocol in earlier versions,
        inherit from this ABC, either in a stub file or at runtime,
        or use ABC registration. This ABC provides no methods, because
        there is no Python-accessible methods shared by pre-3.12 buffer
        classes. It is useful primarily for static checks.

        
Return the class's "original" bases prior to modification by `__mro_entries__`.

        Examples::

            from typing import TypeVar, Generic
            from pip._vendor.typing_extensions import NamedTuple, TypedDict

            T = TypeVar("T")
            class Foo(Generic[T]): ...
            class Bar(Foo[int], float): ...
            class Baz(list[str]): ...
            Eggs = NamedTuple("Eggs", [("a", int), ("b", str)])
            Spam = TypedDict("Spam", {"a": int, "b": str})

            assert get_original_bases(Bar) == (Foo[int], float)
            assert get_original_bases(Baz) == (list[str],)
            assert get_original_bases(Eggs) == (NamedTuple,)
            assert get_original_bases(Spam) == (TypedDict,)
            assert get_original_bases(int) == (object,)
        
NewType creates simple unique types with almost zero
        runtime overhead. NewType(name, tp) is considered a subtype of tp
        by static type checkers. At runtime, NewType(name, tp) returns
        a dummy callable that simply returns its argument. Usage::
            UserId = NewType('UserId', int)
            def name_by_id(user_id: UserId) -> str:
                ...
            UserId('user')          # Fails type check
            name_by_id(42)          # Fails type check
            name_by_id(UserId(42))  # OK
            num = UserId(5) + 1     # type: int
        
Corresponds to is_unionable() in unionobject.c in CPython.
Corresponds to is_unionable() in unionobject.c in CPython.
Create named, parameterized type aliases.

        This provides a backport of the new `type` statement in Python 3.12:

            type ListOrSet[T] = list[T] | set[T]

        is equivalent to:

            T = TypeVar("T")
            ListOrSet = TypeAliasType("ListOrSet", list[T] | set[T], type_params=(T,))

        The name ListOrSet can then be used as an alias for the type it refers to.

        The type_params argument should contain all the type parameters used
        in the value of the type alias. If the alias is not generic, this
        argument is omitted.

        Static type checkers should only support type aliases declared using
        TypeAliasType that follow these rules:

        - The first argument (the name) must be a string literal.
        - The TypeAliasType instance must be immediately assigned to a variable
          of the same name. (For example, 'X = TypeAliasType("Y", int)' is invalid,
          as is 'X, Y = TypeAliasType("X", int), TypeAliasType("Y", int)').

        
Return True if the given type is a Protocol.

        Example::

            >>> from typing_extensions import Protocol, is_protocol
            >>> class P(Protocol):
            ...     def a(self) -> str: ...
            ...     b: int
            >>> is_protocol(P)
            True
            >>> is_protocol(int)
            False
        
Return the set of members defined in a Protocol.

        Example::

            >>> from typing_extensions import Protocol, get_protocol_members
            >>> class P(Protocol):
            ...     def a(self) -> str: ...
            ...     b: int
            >>> get_protocol_members(P)
            frozenset({'a', 'b'})

        Raise a TypeError for arguments that are not Protocols.
        
Define the documentation of a type annotation using ``Annotated``, to be
         used in class attributes, function and method parameters, return values,
         and variables.

        The value should be a positional-only string literal to allow static tools
        like editors and documentation generators to use it.

        This complements docstrings.

        The string value passed is available in the attribute ``documentation``.

        Example::

            >>> from typing_extensions import Annotated, Doc
            >>> def hi(to: Annotated[str, Doc("Who to say hi to")]) -> None: ...
        
Compute the annotations dict for an object.

        obj may be a callable, class, or module.
        Passing in an object of any other type raises TypeError.

        Returns a dict.  get_annotations() returns a new dict every time
        it's called; calling it twice on the same object will return two
        different but equivalent dicts.

        This is a backport of `inspect.get_annotations`, which has been
        in the standard library since Python 3.10. See the standard library
        documentation for more:

            https://docs.python.org/3/library/inspect.html#inspect.get_annotations

        This backport adds the *format* argument introduced by PEP 649. The
        three formats supported are:
        * VALUE: the annotations are returned as-is. This is the default and
          it is compatible with the behavior on previous Python versions.
        * FORWARDREF: return annotations as-is if possible, but replace any
          undefined names with ForwardRef objects. The implementation proposed by
          PEP 649 relies on language changes that cannot be backported; the
          typing-extensions implementation simply returns the same result as VALUE.
        * STRING: return annotations as strings, in a format close to the original
          source. Again, this behavior cannot be replicated directly in a backport.
          As an approximation, typing-extensions retrieves the annotations under
          VALUE semantics and then stringifies them.

        The purpose of this backport is to allow users who would like to use
        FORWARDREF or STRING semantics once PEP 649 is implemented, but who also
        want to support earlier Python versions, to simply write:

            typing_extensions.get_annotations(obj, format=Format.FORWARDREF)

        

        A lax Python 3.11+ like version of typing._type_check
        
Evaluate a forward reference as a type hint.

        This is similar to calling the ForwardRef.evaluate() method,
        but unlike that method, evaluate_forward_ref() also:

        * Recursively evaluates forward references nested within the type hint.
        * Rejects certain objects that are not valid type hints.
        * Replaces type hints that evaluate to None with types.NoneType.
        * Supports the *FORWARDREF* and *STRING* formats.

        *forward_ref* must be an instance of ForwardRef. *owner*, if given,
        should be the object that holds the annotations that the forward reference
        derived from, such as a module, class object, or function. It is used to
        infer the namespaces to use for looking up names. *globals* and *locals*
        can also be explicitly given to provide the global and local namespaces.
        *type_params* is a tuple of type parameters that are in scope when
        evaluating the forward reference. This parameter must be provided (though
        it may be an empty tuple) if *owner* is not given and the forward reference
        does not already have an owner set. *format* specifies the format of the
        annotation and is a member of the annotationlib.Format enum.

        

---

\n'
        s = s.replace("\r\n", "\n")
    else:
        result = '"'

    pos = seq_start = 0
    while True:
        try:
            char = s[pos]
        except IndexError:
            result += s[seq_start:pos]
            if do_multiline:
                return result + '
Decides if an object behaves as an array of tables (i.e. a nonempty list
    of dicts).
Use heuristics to decide if the inline-style representation is a good
    choice for a given table.

---



---

An error occurred when attempting to build a repr.
Class decorator to create __repr__ from __rich_repr__
Create repr string from __rich_repr__
Auto generate __rich_rep__ from signature of __init__

---

A descriptor to get/set a style attribute bit.
A terminal style.

    A terminal style consists of a color (`color`), a background color (`bgcolor`), and a number of attributes, such
    as bold, italic etc. The attributes have 3 states: they can either be on
    (``True``), off (``False``), or not set (``None``).

    Args:
        color (Union[Color, str], optional): Color of terminal text. Defaults to None.
        bgcolor (Union[Color, str], optional): Color of terminal background. Defaults to None.
        bold (bool, optional): Enable bold text. Defaults to None.
        dim (bool, optional): Enable dim text. Defaults to None.
        italic (bool, optional): Enable italic text. Defaults to None.
        underline (bool, optional): Enable underlined text. Defaults to None.
        blink (bool, optional): Enabled blinking text. Defaults to None.
        blink2 (bool, optional): Enable fast blinking text. Defaults to None.
        reverse (bool, optional): Enabled reverse text. Defaults to None.
        conceal (bool, optional): Enable concealed text. Defaults to None.
        strike (bool, optional): Enable strikethrough text. Defaults to None.
        underline2 (bool, optional): Enable doubly underlined text. Defaults to None.
        frame (bool, optional): Enable framed text. Defaults to None.
        encircle (bool, optional): Enable encircled text. Defaults to None.
        overline (bool, optional): Enable overlined text. Defaults to None.
        link (str, link): Link URL. Defaults to None.

    
Create an 'null' style, equivalent to Style(), but more performant.
Create a new style with colors and no attributes.

        Returns:
            color (Optional[Color]): A (foreground) color, or None for no color. Defaults to None.
            bgcolor (Optional[Color]): A (background) color, or None for no color. Defaults to None.
        
Create a new style with meta data.

        Returns:
            meta (Optional[Dict[str, Any]]): A dictionary of meta data. Defaults to None.
        
Create a blank style with meta information.

        Example:
            style = Style.on(click=self.on_click)

        Args:
            meta (Optional[Dict[str, Any]], optional): An optional dict of meta information.
            **handlers (Any): Keyword arguments are translated in to handlers.

        Returns:
            Style: A Style with meta information attached.
        
Get a link id, used in ansi code for links.
Re-generate style definition from attributes.
A Style is false if it has no attributes, colors, or links.
Generate ANSI codes for this style.

        Args:
            color_system (ColorSystem): Color system.

        Returns:
            str: String containing codes.
        
Normalize a style definition so that styles with the same effect have the same string
        representation.

        Args:
            style (str): A style definition.

        Returns:
            str: Normal form of style definition.
        
Pick first non-None style.
The foreground color or None if it is not set.
The background color or None if it is not set.
Link text, if set.
Check if the style specified a transparent background.
A Style with background only.
Get meta information (can not be changed after construction).
Get a copy of the style with color removed.
Parse a style definition.

        Args:
            style_definition (str): A string containing a style.

        Raises:
            errors.StyleSyntaxError: If the style definition syntax is invalid.

        Returns:
            `Style`: A Style instance.
        
Get a CSS style rule.
Combine styles and get result.

        Args:
            styles (Iterable[Style]): Styles to combine.

        Returns:
            Style: A new style instance.
        
Combine styles from positional argument in to a single style.

        Args:
            *styles (Iterable[Style]): Styles to combine.

        Returns:
            Style: A new style instance.
        
Get a copy of this style.

        Returns:
            Style: A new Style instance with identical attributes.
        
Get a copy of this style with link and meta information removed.

        Returns:
            Style: New style object.
        
Get a copy with a different value for link.

        Args:
            link (str, optional): New value for link. Defaults to None.

        Returns:
            Style: A new Style instance.
        
Render the ANSI codes for the style.

        Args:
            text (str, optional): A string to style. Defaults to "".
            color_system (Optional[ColorSystem], optional): Color system to render to. Defaults to ColorSystem.TRUECOLOR.

        Returns:
            str: A string containing ANSI style codes.
        
Write text with style directly to terminal.

        This method is for testing purposes only.

        Args:
            text (Optional[str], optional): Text to style or None for style name.

        
A stack of styles.
Get the Style at the top of the stack.
Push a new style on to the stack.

        Args:
            style (Style): New style to combine with current style.
        
Pop last style and discard.

        Returns:
            Style: New current style (also available as stack.current)
        

---

Base class for a pager.
Show content in pager.

        Args:
            content (str): Content to be displayed.
        
Uses the pager installed on the system.
Use the same pager used by pydoc.

---

Base class for a syntax theme.
Get a style for a given Pygments token.
Get the background color.
Syntax theme that delegates to Pygments theme.
Get a style from a Pygments class.
Syntax theme to use standard colors.
Look up style in the style map.

    A range to highlight in a Syntax object.
    `start` and `end` are 2-integers tuples, where the first integer is the line number
    (starting from 1) and the second integer is the column index (starting from 0).
    
Construct a Syntax object to render syntax highlighted code.

    Args:
        code (str): Code to highlight.
        lexer (Lexer | str): Lexer to use (see https://pygments.org/docs/lexers/)
        theme (str, optional): Color theme, aka Pygments style (see https://pygments.org/docs/styles/#getting-a-list-of-available-styles). Defaults to "monokai".
        dedent (bool, optional): Enable stripping of initial whitespace. Defaults to False.
        line_numbers (bool, optional): Enable rendering of line numbers. Defaults to False.
        start_line (int, optional): Starting number for line numbers. Defaults to 1.
        line_range (Tuple[int | None, int | None], optional): If given should be a tuple of the start and end line to render.
            A value of None in the tuple indicates the range is open in that direction.
        highlight_lines (Set[int]): A set of line numbers to highlight.
        code_width: Width of code to render (not including line numbers), or ``None`` to use all available width.
        tab_size (int, optional): Size of tabs. Defaults to 4.
        word_wrap (bool, optional): Enable word wrapping.
        background_color (str, optional): Optional background color, or None to use theme color. Defaults to None.
        indent_guides (bool, optional): Show indent guides. Defaults to False.
        padding (PaddingDimensions): Padding to apply around the syntax. Defaults to 0 (no padding).
    
Get a syntax theme instance.
Construct a Syntax object from a file.

        Args:
            path (str): Path to file to highlight.
            encoding (str): Encoding of file.
            lexer (str | Lexer, optional): Lexer to use. If None, lexer will be auto-detected from path/file content.
            theme (str, optional): Color theme, aka Pygments style (see https://pygments.org/docs/styles/#getting-a-list-of-available-styles). Defaults to "emacs".
            dedent (bool, optional): Enable stripping of initial whitespace. Defaults to True.
            line_numbers (bool, optional): Enable rendering of line numbers. Defaults to False.
            start_line (int, optional): Starting number for line numbers. Defaults to 1.
            line_range (Tuple[int, int], optional): If given should be a tuple of the start and end line to render.
            highlight_lines (Set[int]): A set of line numbers to highlight.
            code_width: Width of code to render (not including line numbers), or ``None`` to use all available width.
            tab_size (int, optional): Size of tabs. Defaults to 4.
            word_wrap (bool, optional): Enable word wrapping of code.
            background_color (str, optional): Optional background color, or None to use theme color. Defaults to None.
            indent_guides (bool, optional): Show indent guides. Defaults to False.
            padding (PaddingDimensions): Padding to apply around the syntax. Defaults to 0 (no padding).

        Returns:
            [Syntax]: A Syntax object that may be printed to the console
        
Guess the alias of the Pygments lexer to use based on a path and an optional string of code.
        If code is supplied, it will use a combination of the code and the filename to determine the
        best lexer to use. For example, if the file is ``index.html`` and the file contains Django
        templating syntax, then "html+django" will be returned. If the file is ``index.html``, and no
        templating language is used, the "html" lexer will be used. If no string of code
        is supplied, the lexer will be chosen based on the file extension..

        Args:
             path (AnyStr): The path to the file containing the code you wish to know the lexer for.
             code (str, optional): Optional string of code that will be used as a fallback if no lexer
                is found for the supplied path.

        Returns:
            str: The name of the Pygments lexer that best matches the supplied path/code.
        
Get the base style.
Get a color (if any) for the given token.

        Args:
            token_type (TokenType): A token type tuple from Pygments.

        Returns:
            Optional[Color]: Color from theme, or None for no color.
        
The lexer for this syntax, or None if no lexer was found.

        Tries to find the lexer by name if a string was passed to the constructor.
        
A Pygments Lexer to use if one is not specified or invalid.
Highlight code and return a Text instance.

        Args:
            code (str): Code to highlight.
            line_range(Tuple[int, int], optional): Optional line range to highlight.

        Returns:
            Text: A text instance containing highlighted syntax.
        
Split tokens to one per line.
Convert tokens to spans.

        Adds a custom style on a part of the code, that will be applied to the syntax display when it's rendered.
        Line numbers are 1-based, while column indexes are 0-based.

        Args:
            style (StyleType): The style to apply.
            start (Tuple[int, int]): The start of the range, in the form `[line number, column index]`.
            end (Tuple[int, int]): The end of the range, in the form `[line number, column index]`.
            style_before (bool): Apply the style before any existing styles.
        
Get the number of characters used to render the numbers column.
Get background, number, and highlight styles for line numbers.

        Get the Segments for the Syntax object, excluding any vertical/horizontal padding
        

        Apply stylized ranges to a text instance,
        using the given code to determine the right portion to apply the style to.

        Args:
            text (Text): Text instance to apply the style to.
        

        Applies various processing to a raw code string
        (normalises it so it always ends with a line return, dedents it if necessary, etc.)

        Args:
            code (str): The raw code string to process

        Returns:
            Tuple[bool, str]: the boolean indicates whether the raw code ends with a line return,
                while the string is the processed code.
        

    Returns the index of the code string for the given positions.

    Args:
        newlines_offsets (Sequence[int]): The offset of each newline character found in the code snippet.
        position (SyntaxPosition): The position to search for.

    Returns:
        Optional[int]: The index of the code string for this position, or `None`
            if the given position's line number is out of range (if it's the column that is out of range
            we silently clamp its value so that it reaches the end of the line)
    

---

((\\*)\[([a-z#/@][^[]*?)])
A tag in console markup.
The tag name. e.g. 'bold'.
Any additional parameters after the name.
Get the string representation of this tag.
Escapes text so that it won't be interpreted as markup.

    Args:
        markup (str): Content to be inserted in to markup.

    Returns:
        str: Markup with square brackets escaped.
    
Called by re.sub replace matches.
Parse markup in to an iterable of tuples of (position, text, tag).

    Args:
        markup (str): A string containing console markup

    
Render console markup in to a Text instance.

    Args:
        markup (str): A string containing console markup.
        style: (Union[str, Style]): The style to use.
        emoji (bool, optional): Also render emoji code. Defaults to True.
        emoji_variant (str, optional): Optional emoji variant, either "text" or "emoji". Defaults to None.


    Raises:
        MarkupError: If there is a syntax error in the markup.

    Returns:
        Text: A test instance.
    
Pop tag matching given style name.

---

No emoji by that name.
A single emoji character.

        Args:
            name (str): Name of emoji.
            style (Union[str, Style], optional): Optional style. Defaults to None.

        Raises:
            NoEmoji: If the emoji doesn't exist.
        
Replace emoji markup with corresponding unicode characters.

        Args:
            text (str): A string with emojis codes, e.g. "Hello :smiley:!"

        Returns:
            str: A string with emoji codes replaces with actual emoji.
        

---

Exception base class for prompt related errors.
Exception to indicate a response was invalid. Raise this within process_response() to indicate an error
    and provide an error message.

    Args:
        message (Union[str, Text]): Error message.
    
Ask the user for input until a valid response is received. This is the base class, see one of
    the concrete classes for examples.

    Args:
        prompt (TextType, optional): Prompt text. Defaults to "".
        console (Console, optional): A Console instance or None to use global console. Defaults to None.
        password (bool, optional): Enable password input. Defaults to False.
        choices (List[str], optional): A list of valid choices. Defaults to None.
        case_sensitive (bool, optional): Matching of choices should be case-sensitive. Defaults to True.
        show_default (bool, optional): Show default in prompt. Defaults to True.
        show_choices (bool, optional): Show choices in prompt. Defaults to True.
    
Shortcut to construct and run a prompt loop and return the result.

        Example:
            >>> filename = Prompt.ask("Enter a filename")

        Args:
            prompt (TextType, optional): Prompt text. Defaults to "".
            console (Console, optional): A Console instance or None to use global console. Defaults to None.
            password (bool, optional): Enable password input. Defaults to False.
            choices (List[str], optional): A list of valid choices. Defaults to None.
            case_sensitive (bool, optional): Matching of choices should be case-sensitive. Defaults to True.
            show_default (bool, optional): Show default in prompt. Defaults to True.
            show_choices (bool, optional): Show choices in prompt. Defaults to True.
            stream (TextIO, optional): Optional text file open for reading to get input. Defaults to None.
        
Turn the supplied default in to a Text instance.

        Args:
            default (DefaultType): Default value.

        Returns:
            Text: Text containing rendering of default value.
        
Make prompt text.

        Args:
            default (DefaultType): Default value.

        Returns:
            Text: Text to display in prompt.
        
Get input from user.

        Args:
            console (Console): Console instance.
            prompt (TextType): Prompt text.
            password (bool): Enable password entry.

        Returns:
            str: String from user.
        
Check value is in the list of valid choices.

        Args:
            value (str): Value entered by user.

        Returns:
            bool: True if choice was valid, otherwise False.
        
Process response from user, convert to prompt type.

        Args:
            value (str): String typed by user.

        Raises:
            InvalidResponse: If ``value`` is invalid.

        Returns:
            PromptType: The value to be returned from ask method.
        
Called to handle validation error.

        Args:
            value (str): String entered by user.
            error (InvalidResponse): Exception instance the initiated the error.
        
Hook to display something before the prompt.
Run the prompt loop.

        Args:
            default (Any, optional): Optional default value.

        Returns:
            PromptType: Processed value.
        
A prompt that returns a str.

    Example:
        >>> name = Prompt.ask("Enter your name")


    
A prompt that returns an integer.

    Example:
        >>> burrito_count = IntPrompt.ask("How many burritos do you want to order")

    
A prompt that returns a float.

    Example:
        >>> temperature = FloatPrompt.ask("Enter desired temperature")

    
A yes / no confirmation prompt.

    Example:
        >>> if Confirm.ask("Continue"):
                run_job()

    
Render the default as (y) or (n) rather than True/False.
Convert choices to a bool.

---

Makes appropriate Windows Console API calls based on the segments in the buffer.

    Args:
        buffer (Iterable[Segment]): Iterable of Segments to convert to Win32 API calls.
        term (LegacyWindowsTerm): Used to call the Windows Console API.
    

---

Any object that defines an edge (such as Layout).
Divide total space to satisfy size, ratio, and minimum_size, constraints.

    The returned list of integers should add up to total in most cases, unless it is
    impossible to satisfy all the constraints. For instance, if there are two edges
    with a minimum size of 20 each and `total` is 30 then the returned list will be
    greater than total. In practice, this would mean that a Layout object would
    clip the rows that would overflow the screen height.

    Args:
        total (int): Total number of characters.
        edges (List[Edge]): Edges within total space.

    Returns:
        List[int]: Number of characters for each edge.
    
Divide an integer total in to parts based on ratios.

    Args:
        total (int): The total to divide.
        ratios (List[int]): A list of integer ratios.
        maximums (List[int]): List of maximums values for each slot.
        values (List[int]): List of values

    Returns:
        List[int]: A list of integers guaranteed to sum to total.
    
Distribute an integer total in to parts based on ratios.

    Args:
        total (int): The total to divide.
        ratios (List[int]): A list of integer ratios.
        minimums (List[int]): List of minimum values for each slot.

    Returns:
        List[int]: A list of integers guaranteed to sum to total.
    

---

Check if an object was created with attrs module.
Get fields for an attrs object.
Check if an instance of a dataclass contains the default repr.

    Args:
        obj (object): A dataclass instance.

    Returns:
        bool: True if the default repr is used, False if there is a custom repr.
    
Check if an instance of namedtuple contains the default repr

    Args:
        obj (object): A namedtuple

    Returns:
        bool: True if the default repr is used, False if there's a custom repr.
    
isinstance can fail in rare cases, for example types with no __class__
Install automatic pretty printing in the Python REPL.

    Args:
        console (Console, optional): Console instance or ``None`` to use global console. Defaults to None.
        overflow (Optional[OverflowMethod], optional): Overflow method. Defaults to "ignore".
        crop (Optional[bool], optional): Enable cropping of long lines. Defaults to False.
        indent_guides (bool, optional): Enable indentation guides. Defaults to False.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to None.
        max_depth (int, optional): Maximum depth of nested data structures, or None for no maximum. Defaults to None.
        expand_all (bool, optional): Expand all containers. Defaults to False.
        max_frames (int): Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.
    
Replacement sys.displayhook which prettifies objects with Rich.
A rich renderable that pretty prints an object.

    Args:
        _object (Any): An object to pretty print.
        highlighter (HighlighterType, optional): Highlighter object to apply to result, or None for ReprHighlighter. Defaults to None.
        indent_size (int, optional): Number of spaces in indent. Defaults to 4.
        justify (JustifyMethod, optional): Justify method, or None for default. Defaults to None.
        overflow (OverflowMethod, optional): Overflow method, or None for default. Defaults to None.
        no_wrap (Optional[bool], optional): Disable word wrapping. Defaults to False.
        indent_guides (bool, optional): Enable indentation guides. Defaults to False.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to None.
        max_depth (int, optional): Maximum depth of nested data structures, or None for no maximum. Defaults to None.
        expand_all (bool, optional): Expand all containers. Defaults to False.
        margin (int, optional): Subtrace a margin from width to force containers to expand earlier. Defaults to 0.
        insert_line (bool, optional): Insert a new line if the output has multiple new lines. Defaults to False.
    
Check if an object may be expanded by pretty print.
A node in a repr tree. May be atomic or a container.
Generate tokens for this node.
Check the length fits within a limit.

        Args:
            start_length (int): Starting length of the line (indent, prefix, suffix).
            max_length (int): Maximum length.

        Returns:
            bool: True if the node can be rendered within max length, otherwise False.
        
Render the node to a pretty repr.

        Args:
            max_width (int, optional): Maximum width of the repr. Defaults to 80.
            indent_size (int, optional): Size of indents. Defaults to 4.
            expand_all (bool, optional): Expand all levels. Defaults to False.

        Returns:
            str: A repr string of the original object.
        
A line in repr output.
Check if the line may be expanded.
Check this line fits within a given number of cells.
Expand this line by adding children on their own line.
Checks if an object is most likely a namedtuple. It is possible
    to craft an object that passes this check and isn't a namedtuple, but
    there is only a minuscule chance of this happening unintentionally.

    Args:
        obj (Any): The object to test

    Returns:
        bool: True if the object is a namedtuple. False otherwise.
    
Traverse object and generate a tree.

    Args:
        _object (Any): Object to be traversed.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable truncating.
            Defaults to None.
        max_depth (int, optional): Maximum depth of data structures, or None for no maximum.
            Defaults to None.

    Returns:
        Node: The root of a tree structure which can be used to render a pretty repr.
    
Get repr string for an object, but catch errors.
Walk the object depth first.
Iterate over attr fields and values.
Prettify repr string by expanding on to new lines to fit within a given width.

    Args:
        _object (Any): Object to repr.
        max_width (int, optional): Desired maximum width of repr string. Defaults to 80.
        indent_size (int, optional): Number of spaces to indent. Defaults to 4.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable truncating.
            Defaults to None.
        max_depth (int, optional): Maximum depth of nested data structure, or None for no depth.
            Defaults to None.
        expand_all (bool, optional): Expand all containers regardless of available width. Defaults to False.

    Returns:
        str: A possibly multi-line representation of the object.
    
A convenience function for pretty printing.

    Args:
        _object (Any): Object to pretty print.
        console (Console, optional): Console instance, or None to use default. Defaults to None.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of strings before truncating, or None to disable. Defaults to None.
        max_depth (int, optional): Maximum depth for nested data structures, or None for unlimited depth. Defaults to None.
        indent_guides (bool, optional): Enable indentation guides. Defaults to True.
        expand_all (bool, optional): Expand all containers. Defaults to False.
    

---

Draw space around content.

    Example:
        >>> print(Padding("Hello", (2, 4), style="on blue"))

    Args:
        renderable (RenderableType): String or other renderable.
        pad (Union[int, Tuple[int]]): Padding for top, right, bottom, and left borders.
            May be specified with 1, 2, or 4 integers (CSS style).
        style (Union[str, Style], optional): Style for padding characters. Defaults to "none".
        expand (bool, optional): Expand padding to fit available width. Defaults to True.
    
Make padding instance to render an indent.

        Args:
            renderable (RenderableType): String or other renderable.
            level (int): Number of characters to indent.

        Returns:
            Padding: A Padding instance.
        
Unpack padding specified in CSS style.

---

Defines characters to render boxes.

    ┌─┬┐ top
    │ ││ head
    ├─┼┤ head_row
    │ ││ mid
    ├─┼┤ row
    ├─┼┤ foot_row
    │ ││ foot
    └─┴┘ bottom

    Args:
        box (str): Characters making up box.
        ascii (bool, optional): True if this box uses ascii characters only. Default is False.
    
Substitute this box for another if it won't render due to platform issues.

        Args:
            options (ConsoleOptions): Console options used in rendering.
            safe (bool, optional): Substitute this for another Box if there are known problems
                displaying on the platform (currently only relevant on Windows). Default is True.

        Returns:
            Box: A different Box or the same Box.
        
If this box uses special characters for the borders of the header, then
        return the equivalent box that does not.

        Returns:
            Box: The most similar Box that doesn't use header-specific box characters.
                If the current Box already satisfies this criterion, then it's returned.
        
Get the top of a simple box.

        Args:
            widths (List[int]): Widths of columns.

        Returns:
            str: A string of box characters.
        
Get the top of a simple box.

        Args:
            width (List[int]): Widths of columns.

        Returns:
            str: A string of box characters.
        
Get the bottom of a simple box.

        Args:
            widths (List[int]): Widths of columns.

        Returns:
            str: A string of box characters.
        

---

Apply a style to a renderable.

    Args:
        renderable (RenderableType): Any renderable.
        style (StyleType): A style to apply across the entire renderable.
    

---

Replace emoji code in text.

---


(?:\x1b[0-?])|
(?:\x1b\](.*?)\x1b\\)|
(?:\x1b([(@-Z\\-_]|\[[0-?]*[ -/]*[@-~]))

Result of ansi tokenized string.
Tokenize a string in to plain text and ANSI codes.

    Args:
        ansi_text (str): A String containing ANSI codes.

    Yields:
        AnsiToken: A named tuple of (plain, sgr, osc)
    
Translate ANSI code in to styled Text.
Decode ANSI codes in an iterable of lines.

        Args:
            lines (Iterable[str]): An iterable of lines of terminal output.

        Yields:
            Text: Marked up Text.
        
Decode a line containing ansi codes.

        Args:
            line (str): A line of terminal output.

        Returns:
            Text: A Text instance marked up according to ansi codes.
        

---

A renderable which pretty prints JSON.

    Args:
        json (str): JSON encoded data.
        indent (Union[None, int, str], optional): Number of characters to indent by. Defaults to 2.
        highlight (bool, optional): Enable highlighting. Defaults to True.
        skip_keys (bool, optional): Skip keys not of a basic type. Defaults to False.
        ensure_ascii (bool, optional): Escape all non-ascii characters. Defaults to False.
        check_circular (bool, optional): Check for circular references. Defaults to True.
        allow_nan (bool, optional): Allow NaN and Infinity values. Defaults to True.
        default (Callable, optional): A callable that converts values that can not be encoded
            in to something that can be JSON encoded. Defaults to None.
        sort_keys (bool, optional): Sort dictionary keys. Defaults to False.
    
Encodes a JSON object from arbitrary data.

        Args:
            data (Any): An object that may be encoded in to JSON
            indent (Union[None, int, str], optional): Number of characters to indent by. Defaults to 2.
            highlight (bool, optional): Enable highlighting. Defaults to True.
            default (Callable, optional): Optional callable which will be called for objects that cannot be serialized. Defaults to None.
            skip_keys (bool, optional): Skip keys not of a basic type. Defaults to False.
            ensure_ascii (bool, optional): Escape all non-ascii characters. Defaults to False.
            check_circular (bool, optional): Check for circular references. Defaults to True.
            allow_nan (bool, optional): Allow NaN and Infinity values. Defaults to True.
            default (Callable, optional): A callable that converts values that can not be encoded
                in to something that can be JSON encoded. Defaults to None.
            sort_keys (bool, optional): Sort dictionary keys. Defaults to False.

        Returns:
            JSON: New JSON object from the given data.
        

---

Defines a column within a ~Table.

    Args:
        title (Union[str, Text], optional): The title of the table rendered at the top. Defaults to None.
        caption (Union[str, Text], optional): The table caption rendered below. Defaults to None.
        width (int, optional): The width in characters of the table, or ``None`` to automatically fit. Defaults to None.
        min_width (Optional[int], optional): The minimum width of the table, or ``None`` for no minimum. Defaults to None.
        box (box.Box, optional): One of the constants in box.py used to draw the edges (see :ref:`appendix_box`), or ``None`` for no box lines. Defaults to box.HEAVY_HEAD.
        safe_box (Optional[bool], optional): Disable box characters that don't display on windows legacy terminal with *raster* fonts. Defaults to True.
        padding (PaddingDimensions, optional): Padding for cells (top, right, bottom, left). Defaults to (0, 1).
        collapse_padding (bool, optional): Enable collapsing of padding around cells. Defaults to False.
        pad_edge (bool, optional): Enable padding of edge cells. Defaults to True.
        expand (bool, optional): Expand the table to fit the available space if ``True``, otherwise the table width will be auto-calculated. Defaults to False.
        show_header (bool, optional): Show a header row. Defaults to True.
        show_footer (bool, optional): Show a footer row. Defaults to False.
        show_edge (bool, optional): Draw a box around the outside of the table. Defaults to True.
        show_lines (bool, optional): Draw lines between every row. Defaults to False.
        leading (int, optional): Number of blank lines between rows (precludes ``show_lines``). Defaults to 0.
        style (Union[str, Style], optional): Default style for the table. Defaults to "none".
        row_styles (List[Union, str], optional): Optional list of row styles, if more than one style is given then the styles will alternate. Defaults to None.
        header_style (Union[str, Style], optional): Style of the header. Defaults to "table.header".
        footer_style (Union[str, Style], optional): Style of the footer. Defaults to "table.footer".
        border_style (Union[str, Style], optional): Style of the border. Defaults to None.
        title_style (Union[str, Style], optional): Style of the title. Defaults to None.
        caption_style (Union[str, Style], optional): Style of the caption. Defaults to None.
        title_justify (str, optional): Justify method for title. Defaults to "center".
        caption_justify (str, optional): Justify method for caption. Defaults to "center".
        highlight (bool, optional): Highlight cell contents (if str). Defaults to False.
    
RenderableType: Renderable for the header (typically a string)
RenderableType: Renderable for the footer (typically a string)
StyleType: The style of the header.
StyleType: The style of the footer.
StyleType: The style of the column.
str: How to justify text within the column ("left", "center", "right", or "full")
str: How to vertically align content ("top", "middle", or "bottom")
str: Overflow method.
Optional[int]: Width of the column, or ``None`` (default) to auto calculate width.
Optional[int]: Minimum width of column, or ``None`` for no minimum. Defaults to None.
Optional[int]: Maximum width of column, or ``None`` for no maximum. Defaults to None.
Optional[int]: Ratio to use when calculating column width, or ``None`` (default) to adapt to column contents.
bool: Prevent wrapping of text within the column. Defaults to ``False``.
bool: Apply highlighter to column. Defaults to ``False``.
Index of column.
Return a copy of this Column.
Get all cells in the column, not including header.
Check if this column is flexible.
Information regarding a row.
Style to apply to row.
Indicated end of section, which will force a line beneath the row.
A single cell in a table.
Style to apply to cell.
Cell renderable.
Cell vertical alignment.
A console renderable to draw a table.

    Args:
        *headers (Union[Column, str]): Column headers, either as a string, or :class:`~rich.table.Column` instance.
        title (Union[str, Text], optional): The title of the table rendered at the top. Defaults to None.
        caption (Union[str, Text], optional): The table caption rendered below. Defaults to None.
        width (int, optional): The width in characters of the table, or ``None`` to automatically fit. Defaults to None.
        min_width (Optional[int], optional): The minimum width of the table, or ``None`` for no minimum. Defaults to None.
        box (box.Box, optional): One of the constants in box.py used to draw the edges (see :ref:`appendix_box`), or ``None`` for no box lines. Defaults to box.HEAVY_HEAD.
        safe_box (Optional[bool], optional): Disable box characters that don't display on windows legacy terminal with *raster* fonts. Defaults to True.
        padding (PaddingDimensions, optional): Padding for cells (top, right, bottom, left). Defaults to (0, 1).
        collapse_padding (bool, optional): Enable collapsing of padding around cells. Defaults to False.
        pad_edge (bool, optional): Enable padding of edge cells. Defaults to True.
        expand (bool, optional): Expand the table to fit the available space if ``True``, otherwise the table width will be auto-calculated. Defaults to False.
        show_header (bool, optional): Show a header row. Defaults to True.
        show_footer (bool, optional): Show a footer row. Defaults to False.
        show_edge (bool, optional): Draw a box around the outside of the table. Defaults to True.
        show_lines (bool, optional): Draw lines between every row. Defaults to False.
        leading (int, optional): Number of blank lines between rows (precludes ``show_lines``). Defaults to 0.
        style (Union[str, Style], optional): Default style for the table. Defaults to "none".
        row_styles (List[Union, str], optional): Optional list of row styles, if more than one style is given then the styles will alternate. Defaults to None.
        header_style (Union[str, Style], optional): Style of the header. Defaults to "table.header".
        footer_style (Union[str, Style], optional): Style of the footer. Defaults to "table.footer".
        border_style (Union[str, Style], optional): Style of the border. Defaults to None.
        title_style (Union[str, Style], optional): Style of the title. Defaults to None.
        caption_style (Union[str, Style], optional): Style of the caption. Defaults to None.
        title_justify (str, optional): Justify method for title. Defaults to "center".
        caption_justify (str, optional): Justify method for caption. Defaults to "center".
        highlight (bool, optional): Highlight cell contents (if str). Defaults to False.
    
Get a table with no lines, headers, or footer.

        Args:
            *headers (Union[Column, str]): Column headers, either as a string, or :class:`~rich.table.Column` instance.
            padding (PaddingDimensions, optional): Get padding around cells. Defaults to 0.
            collapse_padding (bool, optional): Enable collapsing of padding around cells. Defaults to True.
            pad_edge (bool, optional): Enable padding around edges of table. Defaults to False.
            expand (bool, optional): Expand the table to fit the available space if ``True``, otherwise the table width will be auto-calculated. Defaults to False.

        Returns:
            Table: A table instance.
        
Setting a non-None self.width implies expand.
Set expand.
Get extra width to add to cell content.
Get the current number of rows.
Get the current row style.
Get cell padding.
Set cell padding.
Add a column to the table.

        Args:
            header (RenderableType, optional): Text or renderable for the header.
                Defaults to "".
            footer (RenderableType, optional): Text or renderable for the footer.
                Defaults to "".
            header_style (Union[str, Style], optional): Style for the header, or None for default. Defaults to None.
            highlight (bool, optional): Whether to highlight the text. The default of None uses the value of the table (self) object.
            footer_style (Union[str, Style], optional): Style for the footer, or None for default. Defaults to None.
            style (Union[str, Style], optional): Style for the column cells, or None for default. Defaults to None.
            justify (JustifyMethod, optional): Alignment for cells. Defaults to "left".
            vertical (VerticalAlignMethod, optional): Vertical alignment, one of "top", "middle", or "bottom". Defaults to "top".
            overflow (OverflowMethod): Overflow method: "crop", "fold", "ellipsis". Defaults to "ellipsis".
            width (int, optional): Desired width of column in characters, or None to fit to contents. Defaults to None.
            min_width (Optional[int], optional): Minimum width of column, or ``None`` for no minimum. Defaults to None.
            max_width (Optional[int], optional): Maximum width of column, or ``None`` for no maximum. Defaults to None.
            ratio (int, optional): Flexible ratio for the column (requires ``Table.expand`` or ``Table.width``). Defaults to None.
            no_wrap (bool, optional): Set to ``True`` to disable wrapping of this column.
        
Add a row of renderables.

        Args:
            *renderables (None or renderable): Each cell in a row must be a renderable object (including str),
                or ``None`` for a blank cell.
            style (StyleType, optional): An optional style to apply to the entire row. Defaults to None.
            end_section (bool, optional): End a section and draw a line. Defaults to False.

        Raises:
            errors.NotRenderableError: If you add something that can't be rendered.
        
Add a new section (draw a line after current row).
Calculate the widths of each column, including padding, not including borders.
Reduce widths so that the total is under max_width.

        Args:
            widths (List[int]): List of widths.
            wrapable (List[bool]): List of booleans that indicate if a column may shrink.
            max_width (int): Maximum width to reduce to.

        Returns:
            List[int]: A new list of widths.
        
Get all the cells with padding and optional header.
Get extra width from padding.
Get the minimum and maximum width of the column.

---

Display renderables in neat columns.

    Args:
        renderables (Iterable[RenderableType]): Any number of Rich renderables (including str).
        width (int, optional): The desired width of the columns, or None to auto detect. Defaults to None.
        padding (PaddingDimensions, optional): Optional padding around cells. Defaults to (0, 1).
        expand (bool, optional): Expand columns to full width. Defaults to False.
        equal (bool, optional): Arrange in to equal sized columns. Defaults to False.
        column_first (bool, optional): Align items from top to bottom (rather than left to right). Defaults to False.
        right_to_left (bool, optional): Start column from right hand side. Defaults to False.
        align (str, optional): Align value ("left", "right", or "center") or None for default. Defaults to None.
        title (TextType, optional): Optional title for Columns.
    
Add a renderable to the columns.

        Args:
            renderable (RenderableType): Any renderable object.
        

---

Creates a renderable that may be updated.

    Args:
        renderable (RenderableType): Any renderable object.
        style (StyleType, optional): An optional style to apply to the renderable. Defaults to "".
    
Set a new renderable.

        Args:
            renderable (RenderableType): Any renderable object, including str.
        
Get control codes to move cursor to beginning of live render.

        Returns:
            Control: A control instance that may be printed.
        
Get control codes to clear the render and restore the cursor to its previous position.

        Returns:
            Control: A Control instance that may be printed.
        

---

Iterate and generate a tuple with a flag for first value.
Iterate and generate a tuple with a flag for last value.
Iterate and generate a tuple with a flag for first and last value.

---

One of the 3 color system supported by terminals.
Type of color stored in Color class.
The color could not be parsed.
^
\#([0-9a-f]{6})$|
color\(([0-9]{1,3})\)$|
rgb\(([\d\s,]+)\)$

Terminal color definition.
The name of the color (typically the input to Color.parse).
The type of the color.
The color number, if a standard color, or None.
A triplet of color components, if an RGB color.
Displays the actual color if Rich printed.
Get the native color system for this color.
Check if the color is ultimately defined by the system.
Check if the color is a default color.
Get an equivalent color triplet for this color.

        Args:
            theme (TerminalTheme, optional): Optional terminal theme, or None to use default. Defaults to None.
            foreground (bool, optional): True for a foreground color, or False for background. Defaults to True.

        Returns:
            ColorTriplet: A color triplet containing RGB components.
        
Create a Color number from it's 8-bit ansi number.

        Args:
            number (int): A number between 0-255 inclusive.

        Returns:
            Color: A new Color instance.
        
Create a truecolor RGB color from a triplet of values.

        Args:
            triplet (ColorTriplet): A color triplet containing red, green and blue components.

        Returns:
            Color: A new color object.
        
Create a truecolor from three color components in the range(0->255).

        Args:
            red (float): Red component in range 0-255.
            green (float): Green component in range 0-255.
            blue (float): Blue component in range 0-255.

        Returns:
            Color: A new color object.
        
Get a Color instance representing the default color.

        Returns:
            Color: Default color.
        
Parse a color definition.
Get the ANSI escape codes for this color.
Downgrade a color system to a system with fewer colors.
Parse six hex characters in to RGB triplet.
Blend one RGB color in to another.

---

A thread to periodically update progress.
Track progress by iterating over a sequence.

    Args:
        sequence (Iterable[ProgressType]): A sequence (must support "len") you wish to iterate over.
        description (str, optional): Description of task show next to progress bar. Defaults to "Working".
        total: (float, optional): Total number of steps. Default is len(sequence).
        completed (int, optional): Number of steps completed so far. Defaults to 0.
        auto_refresh (bool, optional): Automatic refresh, disable to force a refresh after each iteration. Default is True.
        transient: (bool, optional): Clear the progress on exit. Defaults to False.
        console (Console, optional): Console to write to. Default creates internal Console instance.
        refresh_per_second (float): Number of times per second to refresh the progress information. Defaults to 10.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
        update_period (float, optional): Minimum time (in seconds) between calls to update(). Defaults to 0.1.
        disable (bool, optional): Disable display of progress.
        show_speed (bool, optional): Show speed if total isn't known. Defaults to True.
    Returns:
        Iterable[ProgressType]: An iterable of the values in the sequence.

    
A reader that tracks progress while it's being read from.
A utility class to handle a context for both a reader and a progress.
Read bytes from a file while tracking progress.

    Args:
        file (Union[str, PathLike[str], BinaryIO]): The path to the file to read, or a file-like object in binary mode.
        total (int): Total number of bytes to read.
        description (str, optional): Description of task show next to progress bar. Defaults to "Reading".
        auto_refresh (bool, optional): Automatic refresh, disable to force a refresh after each iteration. Default is True.
        transient: (bool, optional): Clear the progress on exit. Defaults to False.
        console (Console, optional): Console to write to. Default creates internal Console instance.
        refresh_per_second (float): Number of times per second to refresh the progress information. Defaults to 10.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
        disable (bool, optional): Disable display of progress.
    Returns:
        ContextManager[BinaryIO]: A context manager yielding a progress reader.

    
Read bytes from a file while tracking progress.

    Args:
        path (Union[str, PathLike[str], BinaryIO]): The path to the file to read, or a file-like object in binary mode.
        mode (str): The mode to use to open the file. Only supports "r", "rb" or "rt".
        buffering (int): The buffering strategy to use, see :func:`io.open`.
        encoding (str, optional): The encoding to use when reading in text mode, see :func:`io.open`.
        errors (str, optional): The error handling strategy for decoding errors, see :func:`io.open`.
        newline (str, optional): The strategy for handling newlines in text mode, see :func:`io.open`
        total: (int, optional): Total number of bytes to read. Must be provided if reading from a file handle. Default for a path is os.stat(file).st_size.
        description (str, optional): Description of task show next to progress bar. Defaults to "Reading".
        auto_refresh (bool, optional): Automatic refresh, disable to force a refresh after each iteration. Default is True.
        transient: (bool, optional): Clear the progress on exit. Defaults to False.
        console (Console, optional): Console to write to. Default creates internal Console instance.
        refresh_per_second (float): Number of times per second to refresh the progress information. Defaults to 10.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
        disable (bool, optional): Disable display of progress.
        encoding (str, optional): The encoding to use when reading in text mode.

    Returns:
        ContextManager[BinaryIO]: A context manager yielding a progress reader.

    
Base class for a widget to use in progress display.
Get a table column, used to build tasks table.
Called by the Progress object to return a renderable for the given task.

        Args:
            task (Task): An object containing information regarding the task.

        Returns:
            RenderableType: Anything renderable (including str).
        
Should return a renderable object.
A column to insert an arbitrary column.

    Args:
        renderable (RenderableType, optional): Any renderable. Defaults to empty string.
    
A column with a 'spinner' animation.

    Args:
        spinner_name (str, optional): Name of spinner animation. Defaults to "dots".
        style (StyleType, optional): Style of spinner. Defaults to "progress.spinner".
        speed (float, optional): Speed factor of spinner. Defaults to 1.0.
        finished_text (TextType, optional): Text used when task is finished. Defaults to " ".
    
Set a new spinner.

        Args:
            spinner_name (str): Spinner name, see python -m rich.spinner.
            spinner_style (Optional[StyleType], optional): Spinner style. Defaults to "progress.spinner".
            speed (float, optional): Speed factor of spinner. Defaults to 1.0.
        
A column containing text.
Renders a visual progress bar.

    Args:
        bar_width (Optional[int], optional): Width of bar or None for full width. Defaults to 40.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
    
Gets a progress bar widget for a task.
Renders time elapsed.
Show time elapsed.
Show task progress as a percentage.

    Args:
        text_format (str, optional): Format for percentage display. Defaults to "[progress.percentage]{task.percentage:>3.0f}%".
        text_format_no_percentage (str, optional): Format if percentage is unknown. Defaults to "".
        style (StyleType, optional): Style of output. Defaults to "none".
        justify (JustifyMethod, optional): Text justification. Defaults to "left".
        markup (bool, optional): Enable markup. Defaults to True.
        highlighter (Optional[Highlighter], optional): Highlighter to apply to output. Defaults to None.
        table_column (Optional[Column], optional): Table Column to use. Defaults to None.
        show_speed (bool, optional): Show speed if total is unknown. Defaults to False.
    
Render the speed in iterations per second.

        Args:
            task (Task): A Task object.

        Returns:
            Text: Text object containing the task speed.
        
Renders estimated time remaining.

    Args:
        compact (bool, optional): Render MM:SS when time remaining is less than an hour. Defaults to False.
        elapsed_when_finished (bool, optional): Render time elapsed when the task is finished. Defaults to False.
    
Show time remaining.
Renders completed filesize.
Show data completed.
Renders total filesize.
Show data completed.
Renders completed count/total, e.g. '  10/1000'.

    Best for bounded tasks with int quantities.

    Space pads the completed count so that progress length does not change as task progresses
    past powers of 10.

    Args:
        separator (str, optional): Text to separate completed and total values. Defaults to "/".
    
Show completed/total.
Renders file size downloaded and total, e.g. '0.5/2.3 GB'.

    Args:
        binary_units (bool, optional): Use binary units, KiB, MiB etc. Defaults to False.
    
Calculate common unit for completed and total.
Renders human readable transfer speed.
Show data transfer speed.
Sample of progress for a given time.
Timestamp of sample.
Number of steps completed.
Information regarding a progress task.

    This object should be considered read-only outside of the :class:`~Progress` class.

    
Task ID associated with this task (used in Progress methods).
str: Description of the task.
Optional[float]: Total number of steps in this task.
float: Number of steps completed
Callable to get the current time.
float: Time task was finished.
bool: Indicates if this task is visible in the progress display.
dict: Arbitrary fields passed in via Progress.update.
Optional[float]: Time this task was started, or None if not started.
Optional[float]: Time this task was stopped, or None if not stopped.
Optional[float]: The last speed for a finished task.
Thread lock.
float: Get the current time, in seconds.
bool: Check if the task as started.
Optional[float]: Get the number of steps remaining, if a non-None total was set.
Optional[float]: Time elapsed since task was started, or ``None`` if the task hasn't started.
Check if the task has finished.
float: Get progress of task as a percentage. If a None total was set, returns 0
Optional[float]: Get the estimated speed in steps per second.
Optional[float]: Get estimated time to completion, or ``None`` if no data.
Reset progress.
Renders an auto-updating progress bar(s).

    Args:
        console (Console, optional): Optional Console instance. Defaults to an internal Console instance writing to stdout.
        auto_refresh (bool, optional): Enable auto refresh. If disabled, you will need to call `refresh()`.
        refresh_per_second (Optional[float], optional): Number of times per second to refresh the progress information or None to use default (10). Defaults to None.
        speed_estimate_period: (float, optional): Period (in seconds) used to calculate the speed estimate. Defaults to 30.
        transient: (bool, optional): Clear the progress on exit. Defaults to False.
        redirect_stdout: (bool, optional): Enable redirection of stdout, so ``print`` may be used. Defaults to True.
        redirect_stderr: (bool, optional): Enable redirection of stderr. Defaults to True.
        get_time: (Callable, optional): A callable that gets the current time, or None to use Console.get_time. Defaults to None.
        disable (bool, optional): Disable progress display. Defaults to False
        expand (bool, optional): Expand tasks table to fit width. Defaults to False.
    
Get the default columns used for a new Progress instance:
           - a text column for the description (TextColumn)
           - the bar itself (BarColumn)
           - a text column showing completion percentage (TextColumn)
           - an estimated-time-remaining column (TimeRemainingColumn)
        If the Progress instance is created without passing a columns argument,
        the default columns defined here will be used.

        You can also create a Progress instance using custom columns before
        and/or after the defaults, as in this example:

            progress = Progress(
                SpinnerColumn(),
                *Progress.get_default_columns(),
                "Elapsed:",
                TimeElapsedColumn(),
            )

        This code shows the creation of a Progress display, containing
        a spinner to the left, the default columns, and a labeled elapsed
        time column.
        
Get a list of Task instances.
A list of task IDs.
Check if all tasks have been completed.
Start the progress display.
Stop the progress display.
Track progress by iterating over a sequence.

        Args:
            sequence (Sequence[ProgressType]): A sequence of values you want to iterate over and track progress.
            total: (float, optional): Total number of steps. Default is len(sequence).
            completed (int, optional): Number of steps completed so far. Defaults to 0.
            task_id: (TaskID): Task to track. Default is new task.
            description: (str, optional): Description of task, if new task is created.
            update_period (float, optional): Minimum time (in seconds) between calls to update(). Defaults to 0.1.

        Returns:
            Iterable[ProgressType]: An iterable of values taken from the provided sequence.
        
Track progress file reading from a binary file.

        Args:
            file (BinaryIO): A file-like object opened in binary mode.
            total (int, optional): Total number of bytes to read. This must be provided unless a task with a total is also given.
            task_id (TaskID): Task to track. Default is new task.
            description (str, optional): Description of task, if new task is created.

        Returns:
            BinaryIO: A readable file-like object in binary mode.

        Raises:
            ValueError: When no total value can be extracted from the arguments or the task.
        
Track progress while reading from a binary file.

        Args:
            path (Union[str, PathLike[str]]): The path to the file to read.
            mode (str): The mode to use to open the file. Only supports "r", "rb" or "rt".
            buffering (int): The buffering strategy to use, see :func:`io.open`.
            encoding (str, optional): The encoding to use when reading in text mode, see :func:`io.open`.
            errors (str, optional): The error handling strategy for decoding errors, see :func:`io.open`.
            newline (str, optional): The strategy for handling newlines in text mode, see :func:`io.open`.
            total (int, optional): Total number of bytes to read. If none given, os.stat(path).st_size is used.
            task_id (TaskID): Task to track. Default is new task.
            description (str, optional): Description of task, if new task is created.

        Returns:
            BinaryIO: A readable file-like object in binary mode.

        Raises:
            ValueError: When an invalid mode is given.
        
Start a task.

        Starts a task (used when calculating elapsed time). You may need to call this manually,
        if you called ``add_task`` with ``start=False``.

        Args:
            task_id (TaskID): ID of task.
        
Stop a task.

        This will freeze the elapsed time on the task.

        Args:
            task_id (TaskID): ID of task.
        
Update information associated with a task.

        Args:
            task_id (TaskID): Task id (returned by add_task).
            total (float, optional): Updates task.total if not None.
            completed (float, optional): Updates task.completed if not None.
            advance (float, optional): Add a value to task.completed if not None.
            description (str, optional): Change task description if not None.
            visible (bool, optional): Set visible flag if not None.
            refresh (bool): Force a refresh of progress information. Default is False.
            **fields (Any): Additional data fields required for rendering.
        
Reset a task so completed is 0 and the clock is reset.

        Args:
            task_id (TaskID): ID of task.
            start (bool, optional): Start the task after reset. Defaults to True.
            total (float, optional): New total steps in task, or None to use current total. Defaults to None.
            completed (int, optional): Number of steps completed. Defaults to 0.
            visible (bool, optional): Enable display of the task. Defaults to True.
            description (str, optional): Change task description if not None. Defaults to None.
            **fields (str): Additional data fields required for rendering.
        
Advance task by a number of steps.

        Args:
            task_id (TaskID): ID of task.
            advance (float): Number of steps to advance. Default is 1.
        
Refresh (render) the progress information.
Get a renderable for the progress display.
Get a number of renderables for the progress display.
Get a table to render the Progress display.

        Args:
            tasks (Iterable[Task]): An iterable of Task instances, one per row of the table.

        Returns:
            Table: A table instance.
        
Makes the Progress class itself renderable.
Add a new 'task' to the Progress display.

        Args:
            description (str): A description of the task.
            start (bool, optional): Start the task immediately (to calculate elapsed time). If set to False,
                you will need to call `start` manually. Defaults to True.
            total (float, optional): Number of total steps in the progress if known.
                Set to None to render a pulsing animation. Defaults to 100.
            completed (int, optional): Number of steps completed so far. Defaults to 0.
            visible (bool, optional): Enable display of the task. Defaults to True.
            **fields (str): Additional data fields required for rendering.

        Returns:
            TaskID: An ID you can use when calling `update`.
        
Delete a task if it exists.

        Args:
            task_id (TaskID): A task ID.

        
Iterate and generate a tuple with a flag for last value.

---

Render python variables in a given scope.

    Args:
        scope (Mapping): A mapping containing variable names and values.
        title (str, optional): Optional title. Defaults to None.
        sort_keys (bool, optional): Enable sorting of items. Defaults to True.
        indent_guides (bool, optional): Enable indentation guides. Defaults to False.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to None.

    Returns:
        ConsoleRenderable: A renderable object.
    
Sort special variables first, then alphabetically.

---

Light wrapper around the Win32 Console API - this module should only be imported on Windows

The API that this module wraps is documented at https://docs.microsoft.com/en-us/windows/console/console-functions

Coordinates in the Windows Console API are (y, x), not (x, y).
    This class is intended to prevent that confusion.
    Rows and columns are indexed from 0.
    This class can be used in place of wintypes._COORD in arguments and argtypes.
    
Converts a WindowsCoordinates into a wintypes _COORD structure.
        This classmethod is internally called by ctypes to perform the conversion.

        Args:
            value (WindowsCoordinates): The input coordinates to convert.

        Returns:
            wintypes._COORD: The converted coordinates struct.
        
Retrieves a handle to the specified standard device (standard input, standard output, or standard error).

    Args:
        handle (int): Integer identifier for the handle. Defaults to -11 (stdout).

    Returns:
        wintypes.HANDLE: The handle
    
Retrieves the current input mode of a console's input buffer
    or the current output mode of a console screen buffer.

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.

    Raises:
        LegacyWindowsError: If any error occurs while calling the Windows console API.

    Returns:
        int: Value representing the current console mode as documented at
            https://docs.microsoft.com/en-us/windows/console/getconsolemode#parameters
    
Writes a character to the console screen buffer a specified number of times, beginning at the specified coordinates.

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
        char (str): The character to write. Must be a string of length 1.
        length (int): The number of times to write the character.
        start (WindowsCoordinates): The coordinates to start writing at.

    Returns:
        int: The number of characters written.
    
Sets the character attributes for a specified number of character cells,
    beginning at the specified coordinates in a screen buffer.

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
        attributes (int): Integer value representing the foreground and background colours of the cells.
        length (int): The number of cells to set the output attribute of.
        start (WindowsCoordinates): The coordinates of the first cell whose attributes are to be set.

    Returns:
        int: The number of cells whose attributes were actually set.
    
Set the colour attributes for all text written after this function is called.

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
        attributes (int): Integer value representing the foreground and background colours.


    Returns:
        bool: True if the attribute was set successfully, otherwise False.
    
Retrieves information about the specified console screen buffer.

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.

    Returns:
        CONSOLE_SCREEN_BUFFER_INFO: A CONSOLE_SCREEN_BUFFER_INFO ctype struct contain information about
            screen size, cursor position, colour attributes, and more.
Set the position of the cursor in the console screen

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
        coords (WindowsCoordinates): The coordinates to move the cursor to.

    Returns:
        bool: True if the function succeeds, otherwise False.
    
Get the cursor info - used to get cursor visibility and width

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
        cursor_info (CONSOLE_CURSOR_INFO): CONSOLE_CURSOR_INFO ctype struct that receives information
            about the console's cursor.

    Returns:
          bool: True if the function succeeds, otherwise False.
    
Set the cursor info - used for adjusting cursor visibility and width

    Args:
        std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
        cursor_info (CONSOLE_CURSOR_INFO): CONSOLE_CURSOR_INFO ctype struct containing the new cursor info.

    Returns:
          bool: True if the function succeeds, otherwise False.
    
Sets the title of the current console window

    Args:
        title (str): The new title of the console window.

    Returns:
        bool: True if the function succeeds, otherwise False.
    
This class allows interaction with the legacy Windows Console API. It should only be used in the context
    of environments where virtual terminal processing is not available. However, if it is used in a Windows environment,
    the entire API should work.

    Args:
        file (IO[str]): The file which the Windows Console API HANDLE is retrieved from, defaults to sys.stdout.
    
Returns the current position of the cursor (0-based)

        Returns:
            WindowsCoordinates: The current cursor position.
        
Returns the current size of the console screen buffer, in character columns and rows

        Returns:
            WindowsCoordinates: The width and height of the screen as WindowsCoordinates.
        
Write text directly to the terminal without any modification of styles

        Args:
            text (str): The text to write to the console
        
Write styled text to the terminal.

        Args:
            text (str): The text to write
            style (Style): The style of the text
        
Set the position of the cursor

        Args:
            new_position (WindowsCoordinates): The WindowsCoordinates representing the new position of the cursor.
        
Erase all content on the line the cursor is currently located at
Erase all content from the cursor position to the end of that line
Erase all content from the cursor position to the start of that line
Move the cursor up a single cell
Move the cursor down a single cell
Move the cursor forward a single cell. Wrap to the next line if required.
Move cursor to the column specified by the zero-based column index, staying on the same row

        Args:
            column (int): The zero-based column index to move the cursor to.
        
Move the cursor backward a single cell. Wrap to the previous line if required.
Hide the cursor
Show the cursor
Set the title of the terminal window

        Args:
            title (str): The new title of the console window
        
Get the percentage of the character cell that is filled by the cursor

---

\
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>

A shim to write html to Jupyter notebook.
Add to an Rich renderable to make it render in Jupyter notebook.
Escape html.
Render segments to Jupyter.
Proxy for Console print.

---

An abstract base class for Rich renderables.

    Note that there is no need to extend this class, the intended use is to check if an
    object supports the Rich renderable protocol. For example::

        if isinstance(my_object, RichRenderable):
            console.print(my_object)

    
Check if this class supports the rich render protocol.

---



---



---

A thread that calls refresh() at regular intervals.
Renders an auto-updating live display of any given renderable.

    Args:
        renderable (RenderableType, optional): The renderable to live display. Defaults to displaying nothing.
        console (Console, optional): Optional Console instance. Defaults to an internal Console instance writing to stdout.
        screen (bool, optional): Enable alternate screen mode. Defaults to False.
        auto_refresh (bool, optional): Enable auto refresh. If disabled, you will need to call `refresh()` or `update()` with refresh flag. Defaults to True
        refresh_per_second (float, optional): Number of times per second to refresh the live display. Defaults to 4.
        transient (bool, optional): Clear the renderable on exit (has no effect when screen=True). Defaults to False.
        redirect_stdout (bool, optional): Enable redirection of stdout, so ``print`` may be used. Defaults to True.
        redirect_stderr (bool, optional): Enable redirection of stderr. Defaults to True.
        vertical_overflow (VerticalOverflowMethod, optional): How to handle renderable when it is too tall for the console. Defaults to "ellipsis".
        get_renderable (Callable[[], RenderableType], optional): Optional callable to get renderable. Defaults to None.
    
Check if live display has been started.
Start live rendering display.

        Args:
            refresh (bool, optional): Also refresh. Defaults to False.
        
Stop live rendering display.
Enable redirecting of stdout / stderr.
Disable redirecting of stdout / stderr.
Get the renderable that is being displayed

        Returns:
            RenderableType: Displayed renderable.
        
Update the renderable that is being displayed

        Args:
            renderable (RenderableType): New renderable to use.
            refresh (bool, optional): Refresh the display. Defaults to False.
        
Update the display of the Live Render.
Process renderables to restore cursor and display progress.
Iterate and generate a tuple with a flag for last value.

---



---

Constrain the width of a renderable to a given number of characters.

    Args:
        renderable (RenderableType): A renderable object.
        width (int, optional): The maximum width (in characters) to render. Defaults to 80.
    

---

Defines a rectangular region of the screen.

---

A renderable that inserts a control code (non printable but may move cursor).

    Args:
        *codes (str): Positional arguments are either a :class:`~rich.segment.ControlType` enum or a
            tuple of ControlType and an integer parameter
    
Ring the 'bell'.
Move cursor to 'home' position.
Move cursor relative to current position.

        Args:
            x (int): X offset.
            y (int): Y offset.

        Returns:
            ~Control: Control object.

        
Move to the given column, optionally add offset to row.

        Returns:
            x (int): absolute x (column)
            y (int): optional y offset (row)

        Returns:
            ~Control: Control object.
        
Move cursor to absolute position.

        Args:
            x (int): x offset (column)
            y (int): y offset (row)

        Returns:
            ~Control: Control object.
        
Clear the screen.
Show or hide the cursor.
Enable or disable alt screen.
Set the terminal window title

        Args:
            title (str): The new terminal window title
        
Remove control codes from text.

    Args:
        text (str): A string possibly contain control codes.

    Returns:
        str: String with control codes removed.
    
Replace control codes with their "escaped" equivalent in the given text.
    (e.g. "\b" becomes "\\b")

    Args:
        text (str): A string possibly containing control codes.

    Returns:
        str: String with control codes replaced with their escaped version.
    

---

A list subclass which renders its contents to the console.
Console render method to insert line-breaks.
A list subclass which can render to the console.
Console render method to insert line-breaks.
Justify and overflow text to a given width.

        Args:
            console (Console): Console instance.
            width (int): Number of cells available per line.
            justify (str, optional): Default justify method for text: "left", "center", "full" or "right". Defaults to "left".
            overflow (str, optional): Default overflow for text: "crop", "fold", or "ellipsis". Defaults to "fold".

        

---

A renderable for a tree structure.

    Attributes:
        ASCII_GUIDES (GuideType): Guide lines used when Console.ascii_only is True.
        TREE_GUIDES (List[GuideType, GuideType, GuideType]): Default guide lines.

    Args:
        label (RenderableType): The renderable or str for the tree label.
        style (StyleType, optional): Style of this tree. Defaults to "tree".
        guide_style (StyleType, optional): Style of the guide lines. Defaults to "tree.line".
        expanded (bool, optional): Also display children. Defaults to True.
        highlight (bool, optional): Highlight renderable (if str). Defaults to False.
        hide_root (bool, optional): Hide the root node. Defaults to False.
    
Add a child tree.

        Args:
            label (RenderableType): The renderable or str for the tree label.
            style (StyleType, optional): Style of this tree. Defaults to "tree".
            guide_style (StyleType, optional): Style of the guide lines. Defaults to "tree.line".
            expanded (bool, optional): Also display children. Defaults to True.
            highlight (Optional[bool], optional): Highlight renderable (if str). Defaults to False.

        Returns:
            Tree: A new child Tree, which may be further modified.
        
Make a Segment for a level of the guide lines.
\
class Segment(NamedTuple):
    text: str = ""
    style: Optional[Style] = None
    is_control: bool = False

\
### example.md
> Hello, World!
>
> Markdown _all_ the things


---

Get the number of cells required to display text.

    This method always caches, which may use up a lot of memory. It is recommended to use
    `cell_len` over this method.

    Args:
        text (str): Text to display.

    Returns:
        int: Get the number of cells required to display text.
    
Get the number of cells required to display text.

    Args:
        text (str): Text to display.

    Returns:
        int: Get the number of cells required to display text.
    
Get the cell size of a character.

    Args:
        character (str): A single character.

    Returns:
        int: Number of cells (0, 1 or 2) occupied by that character.
    
Set the length of a string to fit within given number of cells.
Split text into lines such that each line fits within the available (cell) width.

    Args:
        text: The text to fold such that it fits in the given width.
        width: The width available (number of cells).

    Returns:
        A list of strings such that each string in the list has cell width
        less than or equal to the available width.
    
这是对亚洲语言支持的测试。面对模棱两可的想法，拒绝猜测的诱惑。
这是对亚洲语言支持的测试。面对模棱两可的想法，拒绝猜测的诱惑。

---

A renderable that fills the terminal screen and crops excess.

    Args:
        renderable (RenderableType): Child renderable.
        style (StyleType, optional): Optional background style. Defaults to None.
    

---

Align a renderable by adding spaces if necessary.

    Args:
        renderable (RenderableType): A console renderable.
        align (AlignMethod): One of "left", "center", or "right""
        style (StyleType, optional): An optional style to apply to the background.
        vertical (Optional[VerticalAlignMethod], optional): Optional vertical align, one of "top", "middle", or "bottom". Defaults to None.
        pad (bool, optional): Pad the right with spaces. Defaults to True.
        width (int, optional): Restrict contents to given width, or None to use default width. Defaults to None.
        height (int, optional): Set height of align renderable, or None to fit to contents. Defaults to None.

    Raises:
        ValueError: if ``align`` is not one of the expected values.
    
Align a renderable to the left.
Align a renderable to the center.
Align a renderable to the right.
Vertically aligns a renderable.

    Warn:
        This class is deprecated and may be removed in a future version. Use Align class with
        `vertical="middle"`.

    Args:
        renderable (RenderableType): A renderable object.
        style (StyleType, optional): An optional style to apply to the background. Defaults to None.
    

---

A console renderable to draw a horizontal rule (line).

    Args:
        title (Union[str, Text], optional): Text to render in the rule. Defaults to "".
        characters (str, optional): Character(s) used to draw the line. Defaults to "─".
        style (StyleType, optional): Style of Rule. Defaults to "rule.line".
        end (str, optional): Character at end of Rule. defaults to "\\\\n"
        align (str, optional): How to align the title, one of "left", "center", or "right". Defaults to "center".
    

---

An error in console operation.
An error in styles.
Style was badly formatted.
No such style.
Style stack is invalid.
Object is not renderable.
Markup was badly formatted.
Error related to Live display.
Alt screen mode was required.

---

Renders a (progress) bar. Used by rich.progress.

    Args:
        total (float, optional): Number of steps in the bar. Defaults to 100. Set to None to render a pulsing animation.
        completed (float, optional): Number of steps completed. Defaults to 0.
        width (int, optional): Width of the bar, or ``None`` for maximum width. Defaults to None.
        pulse (bool, optional): Enable pulse effect. Defaults to False. Will pulse if a None total was passed.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
        animation_time (Optional[float], optional): Time in seconds to use for animation, or None to use system time.
    
Calculate percentage complete.
Get a list of segments to render a pulse animation.

        Returns:
            List[Segment]: A list of segments, one segment per character.
        
Update progress with new values.

        Args:
            completed (float): Number of steps completed.
            total (float, optional): Total number of steps, or ``None`` to not change. Defaults to None.
        
Renders the pulse animation.

        Args:
            console (Console): Console instance.
            width (int): Width in characters of pulse animation.

        Returns:
            RenderResult: [description]

        Yields:
            Iterator[Segment]: Segments to render pulse
        

---

Get the first paragraph from a docstring.
A renderable to inspect any Python Object.

    Args:
        obj (Any): An object to inspect.
        title (str, optional): Title to display over inspect result, or None use type. Defaults to None.
        help (bool, optional): Show full help text rather than just first paragraph. Defaults to False.
        methods (bool, optional): Enable inspection of callables. Defaults to False.
        docs (bool, optional): Also render doc strings. Defaults to True.
        private (bool, optional): Show private attributes (beginning with underscore). Defaults to False.
        dunder (bool, optional): Show attributes starting with double underscore. Defaults to False.
        sort (bool, optional): Sort attributes alphabetically. Defaults to True.
        all (bool, optional): Show all attributes. Defaults to False.
        value (bool, optional): Pretty print value of object. Defaults to True.
    
Make a default title.
Get a signature for a callable.
Render object.
Get attribute or any exception.

        Extract the docstring of an object, process it and returns it.
        The processing consists in cleaning up the doctring's indentation,
        taking only its 1st paragraph if `self.help` is not True,
        and escape its control codes.

        Args:
            object_ (Any): the object to get the docstring from.

        Returns:
            Optional[str]: the processed docstring, or None if no docstring was found.
        
Returns the MRO of an object's class, or of the object itself if it's a class.

    Returns the MRO of an object's class as full qualified names, or of the object itself if it's a class.

    Examples:
        `object_types_mro_as_strings(JSONDecoder)` will return `['json.decoder.JSONDecoder', 'builtins.object']`
    

    Returns `True` if the given object's class (or the object itself, if it's a class) has one of the
    fully qualified names in its MRO.
    

---

A logging handler that renders output with Rich. The time / level / message and file are displayed in columns.
    The level is color coded, and the message is syntax highlighted.

    Note:
        Be careful when enabling console markup in log messages if you have configured logging for libraries not
        under your control. If a dependency writes messages containing square brackets, it may not produce the intended output.

    Args:
        level (Union[int, str], optional): Log level. Defaults to logging.NOTSET.
        console (:class:`~rich.console.Console`, optional): Optional console instance to write logs.
            Default will use a global console instance writing to stdout.
        show_time (bool, optional): Show a column for the time. Defaults to True.
        omit_repeated_times (bool, optional): Omit repetition of the same time. Defaults to True.
        show_level (bool, optional): Show a column for the level. Defaults to True.
        show_path (bool, optional): Show the path to the original log call. Defaults to True.
        enable_link_path (bool, optional): Enable terminal link of path column to file. Defaults to True.
        highlighter (Highlighter, optional): Highlighter to style log messages, or None to use ReprHighlighter. Defaults to None.
        markup (bool, optional): Enable console markup in log messages. Defaults to False.
        rich_tracebacks (bool, optional): Enable rich tracebacks with syntax highlighting and formatting. Defaults to False.
        tracebacks_width (Optional[int], optional): Number of characters used to render tracebacks, or None for full width. Defaults to None.
        tracebacks_code_width (int, optional): Number of code characters used to render tracebacks, or None for full width. Defaults to 88.
        tracebacks_extra_lines (int, optional): Additional lines of code to render tracebacks, or None for full width. Defaults to None.
        tracebacks_theme (str, optional): Override pygments theme used in traceback.
        tracebacks_word_wrap (bool, optional): Enable word wrapping of long tracebacks lines. Defaults to True.
        tracebacks_show_locals (bool, optional): Enable display of locals in tracebacks. Defaults to False.
        tracebacks_suppress (Sequence[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.
        tracebacks_max_frames (int, optional): Optional maximum number of frames returned by traceback.
        locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to 10.
        locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
        log_time_format (Union[str, TimeFormatterCallable], optional): If ``log_time`` is enabled, either string for strftime or callable that formats the time. Defaults to "[%x %X] ".
        keywords (List[str], optional): List of words to highlight instead of ``RichHandler.KEYWORDS``.
    
Get the level name from the record.

        Args:
            record (LogRecord): LogRecord instance.

        Returns:
            Text: A tuple of the style and level name.
        
Invoked by logging.
Render message text in to Text.

        Args:
            record (LogRecord): logging Record.
            message (str): String containing log message.

        Returns:
            ConsoleRenderable: Renderable to display log message.
        
Render log for display.

        Args:
            record (LogRecord): logging Record.
            traceback (Optional[Traceback]): Traceback instance or None for no Traceback.
            message_renderable (ConsoleRenderable): Renderable (typically Text) containing log message contents.

        Returns:
            ConsoleRenderable: Renderable to display log.
        

---



---


Timer context manager, only used in debug.


print the elapsed time. (only used in debugging)

---

Size of the terminal.
The width of the console in 'cells'.
The height of the console in lines.
Options for __rich_console__ method.
Size of console.
legacy_windows: flag for legacy windows.
Minimum width of renderable.
Maximum width of renderable.
True if the target is a terminal, otherwise False.
Encoding of terminal.
Height of container (starts as terminal)
Justify value override for renderable.
Overflow value override for renderable.
Disable wrapping for text.
Highlight override for render_str.
Enable markup when rendering strings.
Check if renderables should use ascii only.
Return a copy of the options.

        Returns:
            ConsoleOptions: a copy of self.
        
Update values, return a copy.
Update just the width, return a copy.

        Args:
            width (int): New width (sets both min_width and max_width)

        Returns:
            ~ConsoleOptions: New console options instance.
        
Update the height, and return a copy.

        Args:
            height (int): New height

        Returns:
            ~ConsoleOptions: New Console options instance.
        
Return a copy of the options with height set to ``None``.

        Returns:
            ~ConsoleOptions: New console options instance.
        
Update the width and height, and return a copy.

        Args:
            width (int): New width (sets both min_width and max_width).
            height (int): New height.

        Returns:
            ~ConsoleOptions: New console options instance.
        
An object that may be 'cast' to a console renderable.
An object that supports the console protocol.
A string or any object that may be rendered by Rich.
An error in the Capture context manager.
A renderable to generate new line(s)
Render a list of lines at a given offset.
Context manager to capture the result of printing to the console.
    See :meth:`~rich.console.Console.capture` for how to use.

    Args:
        console (Console): A console instance to capture output.
    
Get the result of the capture.
A context manager to use a temporary theme. See :meth:`~rich.console.Console.use_theme` for usage.
A context manager that 'pages' content. See :meth:`~rich.console.Console.pager` for usage.
A context manager that enables an alternative screen. See :meth:`~rich.console.Console.screen` for usage.
Update the screen.

        Args:
            renderable (RenderableType, optional): Optional renderable to replace current renderable,
                or None for no change. Defaults to None.
            style: (Style, optional): Replacement style, or None for no change. Defaults to None.
        
Takes a group of renderables and returns a renderable object that renders the group.

    Args:
        renderables (Iterable[RenderableType]): An iterable of renderable objects.
        fit (bool, optional): Fit dimension of group to contents, or fill available space. Defaults to True.
    
A decorator that turns an iterable of renderables in to a group.

    Args:
        fit (bool, optional): Fit dimension of group to contents, or fill available space. Defaults to True.
    
Convert a method that returns an iterable of renderables in to a Group.
Check if we're running in a Jupyter notebook.
Thread local values for Console context.
Provides hooks in to the render process.
Called with a list of objects to render.

        This method can return a new list of renderables, or modify and return the same list.

        Args:
            renderables (List[ConsoleRenderable]): A number of renderable objects.

        Returns:
            List[ConsoleRenderable]: A replacement list of renderables.
        
Detect legacy Windows.
A high level console interface.

    Args:
        color_system (str, optional): The color system supported by your terminal,
            either ``"standard"``, ``"256"`` or ``"truecolor"``. Leave as ``"auto"`` to autodetect.
        force_terminal (Optional[bool], optional): Enable/disable terminal control codes, or None to auto-detect terminal. Defaults to None.
        force_jupyter (Optional[bool], optional): Enable/disable Jupyter rendering, or None to auto-detect Jupyter. Defaults to None.
        force_interactive (Optional[bool], optional): Enable/disable interactive mode, or None to auto detect. Defaults to None.
        soft_wrap (Optional[bool], optional): Set soft wrap default on print method. Defaults to False.
        theme (Theme, optional): An optional style theme object, or ``None`` for default theme.
        stderr (bool, optional): Use stderr rather than stdout if ``file`` is not specified. Defaults to False.
        file (IO, optional): A file object where the console should write to. Defaults to stdout.
        quiet (bool, Optional): Boolean to suppress all output. Defaults to False.
        width (int, optional): The width of the terminal. Leave as default to auto-detect width.
        height (int, optional): The height of the terminal. Leave as default to auto-detect height.
        style (StyleType, optional): Style to apply to all output, or None for no style. Defaults to None.
        no_color (Optional[bool], optional): Enabled no color mode, or None to auto detect. Defaults to None.
        tab_size (int, optional): Number of spaces used to replace a tab character. Defaults to 8.
        record (bool, optional): Boolean to enable recording of terminal output,
            required to call :meth:`export_html`, :meth:`export_svg`, and :meth:`export_text`. Defaults to False.
        markup (bool, optional): Boolean to enable :ref:`console_markup`. Defaults to True.
        emoji (bool, optional): Enable emoji code. Defaults to True.
        emoji_variant (str, optional): Optional emoji variant, either "text" or "emoji". Defaults to None.
        highlight (bool, optional): Enable automatic highlighting. Defaults to True.
        log_time (bool, optional): Boolean to enable logging of time by :meth:`log` methods. Defaults to True.
        log_path (bool, optional): Boolean to enable the logging of the caller by :meth:`log`. Defaults to True.
        log_time_format (Union[str, TimeFormatterCallable], optional): If ``log_time`` is enabled, either string for strftime or callable that formats the time. Defaults to "[%X] ".
        highlighter (HighlighterType, optional): Default highlighter.
        legacy_windows (bool, optional): Enable legacy Windows mode, or ``None`` to auto detect. Defaults to ``None``.
        safe_box (bool, optional): Restrict box options that don't render on legacy Windows.
        get_datetime (Callable[[], datetime], optional): Callable that gets the current time as a datetime.datetime object (used by Console.log),
            or None for datetime.now.
        get_time (Callable[[], time], optional): Callable that gets the current time in seconds, default uses time.monotonic.
    
Get the file object to write to.
Set a new file object.
Get a thread local buffer.
Get a thread local buffer.
Get the thread local theme stack.
Detect color system from env vars.
Enter in to a buffer context, and buffer all output.
Leave buffer context, and render content if required.
Set Live instance. Used by Live context manager.

        Args:
            live (Live): Live instance using this Console.

        Raises:
            errors.LiveError: If this Console has a Live context currently active.
        
Clear the Live instance.
Add a new render hook to the stack.

        Args:
            hook (RenderHook): Render hook instance.
        
Pop the last renderhook from the stack.
Own context manager to enter buffer context.
Exit buffer context.
Begin capturing console output. Call :meth:`end_capture` to exit capture mode and return output.
End capture mode and return captured string.

        Returns:
            str: Console output.
        
Push a new theme on to the top of the stack, replacing the styles from the previous theme.
        Generally speaking, you should call :meth:`~rich.console.Console.use_theme` to get a context manager, rather
        than calling this method directly.

        Args:
            theme (Theme): A theme instance.
            inherit (bool, optional): Inherit existing styles. Defaults to True.
        
Remove theme from top of stack, restoring previous theme.
Use a different theme for the duration of the context manager.

        Args:
            theme (Theme): Theme instance to user.
            inherit (bool, optional): Inherit existing console styles. Defaults to True.

        Returns:
            ThemeContext: [description]
        
Get color system string.

        Returns:
            Optional[str]: "standard", "256" or "truecolor".
        
Get the encoding of the console file, e.g. ``"utf-8"``.

        Returns:
            str: A standard encoding string.
        
Check if the console is writing to a terminal.

        Returns:
            bool: True if the console writing to a device capable of
                understanding escape sequences, otherwise False.
        
Detect dumb terminal.

        Returns:
            bool: True if writing to a dumb terminal, otherwise False.

        
Get default console options.
Get the size of the console.

        Returns:
            ConsoleDimensions: A named tuple containing the dimensions.
        
Set a new size for the terminal.

        Args:
            new_size (Tuple[int, int]): New width and height.
        
Get the width of the console.

        Returns:
            int: The width (in characters) of the console.
        
Set width.

        Args:
            width (int): New width.
        
Get the height of the console.

        Returns:
            int: The height (in lines) of the console.
        
Set height.

        Args:
            height (int): new height.
        
Play a 'bell' sound (if supported by the terminal).
A context manager to *capture* the result of print() or log() in a string,
        rather than writing it to the console.

        Example:
            >>> from rich.console import Console
            >>> console = Console()
            >>> with console.capture() as capture:
            ...     console.print("[bold magenta]Hello World[/]")
            >>> print(capture.get())

        Returns:
            Capture: Context manager with disables writing to the terminal.
        
A context manager to display anything printed within a "pager". The pager application
        is defined by the system and will typically support at least pressing a key to scroll.

        Args:
            pager (Pager, optional): A pager object, or None to use :class:`~rich.pager.SystemPager`. Defaults to None.
            styles (bool, optional): Show styles in pager. Defaults to False.
            links (bool, optional): Show links in pager. Defaults to False.

        Example:
            >>> from rich.console import Console
            >>> from rich.__main__ import make_test_card
            >>> console = Console()
            >>> with console.pager():
                    console.print(make_test_card())

        Returns:
            PagerContext: A context manager.
        
Write new line(s).

        Args:
            count (int, optional): Number of new lines. Defaults to 1.
        
Clear the screen.

        Args:
            home (bool, optional): Also move the cursor to 'home' position. Defaults to True.
        
Display a status and spinner.

        Args:
            status (RenderableType): A status renderable (str or Text typically).
            spinner (str, optional): Name of spinner animation (see python -m rich.spinner). Defaults to "dots".
            spinner_style (StyleType, optional): Style of spinner. Defaults to "status.spinner".
            speed (float, optional): Speed factor for spinner animation. Defaults to 1.0.
            refresh_per_second (float, optional): Number of refreshes per second. Defaults to 12.5.

        Returns:
            Status: A Status object that may be used as a context manager.
        
Show or hide the cursor.

        Args:
            show (bool, optional): Set visibility of the cursor.
        
Enables alternative screen mode.

        Note, if you enable this mode, you should ensure that is disabled before
        the application exits. See :meth:`~rich.Console.screen` for a context manager
        that handles this for you.

        Args:
            enable (bool, optional): Enable (True) or disable (False) alternate screen. Defaults to True.

        Returns:
            bool: True if the control codes were written.

        
Check if the alt screen was enabled.

        Returns:
            bool: True if the alt screen was enabled, otherwise False.
        
Set the title of the console terminal window.

        Warning: There is no means within Rich of "resetting" the window title to its
        previous value, meaning the title you set will persist even after your application
        exits.

        ``fish`` shell resets the window title before and after each command by default,
        negating this issue. Windows Terminal and command prompt will also reset the title for you.
        Most other shells and terminals, however, do not do this.

        Some terminals may require configuration changes before you can set the title.
        Some terminals may not support setting the title at all.

        Other software (including the terminal itself, the shell, custom prompts, plugins, etc.)
        may also set the terminal window title. This could result in whatever value you write
        using this method being overwritten.

        Args:
            title (str): The new title of the terminal window.

        Returns:
            bool: True if the control code to change the terminal title was
                written, otherwise False. Note that a return value of True
                does not guarantee that the window title has actually changed,
                since the feature may be unsupported/disabled in some terminals.
        
Context manager to enable and disable 'alternative screen' mode.

        Args:
            hide_cursor (bool, optional): Also hide the cursor. Defaults to False.
            style (Style, optional): Optional style for screen. Defaults to None.

        Returns:
            ~ScreenContext: Context which enables alternate screen on enter, and disables it on exit.
        
Measure a renderable. Returns a :class:`~rich.measure.Measurement` object which contains
        information regarding the number of characters required to print the renderable.

        Args:
            renderable (RenderableType): Any renderable or string.
            options (Optional[ConsoleOptions], optional): Options to use when measuring, or None
                to use default options. Defaults to None.

        Returns:
            Measurement: A measurement of the renderable.
        
Render an object in to an iterable of `Segment` instances.

        This method contains the logic for rendering objects with the console protocol.
        You are unlikely to need to use it directly, unless you are extending the library.

        Args:
            renderable (RenderableType): An object supporting the console protocol, or
                an object that may be converted to a string.
            options (ConsoleOptions, optional): An options object, or None to use self.options. Defaults to None.

        Returns:
            Iterable[Segment]: An iterable of segments that may be rendered.
        
Render objects in to a list of lines.

        The output of render_lines is useful when further formatting of rendered console text
        is required, such as the Panel class which draws a border around any renderable object.

        Args:
            renderable (RenderableType): Any object renderable in the console.
            options (Optional[ConsoleOptions], optional): Console options, or None to use self.options. Default to ``None``.
            style (Style, optional): Optional style to apply to renderables. Defaults to ``None``.
            pad (bool, optional): Pad lines shorter than render width. Defaults to ``True``.
            new_lines (bool, optional): Include "\n" characters at end of lines.

        Returns:
            List[List[Segment]]: A list of lines, where a line is a list of Segment objects.
        
Convert a string to a Text instance. This is called automatically if
        you print or log a string.

        Args:
            text (str): Text to render.
            style (Union[str, Style], optional): Style to apply to rendered text.
            justify (str, optional): Justify method: "default", "left", "center", "full", or "right". Defaults to ``None``.
            overflow (str, optional): Overflow method: "crop", "fold", or "ellipsis". Defaults to ``None``.
            emoji (Optional[bool], optional): Enable emoji, or ``None`` to use Console default.
            markup (Optional[bool], optional): Enable markup, or ``None`` to use Console default.
            highlight (Optional[bool], optional): Enable highlighting, or ``None`` to use Console default.
            highlighter (HighlighterType, optional): Optional highlighter to apply.
        Returns:
            ConsoleRenderable: Renderable object.

        
Get a Style instance by its theme name or parse a definition.

        Args:
            name (str): The name of a style or a style definition.

        Returns:
            Style: A Style object.

        Raises:
            MissingStyle: If no style could be parsed from name.

        
Combine a number of renderables and text into one renderable.

        Args:
            objects (Iterable[Any]): Anything that Rich can render.
            sep (str): String to write between print data.
            end (str): String to write at end of print data.
            justify (str, optional): One of "left", "right", "center", or "full". Defaults to ``None``.
            emoji (Optional[bool], optional): Enable emoji code, or ``None`` to use console default.
            markup (Optional[bool], optional): Enable markup, or ``None`` to use console default.
            highlight (Optional[bool], optional): Enable automatic highlighting, or ``None`` to use console default.

        Returns:
            List[ConsoleRenderable]: A list of things to render.
        
Draw a line with optional centered title.

        Args:
            title (str, optional): Text to render over the rule. Defaults to "".
            characters (str, optional): Character(s) to form the line. Defaults to "─".
            style (str, optional): Style of line. Defaults to "rule.line".
            align (str, optional): How to align the title, one of "left", "center", or "right". Defaults to "center".
        
Insert non-printing control codes.

        Args:
            control_codes (str): Control codes, such as those that may move the cursor.
        
Output to the terminal. This is a low-level way of writing to the terminal which unlike
        :meth:`~rich.console.Console.print` won't pretty print, wrap text, or apply markup, but will
        optionally apply highlighting and a basic style.

        Args:
            sep (str, optional): String to write between print data. Defaults to " ".
            end (str, optional): String to write at end of print data. Defaults to "\\\\n".
            style (Union[str, Style], optional): A style to apply to output. Defaults to None.
            highlight (Optional[bool], optional): Enable automatic highlighting, or ``None`` to use
                console default. Defaults to ``None``.
        
Print to the console.

        Args:
            objects (positional args): Objects to log to the terminal.
            sep (str, optional): String to write between print data. Defaults to " ".
            end (str, optional): String to write at end of print data. Defaults to "\\\\n".
            style (Union[str, Style], optional): A style to apply to output. Defaults to None.
            justify (str, optional): Justify method: "default", "left", "right", "center", or "full". Defaults to ``None``.
            overflow (str, optional): Overflow method: "ignore", "crop", "fold", or "ellipsis". Defaults to None.
            no_wrap (Optional[bool], optional): Disable word wrapping. Defaults to None.
            emoji (Optional[bool], optional): Enable emoji code, or ``None`` to use console default. Defaults to ``None``.
            markup (Optional[bool], optional): Enable markup, or ``None`` to use console default. Defaults to ``None``.
            highlight (Optional[bool], optional): Enable automatic highlighting, or ``None`` to use console default. Defaults to ``None``.
            width (Optional[int], optional): Width of output, or ``None`` to auto-detect. Defaults to ``None``.
            crop (Optional[bool], optional): Crop output to width of terminal. Defaults to True.
            soft_wrap (bool, optional): Enable soft wrap mode which disables word wrapping and cropping of text or ``None`` for
                Console default. Defaults to ``None``.
            new_line_start (bool, False): Insert a new line at the start if the output contains more than one line. Defaults to ``False``.
        
Pretty prints JSON. Output will be valid JSON.

        Args:
            json (Optional[str]): A string containing JSON.
            data (Any): If json is not supplied, then encode this data.
            indent (Union[None, int, str], optional): Number of spaces to indent. Defaults to 2.
            highlight (bool, optional): Enable highlighting of output: Defaults to True.
            skip_keys (bool, optional): Skip keys not of a basic type. Defaults to False.
            ensure_ascii (bool, optional): Escape all non-ascii characters. Defaults to False.
            check_circular (bool, optional): Check for circular references. Defaults to True.
            allow_nan (bool, optional): Allow NaN and Infinity values. Defaults to True.
            default (Callable, optional): A callable that converts values that can not be encoded
                in to something that can be JSON encoded. Defaults to None.
            sort_keys (bool, optional): Sort dictionary keys. Defaults to False.
        
Update the screen at a given offset.

        Args:
            renderable (RenderableType): A Rich renderable.
            region (Region, optional): Region of screen to update, or None for entire screen. Defaults to None.
            x (int, optional): x offset. Defaults to 0.
            y (int, optional): y offset. Defaults to 0.

        Raises:
            errors.NoAltScreen: If the Console isn't in alt screen mode.

        
Update lines of the screen at a given offset.

        Args:
            lines (List[List[Segment]]): Rendered lines (as produced by :meth:`~rich.Console.render_lines`).
            x (int, optional): x offset (column no). Defaults to 0.
            y (int, optional): y offset (column no). Defaults to 0.

        Raises:
            errors.NoAltScreen: If the Console isn't in alt screen mode.
        
Prints a rich render of the last exception and traceback.

        Args:
            width (Optional[int], optional): Number of characters used to render code. Defaults to 100.
            extra_lines (int, optional): Additional lines of code to render. Defaults to 3.
            theme (str, optional): Override pygments theme used in traceback
            word_wrap (bool, optional): Enable word wrapping of long lines. Defaults to False.
            show_locals (bool, optional): Enable display of local variables. Defaults to False.
            suppress (Iterable[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.
            max_frames (int): Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.
        
Get caller frame information.

        Args:
            offset (int): the caller offset within the current frame stack.
            currentframe (Callable[[], Optional[FrameType]], optional): the callable to use to
                retrieve the current frame. Defaults to ``inspect.currentframe``.

        Returns:
            Tuple[str, int, Dict[str, Any]]: A tuple containing the filename, the line number and
                the dictionary of local variables associated with the caller frame.

        Raises:
            RuntimeError: If the stack offset is invalid.
        
Log rich content to the terminal.

        Args:
            objects (positional args): Objects to log to the terminal.
            sep (str, optional): String to write between print data. Defaults to " ".
            end (str, optional): String to write at end of print data. Defaults to "\\\\n".
            style (Union[str, Style], optional): A style to apply to output. Defaults to None.
            justify (str, optional): One of "left", "right", "center", or "full". Defaults to ``None``.
            emoji (Optional[bool], optional): Enable emoji code, or ``None`` to use console default. Defaults to None.
            markup (Optional[bool], optional): Enable markup, or ``None`` to use console default. Defaults to None.
            highlight (Optional[bool], optional): Enable automatic highlighting, or ``None`` to use console default. Defaults to None.
            log_locals (bool, optional): Boolean to enable logging of locals where ``log()``
                was called. Defaults to False.
            _stack_offset (int, optional): Offset of caller from end of call stack. Defaults to 1.
        
This function is called when a `BrokenPipeError` is raised.

        This can occur when piping Textual output in Linux and macOS.
        The default implementation is to exit the app, but you could implement
        this method in a subclass to change the behavior.

        See https://docs.python.org/3/library/signal.html#note-on-sigpipe for details.
        
Check if the buffer may be rendered. Render it if it can (e.g. Console.quiet is False)
        Rendering is supported on Windows, Unix and Jupyter environments. For
        legacy Windows consoles, the win32 API is called directly.
        This method will also record what it renders if recording is enabled via Console.record.
        
Write the buffer to the output file.
Render buffered output, and clear buffer.
Displays a prompt and waits for input from the user. The prompt may contain color / style.

        It works in the same way as Python's builtin :func:`input` function and provides elaborate line editing and history features if Python's builtin :mod:`readline` module is previously loaded.

        Args:
            prompt (Union[str, Text]): Text to render in the prompt.
            markup (bool, optional): Enable console markup (requires a str prompt). Defaults to True.
            emoji (bool, optional): Enable emoji (requires a str prompt). Defaults to True.
            password: (bool, optional): Hide typed text. Defaults to False.
            stream: (TextIO, optional): Optional file to read input from (rather than stdin). Defaults to None.

        Returns:
            str: Text read from stdin.
        
Generate text from console contents (requires record=True argument in constructor).

        Args:
            clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``.
            styles (bool, optional): If ``True``, ansi escape codes will be included. ``False`` for plain text.
                Defaults to ``False``.

        Returns:
            str: String containing console contents.

        
Generate text from console and save to a given location (requires record=True argument in constructor).

        Args:
            path (str): Path to write text files.
            clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``.
            styles (bool, optional): If ``True``, ansi style codes will be included. ``False`` for plain text.
                Defaults to ``False``.

        
Generate HTML from console contents (requires record=True argument in constructor).

        Args:
            theme (TerminalTheme, optional): TerminalTheme object containing console colors.
            clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``.
            code_format (str, optional): Format string to render HTML. In addition to '{foreground}',
                '{background}', and '{code}', should contain '{stylesheet}' if inline_styles is ``False``.
            inline_styles (bool, optional): If ``True`` styles will be inlined in to spans, which makes files
                larger but easier to cut and paste markup. If ``False``, styles will be embedded in a style tag.
                Defaults to False.

        Returns:
            str: String containing console contents as HTML.
        
Generate HTML from console contents and write to a file (requires record=True argument in constructor).

        Args:
            path (str): Path to write html file.
            theme (TerminalTheme, optional): TerminalTheme object containing console colors.
            clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``.
            code_format (str, optional): Format string to render HTML. In addition to '{foreground}',
                '{background}', and '{code}', should contain '{stylesheet}' if inline_styles is ``False``.
            inline_styles (bool, optional): If ``True`` styles will be inlined in to spans, which makes files
                larger but easier to cut and paste markup. If ``False``, styles will be embedded in a style tag.
                Defaults to False.

        

        Generate an SVG from the console contents (requires record=True in Console constructor).

        Args:
            title (str, optional): The title of the tab in the output image
            theme (TerminalTheme, optional): The ``TerminalTheme`` object to use to style the terminal
            clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``
            code_format (str, optional): Format string used to generate the SVG. Rich will inject a number of variables
                into the string in order to form the final SVG output. The default template used and the variables
                injected by Rich can be found by inspecting the ``console.CONSOLE_SVG_FORMAT`` variable.
            font_aspect_ratio (float, optional): The width to height ratio of the font used in the ``code_format``
                string. Defaults to 0.61, which is the width to height ratio of Fira Code (the default font).
                If you aren't specifying a different font inside ``code_format``, you probably don't need this.
            unique_id (str, optional): unique id that is used as the prefix for various elements (CSS styles, node
                ids). If not set, this defaults to a computed value based on the recorded content.
        
Convert a Style to CSS rules for SVG.
HTML escape text and replace spaces with nbsp.
Make a tag from name, content, and attributes.
<clipPath id="{unique_id}-line-{line_no}">
    {make_tag("rect", x=0, y=offset, width=char_width * width, height=line_height + 0.25)}
            </clipPath>

            <g transform="translate(26,22)">
            <circle cx="0" cy="0" r="7" fill="#ff5f57"/>
            <circle cx="22" cy="0" r="7" fill="#febc2e"/>
            <circle cx="44" cy="0" r="7" fill="#28c840"/>
            </g>
        
Generate an SVG file from the console contents (requires record=True in Console constructor).

        Args:
            path (str): The path to write the SVG to.
            title (str, optional): The title of the tab in the output image
            theme (TerminalTheme, optional): The ``TerminalTheme`` object to use to style the terminal
            clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``
            code_format (str, optional): Format string used to generate the SVG. Rich will inject a number of variables
                into the string in order to form the final SVG output. The default template used and the variables
                injected by Rich can be found by inspecting the ``console.CONSOLE_SVG_FORMAT`` variable.
            font_aspect_ratio (float, optional): The width to height ratio of the font used in the ``code_format``
                string. Defaults to 0.61, which is the width to height ratio of Fira Code (the default font).
                If you aren't specifying a different font inside ``code_format``, you probably don't need this.
            unique_id (str, optional): unique id that is used as the prefix for various elements (CSS styles, node
                ids). If not set, this defaults to a computed value based on the recorded content.
        
Returns a unique hash for the given SVG main code.

    Args:
        svg_main_code (str): The content we're going to inject in the SVG envelope.

    Returns:
        str: a hash of the given content
    

---

A palette of available colors.
Find a color from a palette that most closely matches a given color.

        Args:
            color (Tuple[int, int, int]): RGB components in range 0 > 255.

        Returns:
            int: Index of closes matching color.
        
Get the distance to a color.

---

Print a report to the terminal with debugging information

---



---

Pick the first non-none bool or return the last value.

    Args:
        *values (bool): Any number of boolean or None values.

    Returns:
        bool: First non-none boolean.
    

---

Stores the minimum and maximum widths (in characters) required to render an object.
Minimum number of cells required to render.
Maximum number of cells required to render.
Get difference between maximum and minimum.
Get measurement that ensures that minimum <= maximum and minimum >= 0

        Returns:
            Measurement: A normalized measurement.
        
Get a RenderableWith where the widths are <= width.

        Args:
            width (int): Maximum desired width.

        Returns:
            Measurement: New Measurement object.
        
Get a RenderableWith where the widths are >= width.

        Args:
            width (int): Minimum desired width.

        Returns:
            Measurement: New Measurement object.
        
Clamp a measurement within the specified range.

        Args:
            min_width (int): Minimum desired width, or ``None`` for no minimum. Defaults to None.
            max_width (int): Maximum desired width, or ``None`` for no maximum. Defaults to None.

        Returns:
            Measurement: New Measurement object.
        
Get a measurement for a renderable.

        Args:
            console (~rich.console.Console): Console instance.
            options (~rich.console.ConsoleOptions): Console options.
            renderable (RenderableType): An object that may be rendered with Rich.

        Raises:
            errors.NotRenderableError: If the object is not renderable.

        Returns:
            Measurement: Measurement object containing range of character widths required to render the object.
        
Get a measurement that would fit a number of renderables.

    Args:
        console (~rich.console.Console): Console instance.
        options (~rich.console.ConsoleOptions): Console options.
        renderables (Iterable[RenderableType]): One or more renderable objects.

    Returns:
        Measurement: Measurement object containing range of character widths required to
            contain all given renderables.
    

---

A color theme used when exporting console content.

    Args:
        background (Tuple[int, int, int]): The background color.
        foreground (Tuple[int, int, int]): The foreground (text) color.
        normal (List[Tuple[int, int, int]]): A list of 8 normal intensity colors.
        bright (List[Tuple[int, int, int]], optional): A list of 8 bright colors, or None
            to repeat normal intensity. Defaults to None.
    

---

A plain string or a :class:`Text` instance.
A marked up region in some text.
Span start index.
Span end index.
Style associated with the span.
Split a span in to 2 from a given offset.
Move start and end by a given offset.

        Args:
            offset (int): Number of characters to add to start and end.

        Returns:
            TextSpan: A new TextSpan with adjusted position.
        
Crop the span at the given offset.

        Args:
            offset (int): A value between start and end.

        Returns:
            Span: A new (possibly smaller) span.
        
Extend the span by the given number of cells.

        Args:
            cells (int): Additional space to add to end of span.

        Returns:
            Span: A span.
        
Text with color / style.

    Args:
        text (str, optional): Default unstyled text. Defaults to "".
        style (Union[str, Style], optional): Base style for text. Defaults to "".
        justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
        overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.
        no_wrap (bool, optional): Disable text wrapping, or None for default. Defaults to None.
        end (str, optional): Character to end text with. Defaults to "\\\\n".
        tab_size (int): Number of spaces per tab, or ``None`` to use ``console.tab_size``. Defaults to None.
        spans (List[Span], optional). A list of predefined style spans. Defaults to None.
    
Get the number of cells required to render this text.
Get console markup to render this Text.

        Returns:
            str: A string potentially creating markup tags.
        
Create Text instance from markup.

        Args:
            text (str): A string containing console markup.
            style (Union[str, Style], optional): Base style for text. Defaults to "".
            emoji (bool, optional): Also render emoji code. Defaults to True.
            emoji_variant (str, optional): Optional emoji variant, either "text" or "emoji". Defaults to None.
            justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
            overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.
            end (str, optional): Character to end text with. Defaults to "\\\\n".

        Returns:
            Text: A Text instance with markup rendered.
        
Create a Text object from a string containing ANSI escape codes.

        Args:
            text (str): A string containing escape codes.
            style (Union[str, Style], optional): Base style for text. Defaults to "".
            justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
            overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.
            no_wrap (bool, optional): Disable text wrapping, or None for default. Defaults to None.
            end (str, optional): Character to end text with. Defaults to "\\\\n".
            tab_size (int): Number of spaces per tab, or ``None`` to use ``console.tab_size``. Defaults to None.
        
Construct a Text instance with a pre-applied styled. A style applied in this way won't be used
        to pad the text when it is justified.

        Args:
            text (str): A string containing console markup.
            style (Union[str, Style]): Style to apply to the text. Defaults to "".
            justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
            overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.

        Returns:
            Text: A text instance with a style applied to the entire string.
        
Construct a text instance by combining a sequence of strings with optional styles.
        The positional arguments should be either strings, or a tuple of string + style.

        Args:
            style (Union[str, Style], optional): Base style for text. Defaults to "".
            justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
            overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.
            no_wrap (bool, optional): Disable text wrapping, or None for default. Defaults to None.
            end (str, optional): Character to end text with. Defaults to "\\\\n".
            tab_size (int): Number of spaces per tab, or ``None`` to use ``console.tab_size``. Defaults to None.
            meta (Dict[str, Any], optional). Meta data to apply to text, or None for no meta data. Default to None

        Returns:
            Text: A new text instance.
        
Get the text as a single string.
Set the text to a new value.
Get a reference to the internal list of spans.
Set spans.
Return a new Text instance with copied metadata (but not the string or spans).
Return a copy of this instance.
Apply a style to the text, or a portion of the text.

        Args:
            style (Union[str, Style]): Style instance or style definition to apply.
            start (int): Start offset (negative indexing is supported). Defaults to 0.
            end (Optional[int], optional): End offset (negative indexing is supported), or None for end of text. Defaults to None.
        
Apply a style to the text, or a portion of the text. Styles will be applied before other styles already present.

        Args:
            style (Union[str, Style]): Style instance or style definition to apply.
            start (int): Start offset (negative indexing is supported). Defaults to 0.
            end (Optional[int], optional): End offset (negative indexing is supported), or None for end of text. Defaults to None.
        
Apply metadata to the text, or a portion of the text.

        Args:
            meta (Dict[str, Any]): A dict of meta information.
            start (int): Start offset (negative indexing is supported). Defaults to 0.
            end (Optional[int], optional): End offset (negative indexing is supported), or None for end of text. Defaults to None.

        
Apply event handlers (used by Textual project).

        Example:
            >>> from rich.text import Text
            >>> text = Text("hello world")
            >>> text.on(click="view.toggle('world')")

        Args:
            meta (Dict[str, Any]): Mapping of meta information.
            **handlers: Keyword args are prefixed with "@" to defined handlers.

        Returns:
            Text: Self is returned to method may be chained.
        
Remove a suffix if it exists.

        Args:
            suffix (str): Suffix to remove.
        
Get the style of a character at give offset.

        Args:
            console (~Console): Console where text will be rendered.
            offset (int): Offset in to text (negative indexing supported)

        Returns:
            Style: A Style instance.
        
Extend the Text given number of spaces where the spaces have the same style as the last character.

        Args:
            spaces (int): Number of spaces to add to the Text.
        
Highlight text with a regular expression, where group names are
        translated to styles.

        Args:
            re_highlight (Union[re.Pattern, str]): A regular expression object or string.
            style (Union[GetStyleCallable, StyleType]): Optional style to apply to whole match, or a callable
                which accepts the matched text and returns a style. Defaults to None.
            style_prefix (str, optional): Optional prefix to add to style group names.

        Returns:
            int: Number of regex matches
        
Highlight words with a style.

        Args:
            words (Iterable[str]): Words to highlight.
            style (Union[str, Style]): Style to apply.
            case_sensitive (bool, optional): Enable case sensitive matching. Defaults to True.

        Returns:
            int: Number of words highlighted.
        
Strip whitespace from end of text.
Remove whitespace beyond a certain width at the end of the text.

        Args:
            size (int): The desired size of the text.
        
Set new length of the text, clipping or padding is required.
Render the text as Segments.

        Args:
            console (Console): Console instance.
            end (Optional[str], optional): Optional end character.

        Returns:
            Iterable[Segment]: Result of render that may be written to the console.
        
Construct current style from stack.
Join text together with this instance as the separator.

        Args:
            lines (Iterable[Text]): An iterable of Text instances to join.

        Returns:
            Text: A new text instance containing join text.
        
Converts tabs to spaces.

        Args:
            tab_size (int, optional): Size of tabs. Defaults to 8.

        
Truncate text if it is longer that a given width.

        Args:
            max_width (int): Maximum number of characters in text.
            overflow (str, optional): Overflow method: "crop", "fold", or "ellipsis". Defaults to None, to use self.overflow.
            pad (bool, optional): Pad with spaces if the length is less than max_width. Defaults to False.
        
Remove or modify any spans that are over the end of the text.
Pad left and right with a given number of characters.

        Args:
            count (int): Width of padding.
            character (str): The character to pad with. Must be a string of length 1.
        
Pad the left with a given character.

        Args:
            count (int): Number of characters to pad.
            character (str, optional): Character to pad with. Defaults to " ".
        
Pad the right with a given character.

        Args:
            count (int): Number of characters to pad.
            character (str, optional): Character to pad with. Defaults to " ".
        
Align text to a given width.

        Args:
            align (AlignMethod): One of "left", "center", or "right".
            width (int): Desired width.
            character (str, optional): Character to pad with. Defaults to " ".
        
Add text with an optional style.

        Args:
            text (Union[Text, str]): A str or Text to append.
            style (str, optional): A style name. Defaults to None.

        Returns:
            Text: Returns self for chaining.
        
Append another Text instance. This method is more performant that Text.append, but
        only works for Text.

        Args:
            text (Text): The Text instance to append to this instance.

        Returns:
            Text: Returns self for chaining.
        
Append iterable of str and style. Style may be a Style instance or a str style definition.

        Args:
            tokens (Iterable[Tuple[str, Optional[StyleType]]]): An iterable of tuples containing str content and style.

        Returns:
            Text: Returns self for chaining.
        
Copy styles from another Text instance.

        Args:
            text (Text): A Text instance to copy styles from, must be the same length.
        
Split rich text in to lines, preserving styles.

        Args:
            separator (str, optional): String to split on. Defaults to "\\\\n".
            include_separator (bool, optional): Include the separator in the lines. Defaults to False.
            allow_blank (bool, optional): Return a blank line if the text ends with a separator. Defaults to False.

        Returns:
            List[RichText]: A list of rich text, one per line of the original.
        
Divide text in to a number of lines at given offsets.

        Args:
            offsets (Iterable[int]): Offsets used to divide text.

        Returns:
            Lines: New RichText instances between offsets.
        
Remove a number of characters from the end of the text.
Word wrap the text.

        Args:
            console (Console): Console instance.
            width (int): Number of cells available per line.
            justify (str, optional): Justify method: "default", "left", "center", "full", "right". Defaults to "default".
            overflow (str, optional): Overflow method: "crop", "fold", or "ellipsis". Defaults to None.
            tab_size (int, optional): Default tab size. Defaults to 8.
            no_wrap (bool, optional): Disable wrapping, Defaults to False.

        Returns:
            Lines: Number of lines.
        
Fit the text in to given width by chopping in to lines.

        Args:
            width (int): Maximum characters in a line.

        Returns:
            Lines: Lines container.
        
Auto-detect indentation of code.

        Returns:
            int: Number of spaces used to indent code.
        
Adds indent guide lines to text.

        Args:
            indent_size (Optional[int]): Size of indentation, or None to auto detect. Defaults to None.
            character (str, optional): Character to use for indentation. Defaults to "│".
            style (Union[Style, str], optional): Style of indent guides.

        Returns:
            Text: New text with indentation guides.
        
\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n

---

Non-printable control codes which typically translate to ANSI codes.
A piece of text with associated style. Segments are produced by the Console render process and
    are ultimately converted in to strings to be written to the terminal.

    Args:
        text (str): A piece of text.
        style (:class:`~rich.style.Style`, optional): An optional style to apply to the text.
        control (Tuple[ControlCode], optional): Optional sequence of control codes.

    Attributes:
        cell_length (int): The cell length of this Segment.
    
The number of terminal cells required to display self.text.

        Returns:
            int: A number of cells.
        
Check if the segment contains text.
Check if the segment contains control codes.
Split a segment in to two at a given cell position.

        Note that splitting a double-width character, may result in that character turning
        into two spaces.

        Args:
            segment (Segment): A segment to split.
            cut (int): A cell position to cut on.

        Returns:
            A tuple of two segments.
        
Split segment in to two segments at the specified column.

        If the cut point falls in the middle of a 2-cell wide character then it is replaced
        by two spaces, to preserve the display width of the parent segment.

        Args:
            cut (int): Offset within the segment to cut.

        Returns:
            Tuple[Segment, Segment]: Two segments.
        
Make a new line segment.
Apply style(s) to an iterable of segments.

        Returns an iterable of segments where the style is replaced by ``style + segment.style + post_style``.

        Args:
            segments (Iterable[Segment]): Segments to process.
            style (Style, optional): Base style. Defaults to None.
            post_style (Style, optional): Style to apply on top of segment style. Defaults to None.

        Returns:
            Iterable[Segments]: A new iterable of segments (possibly the same iterable).
        
Filter segments by ``is_control`` attribute.

        Args:
            segments (Iterable[Segment]): An iterable of Segment instances.
            is_control (bool, optional): is_control flag to match in search.

        Returns:
            Iterable[Segment]: And iterable of Segment instances.

        
Split a sequence of segments in to a list of lines.

        Args:
            segments (Iterable[Segment]): Segments potentially containing line feeds.

        Yields:
            Iterable[List[Segment]]: Iterable of segment lists, one per line.
        
Split segments in to lines, and crop lines greater than a given length.

        Args:
            segments (Iterable[Segment]): An iterable of segments, probably
                generated from console.render.
            length (int): Desired line length.
            style (Style, optional): Style to use for any padding.
            pad (bool): Enable padding of lines that are less than `length`.

        Returns:
            Iterable[List[Segment]]: An iterable of lines of segments.
        
Adjust a line to a given width (cropping or padding as required).

        Args:
            segments (Iterable[Segment]): A list of segments in a single line.
            length (int): The desired width of the line.
            style (Style, optional): The style of padding if used (space on the end). Defaults to None.
            pad (bool, optional): Pad lines with spaces if they are shorter than `length`. Defaults to True.

        Returns:
            List[Segment]: A line of segments with the desired length.
        
Get the length of list of segments.

        Args:
            line (List[Segment]): A line encoded as a list of Segments (assumes no '\\\\n' characters),

        Returns:
            int: The length of the line.
        
Get the shape (enclosing rectangle) of a list of lines.

        Args:
            lines (List[List[Segment]]): A list of lines (no '\\\\n' characters).

        Returns:
            Tuple[int, int]: Width and height in characters.
        
Set the shape of a list of lines (enclosing rectangle).

        Args:
            lines (List[List[Segment]]): A list of lines.
            width (int): Desired width.
            height (int, optional): Desired height or None for no change.
            style (Style, optional): Style of any padding added.
            new_lines (bool, optional): Padded lines should include "\n". Defaults to False.

        Returns:
            List[List[Segment]]: New list of lines.
        
Aligns lines to top (adds extra lines to bottom as required).

        Args:
            lines (List[List[Segment]]): A list of lines.
            width (int): Desired width.
            height (int, optional): Desired height or None for no change.
            style (Style): Style of any padding added.
            new_lines (bool, optional): Padded lines should include "\n". Defaults to False.

        Returns:
            List[List[Segment]]: New list of lines.
        
Aligns render to bottom (adds extra lines above as required).

        Args:
            lines (List[List[Segment]]): A list of lines.
            width (int): Desired width.
            height (int, optional): Desired height or None for no change.
            style (Style): Style of any padding added. Defaults to None.
            new_lines (bool, optional): Padded lines should include "\n". Defaults to False.

        Returns:
            List[List[Segment]]: New list of lines.
        
Aligns lines to middle (adds extra lines to above and below as required).

        Args:
            lines (List[List[Segment]]): A list of lines.
            width (int): Desired width.
            height (int, optional): Desired height or None for no change.
            style (Style): Style of any padding added.
            new_lines (bool, optional): Padded lines should include "\n". Defaults to False.

        Returns:
            List[List[Segment]]: New list of lines.
        
Simplify an iterable of segments by combining contiguous segments with the same style.

        Args:
            segments (Iterable[Segment]): An iterable of segments.

        Returns:
            Iterable[Segment]: A possibly smaller iterable of segments that will render the same way.
        
Remove all links from an iterable of styles.

        Args:
            segments (Iterable[Segment]): An iterable segments.

        Yields:
            Segment: Segments with link removed.
        
Remove all styles from an iterable of segments.

        Args:
            segments (Iterable[Segment]): An iterable segments.

        Yields:
            Segment: Segments with styles replace with None
        
Remove all color from an iterable of segments.

        Args:
            segments (Iterable[Segment]): An iterable segments.

        Yields:
            Segment: Segments with colorless style.
        
Divides an iterable of segments in to portions.

        Args:
            cuts (Iterable[int]): Cell positions where to divide.

        Yields:
            [Iterable[List[Segment]]]: An iterable of Segments in List.
        
A simple renderable to render an iterable of segments. This class may be useful if
    you want to print segments outside of a __rich_console__ method.

    Args:
        segments (Iterable[Segment]): An iterable of segments.
        new_lines (bool, optional): Add new lines between segments. Defaults to False.
    
A simple renderable containing a number of lines of segments. May be used as an intermediate
        in rendering process.

        Args:
            lines (Iterable[List[Segment]]): Lists of segments forming lines.
            new_lines (bool, optional): Insert new lines after each line. Defaults to False.
        
from rich.console import Console
console = Console()
text = Text.from_markup("Hello, [bold magenta]World[/]!")
console.print(text)

---



---

A spinner animation.

    Args:
        name (str): Name of spinner (run python -m rich.spinner).
        text (RenderableType, optional): A renderable to display at the right of the spinner (str or Text typically). Defaults to "".
        style (StyleType, optional): Style for spinner animation. Defaults to None.
        speed (float, optional): Speed factor for animation. Defaults to 1.0.

    Raises:
        KeyError: If name isn't one of the supported spinner animations.
    
Render the spinner for a given time.

        Args:
            time (float): Time in seconds.

        Returns:
            RenderableType: A renderable containing animation frame.
        
Updates attributes of a spinner after it has been started.

        Args:
            text (RenderableType, optional): A renderable to display at the right of the spinner (str or Text typically). Defaults to "".
            style (StyleType, optional): Style for spinner animation. Defaults to None.
            speed (float, optional): Speed factor for animation. Defaults to None.
        

---

Combine a number of regexes in to a single regex.

    Returns:
        str: New regex with all regexes ORed together.
    
Abstract base class for highlighters.
Highlight a str or Text instance.

        Args:
            text (Union[str, ~Text]): Text to highlight.

        Raises:
            TypeError: If not called with text or str.

        Returns:
            Text: A test instance with highlighting applied.
        
Apply highlighting in place to text.

        Args:
            text (~Text): A text object highlight.
        
A highlighter object that doesn't highlight.

    May be used to disable highlighting entirely.

    
Nothing to do
Applies highlighting from a list of regular expressions.
Highlight :class:`rich.text.Text` using regular expressions.

        Args:
            text (~Text): Text to highlighted.

        
Highlights the text typically produced from ``__repr__`` methods.
Highlights JSON
Highlights the ISO8601 date time strings.
    Regex reference: https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s07.html
    

---

Functions for reporting filesizes. Borrowed from https://github.com/PyFilesystem/pyfilesystem2

The functions declared in this module should cover the different
use cases needed to generate a string representation of a file size
using several different units. Since there are many standards regarding
file size units, three different functions have been implemented.

See Also:
    * `Wikipedia: Binary prefix <https://en.wikipedia.org/wiki/Binary_prefix>`_


Pick a suffix and base for the given size.
Convert a filesize in to a string (powers of 1000, SI prefixes).

    In this convention, ``1000 B = 1 kB``.

    This is typically the format used to advertise the storage
    capacity of USB flash drives and the like (*256 MB* meaning
    actually a storage capacity of more than *256 000 000 B*),
    or used by **Mac OS X** since v10.6 to report file sizes.

    Arguments:
        int (size): A file size.
        int (precision): The number of decimal places to include (default = 1).
        str (separator): The string to separate the value from the units (default = " ").

    Returns:
        `str`: A string containing a abbreviated file size and units.

    Example:
        >>> filesize.decimal(30000)
        '30.0 kB'
        >>> filesize.decimal(30000, precision=2, separator="")
        '30.00kB'

    

---

Windows features available.
The console supports VT codes.
The console supports truecolor.
Get windows console features.

        Returns:
            WindowsConsoleFeatures: An instance of WindowsConsoleFeatures.
        

---



---

Wraps a file (e.g. sys.stdout) and redirects writes to a console.
Get proxied file.

---

Rich text and beautiful formatting in the terminal.
Get a global :class:`~rich.console.Console` instance. This function is used when Rich requires a Console,
    and hasn't been explicitly given one.

    Returns:
        Console: A console instance.
    
Reconfigures the global console by replacing it with another.

    Args:
        *args (Any): Positional arguments for the replacement :class:`~rich.console.Console`.
        **kwargs (Any): Keyword arguments for the replacement :class:`~rich.console.Console`.
    
Print object(s) supplied via positional arguments.
    This function has an identical signature to the built-in print.
    For more advanced features, see the :class:`~rich.console.Console` class.

    Args:
        sep (str, optional): Separator between printed objects. Defaults to " ".
        end (str, optional): Character to write at end of output. Defaults to "\\n".
        file (IO[str], optional): File to write to, or None for stdout. Defaults to None.
        flush (bool, optional): Has no effect as Rich always flushes output. Defaults to False.

    
Pretty prints JSON. Output will be valid JSON.

    Args:
        json (str): A string containing JSON.
        data (Any): If json is not supplied, then encode this data.
        indent (int, optional): Number of spaces to indent. Defaults to 2.
        highlight (bool, optional): Enable highlighting of output: Defaults to True.
        skip_keys (bool, optional): Skip keys not of a basic type. Defaults to False.
        ensure_ascii (bool, optional): Escape all non-ascii characters. Defaults to False.
        check_circular (bool, optional): Check for circular references. Defaults to True.
        allow_nan (bool, optional): Allow NaN and Infinity values. Defaults to True.
        default (Callable, optional): A callable that converts values that can not be encoded
            in to something that can be JSON encoded. Defaults to None.
        sort_keys (bool, optional): Sort dictionary keys. Defaults to False.
    
Inspect any Python object.

    * inspect(<OBJECT>) to see summarized info.
    * inspect(<OBJECT>, methods=True) to see methods.
    * inspect(<OBJECT>, help=True) to see full (non-abbreviated) help.
    * inspect(<OBJECT>, private=True) to see private attributes (single underscore).
    * inspect(<OBJECT>, dunder=True) to see attributes beginning with double underscore.
    * inspect(<OBJECT>, all=True) to see all attributes.

    Args:
        obj (Any): An object to inspect.
        title (str, optional): Title to display over inspect result, or None use type. Defaults to None.
        help (bool, optional): Show full help text rather than just first paragraph. Defaults to False.
        methods (bool, optional): Enable inspection of callables. Defaults to False.
        docs (bool, optional): Also render doc strings. Defaults to True.
        private (bool, optional): Show private attributes (beginning with underscore). Defaults to False.
        dunder (bool, optional): Show attributes starting with double underscore. Defaults to False.
        sort (bool, optional): Sort attributes alphabetically. Defaults to True.
        all (bool, optional): Show all attributes. Defaults to False.
        value (bool, optional): Pretty print value. Defaults to True.
    

---

The red, green, and blue components of a color.
Red component in 0 to 255 range.
Green component in 0 to 255 range.
Blue component in 0 to 255 range.
get the color triplet in CSS style.
The color in RGB format.

        Returns:
            str: An rgb color, e.g. ``"rgb(100,23,255)"``.
        
Convert components into floats between 0 and 1.

        Returns:
            Tuple[float, float, float]: A tuple of three normalized colour components.
        

---

Displays a status indicator with a 'spinner' animation.

    Args:
        status (RenderableType): A status renderable (str or Text typically).
        console (Console, optional): Console instance to use, or None for global console. Defaults to None.
        spinner (str, optional): Name of spinner animation (see python -m rich.spinner). Defaults to "dots".
        spinner_style (StyleType, optional): Style of spinner. Defaults to "status.spinner".
        speed (float, optional): Speed factor for spinner animation. Defaults to 1.0.
        refresh_per_second (float, optional): Number of refreshes per second. Defaults to 12.5.
    
Get the Console used by the Status objects.
Update status.

        Args:
            status (Optional[RenderableType], optional): New status renderable or None for no change. Defaults to None.
            spinner (Optional[str], optional): New spinner or None for no change. Defaults to None.
            spinner_style (Optional[StyleType], optional): New spinner style or None for no change. Defaults to None.
            speed (Optional[float], optional): Speed factor for spinner animation or None for no change. Defaults to None.
        
Start the status animation.
Stop the spinner animation.

---

Yields each word from the text as a tuple
    containing (start_index, end_index, word). A "word" in this context may
    include the actual word and any whitespace to the right.
    
Given a string of text, and a width (measured in cells), return a list
    of cell offsets which the string should be split at in order for it to fit
    within the given width.

    Args:
        text: The text to examine.
        width: The available cell width.
        fold: If True, words longer than `width` will be folded onto a new line.

    Returns:
        A list of indices to break the line at.
    

---

Get a renderable that demonstrates a number of features.
Word wrap text. Justify [green]left[/], [yellow]center[/], [blue]right[/] or [red]full[/].\n
Iterate and generate a tuple with a flag for last value.
\
# Markdown

Supports much of the *markdown* __syntax__!

- Headers
- Basic formatting: **bold**, *italic*, `code`
- Block quotes
- Lists, and more...
    
Progress bars, columns, styled logging handler, tracebacks, etc...
\
We hope you enjoy using Rich!

Rich is maintained with [red]:heart:[/] by [link=https://www.textualize.io]Textualize.io[/]

- Will McGugan

---



---

Yield start and end positions per line.

    Args:
        start: Start position.
        end: End position.

    Returns:
        Iterable of (LINE, COLUMN1, COLUMN2).
    
Install a rich traceback handler.

    Once installed, any tracebacks will be printed with syntax highlighting and rich formatting.


    Args:
        console (Optional[Console], optional): Console to write exception to. Default uses internal Console instance.
        width (Optional[int], optional): Width (in characters) of traceback. Defaults to 100.
        code_width (Optional[int], optional): Code width (in characters) of traceback. Defaults to 88.
        extra_lines (int, optional): Extra lines of code. Defaults to 3.
        theme (Optional[str], optional): Pygments theme to use in traceback. Defaults to ``None`` which will pick
            a theme appropriate for the platform.
        word_wrap (bool, optional): Enable word wrapping of long lines. Defaults to False.
        show_locals (bool, optional): Enable display of local variables. Defaults to False.
        locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to 10.
        locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
        locals_hide_dunder (bool, optional): Hide locals prefixed with double underscore. Defaults to True.
        locals_hide_sunder (bool, optional): Hide locals prefixed with single underscore. Defaults to False.
        indent_guides (bool, optional): Enable indent guides in code and locals. Defaults to True.
        suppress (Sequence[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.

    Returns:
        Callable: The previous exception handler that was replaced.

    
wrap the default ip.showtraceback to store info for ip._showtraceback
Internally called traceback from ip._showtraceback
A Console renderable that renders a traceback.

    Args:
        trace (Trace, optional): A `Trace` object produced from `extract`. Defaults to None, which uses
            the last exception.
        width (Optional[int], optional): Number of characters used to traceback. Defaults to 100.
        code_width (Optional[int], optional): Number of code characters used to traceback. Defaults to 88.
        extra_lines (int, optional): Additional lines of code to render. Defaults to 3.
        theme (str, optional): Override pygments theme used in traceback.
        word_wrap (bool, optional): Enable word wrapping of long lines. Defaults to False.
        show_locals (bool, optional): Enable display of local variables. Defaults to False.
        indent_guides (bool, optional): Enable indent guides in code and locals. Defaults to True.
        locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to 10.
        locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
        locals_hide_dunder (bool, optional): Hide locals prefixed with double underscore. Defaults to True.
        locals_hide_sunder (bool, optional): Hide locals prefixed with single underscore. Defaults to False.
        suppress (Sequence[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.
        max_frames (int): Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.

    
Create a traceback from exception info

        Args:
            exc_type (Type[BaseException]): Exception type.
            exc_value (BaseException): Exception value.
            traceback (TracebackType): Python Traceback object.
            width (Optional[int], optional): Number of characters used to traceback. Defaults to 100.
            code_width (Optional[int], optional): Number of code characters used to traceback. Defaults to 88.
            extra_lines (int, optional): Additional lines of code to render. Defaults to 3.
            theme (str, optional): Override pygments theme used in traceback.
            word_wrap (bool, optional): Enable word wrapping of long lines. Defaults to False.
            show_locals (bool, optional): Enable display of local variables. Defaults to False.
            indent_guides (bool, optional): Enable indent guides in code and locals. Defaults to True.
            locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
                Defaults to 10.
            locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
            locals_hide_dunder (bool, optional): Hide locals prefixed with double underscore. Defaults to True.
            locals_hide_sunder (bool, optional): Hide locals prefixed with single underscore. Defaults to False.
            suppress (Iterable[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.
            max_frames (int): Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.

        Returns:
            Traceback: A Traceback instance that may be printed.
        
Extract traceback information.

        Args:
            exc_type (Type[BaseException]): Exception type.
            exc_value (BaseException): Exception value.
            traceback (TracebackType): Python Traceback object.
            show_locals (bool, optional): Enable display of local variables. Defaults to False.
            locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
                Defaults to 10.
            locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
            locals_hide_dunder (bool, optional): Hide locals prefixed with double underscore. Defaults to True.
            locals_hide_sunder (bool, optional): Hide locals prefixed with single underscore. Defaults to False.

        Returns:
            Trace: A Trace instance which you can use to construct a `Traceback`.
        
Don't allow exceptions from __str__ to propagate.
Extract locals from an iterator of key pairs.

---

Renders a solid block bar.

    Args:
        size (float): Value for the end of the bar.
        begin (float): Begin point (between 0 and size, inclusive).
        end (float): End point (between 0 and size, inclusive).
        width (int, optional): Width of the bar, or ``None`` for maximum width. Defaults to None.
        color (Union[Color, str], optional): Color of the bar. Defaults to "default".
        bgcolor (Union[Color, str], optional): Color of bar background. Defaults to "default".
    

---

aihwerij235234ljsdnp34ksodfipwoe234234jlskjdf
Check if an object may be rendered by Rich.
Cast an object to a renderable by calling __rich__ if present.

    Args:
        renderable (object): A potentially renderable object

    Returns:
        object: The result of recursively calling __rich__.
    

---


Spinners are from:
* cli-spinners:
    MIT License
    Copyright (c) Sindre Sorhus <sindresorhus@gmail.com> (sindresorhus.com)
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:
    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
    INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
    PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
    FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
    IN THE SOFTWARE.


---

An individual layout render.
Layout related error.
Requested splitter does not exist.
An internal renderable used as a Layout placeholder.
Base class for a splitter.
Get the icon (emoji) used in layout.tree
Divide a region amongst several child layouts.

        Args:
            children (Sequence(Layout)): A number of child layouts.
            region (Region): A rectangular region to divide.
        
Split a layout region in to rows.
Split a layout region in to columns.
A renderable to divide a fixed height in to rows or columns.

    Args:
        renderable (RenderableType, optional): Renderable content, or None for placeholder. Defaults to None.
        name (str, optional): Optional identifier for Layout. Defaults to None.
        size (int, optional): Optional fixed size of layout. Defaults to None.
        minimum_size (int, optional): Minimum size of layout. Defaults to 1.
        ratio (int, optional): Optional ratio for flexible layout. Defaults to 1.
        visible (bool, optional): Visibility of layout. Defaults to True.
    
Layout renderable.
Gets (visible) layout children.
Get a map of the last render.
Get a named layout, or None if it doesn't exist.

        Args:
            name (str): Name of layout.

        Returns:
            Optional[Layout]: Layout instance or None if no layout was found.
        
Get a tree renderable to show layout structure.
Split the layout in to multiple sub-layouts.

        Args:
            *layouts (Layout): Positional arguments should be (sub) Layout instances.
            splitter (Union[Splitter, str]): Splitter instance or name of splitter.
        
Add a new layout(s) to existing split.

        Args:
            *layouts (Union[Layout, RenderableType]): Positional arguments should be renderables or (sub) Layout instances.

        
Split the layout in to a row (layouts side by side).

        Args:
            *layouts (Layout): Positional arguments should be (sub) Layout instances.
        
Split the layout in to a column (layouts stacked on top of each other).

        Args:
            *layouts (Layout): Positional arguments should be (sub) Layout instances.
        
Reset splits to initial state.
Update renderable.

        Args:
            renderable (RenderableType): New renderable object.
        
Refresh a sub-layout.

        Args:
            console (Console): Console instance where Layout is to be rendered.
            layout_name (str): Name of layout.
        
Create a dict that maps layout on to Region.
Render the sub_layouts.

        Args:
            console (Console): Console instance.
            options (ConsoleOptions): Console options.

        Returns:
            RenderMap: A dict that maps Layout on to a tuple of Region, lines
        

---

\
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{stylesheet}
body {{
    color: {foreground};
    background-color: {background};
}}
</style>
</head>
<body>
    <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code style="font-family:inherit">{code}</code></pre>
</body>
</html>

\
<svg class="rich-terminal" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <!-- Generated with Rich https://www.textualize.io -->
    <style>

    @font-face {{
        font-family: "Fira Code";
        src: local("FiraCode-Regular"),
                url("https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff2/FiraCode-Regular.woff2") format("woff2"),
                url("https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff/FiraCode-Regular.woff") format("woff");
        font-style: normal;
        font-weight: 400;
    }}
    @font-face {{
        font-family: "Fira Code";
        src: local("FiraCode-Bold"),
                url("https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff2/FiraCode-Bold.woff2") format("woff2"),
                url("https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff/FiraCode-Bold.woff") format("woff");
        font-style: bold;
        font-weight: 700;
    }}

    .{unique_id}-matrix {{
        font-family: Fira Code, monospace;
        font-size: {char_height}px;
        line-height: {line_height}px;
        font-variant-east-asian: full-width;
    }}

    .{unique_id}-title {{
        font-size: 18px;
        font-weight: bold;
        font-family: arial;
    }}

    {styles}
    </style>

    <defs>
    <clipPath id="{unique_id}-clip-terminal">
      <rect x="0" y="0" width="{terminal_width}" height="{terminal_height}" />
    </clipPath>
    {lines}
    </defs>

    {chrome}
    <g transform="translate({terminal_x}, {terminal_y})" clip-path="url(#{unique_id}-clip-terminal)">
    {backgrounds}
    <g class="{unique_id}-matrix">
    {matrix}
    </g>
    </g>
</svg>


---

A small shim over builtin list.
Get top of stack.
Push an item on to the stack (append in stack nomenclature).

---

A console renderable that draws a border around its contents.

    Example:
        >>> console.print(Panel("Hello, World!"))

    Args:
        renderable (RenderableType): A console renderable object.
        box (Box): A Box instance that defines the look of the border (see :ref:`appendix_box`. Defaults to box.ROUNDED.
        title (Optional[TextType], optional): Optional title displayed in panel header. Defaults to None.
        title_align (AlignMethod, optional): Alignment of title. Defaults to "center".
        subtitle (Optional[TextType], optional): Optional subtitle displayed in panel footer. Defaults to None.
        subtitle_align (AlignMethod, optional): Alignment of subtitle. Defaults to "center".
        safe_box (bool, optional): Disable box characters that don't display on windows legacy terminal with *raster* fonts. Defaults to True.
        expand (bool, optional): If True the panel will stretch to fill the console width, otherwise it will be sized to fit the contents. Defaults to True.
        style (str, optional): The style of the panel (border and contents). Defaults to "none".
        border_style (str, optional): The style of the border. Defaults to "none".
        width (Optional[int], optional): Optional width of panel. Defaults to None to auto-detect.
        height (Optional[int], optional): Optional height of panel. Defaults to None to auto-detect.
        padding (Optional[PaddingDimensions]): Optional padding around renderable. Defaults to 0.
        highlight (bool, optional): Enable automatic highlighting of panel title (if str). Defaults to False.
    
An alternative constructor that sets expand=False.
Gets new aligned text.

            Args:
                text (Text): Title or subtitle text.
                width (int): Desired width.
                align (str): Alignment.
                character (str): Character for alignment.
                style (Style): Border style

            Returns:
                Text: New text instance
            

---

Get fileno() from a file, accounting for poorly implemented file-like objects.

    Args:
        file_like (IO): A file-like object.

    Returns:
        int | None: The result of fileno if available, or None if operation failed.
    

---

A container for style information, used by :class:`~rich.console.Console`.

    Args:
        styles (Dict[str, Style], optional): A mapping of style names on to styles. Defaults to None for a theme with no styles.
        inherit (bool, optional): Inherit default styles. Defaults to True.
    
Get contents of a config file for this theme.
Load a theme from a text mode file.

        Args:
            config_file (IO[str]): An open conf file.
            source (str, optional): The filename of the open file. Defaults to None.
            inherit (bool, optional): Inherit default styles. Defaults to True.

        Returns:
            Theme: A New theme instance.
        
Read a theme from a path.

        Args:
            path (str): Path to a config file readable by Python configparser module.
            inherit (bool, optional): Inherit default styles. Defaults to True.
            encoding (str, optional): Encoding of the config file. Defaults to None.

        Returns:
            Theme: A new theme instance.
        
Base exception for errors related to the theme stack.
A stack of themes.

    Args:
        theme (Theme): A theme instance
    
Push a theme on the top of the stack.

        Args:
            theme (Theme): A Theme instance.
            inherit (boolean, optional): Inherit styles from current top of stack.
        
Pop (and discard) the top-most theme.

---


Package resource API
--------------------

A resource is a logical file contained within a package, or a logical
subdirectory thereof.  The package resource API expects resource names
to have their path parts separated with ``/``, *not* whatever the local
path separator is.  Do not use os.path operations to manipulate resource
names being passed into the API.

The package resource API is designed to work with normal filesystem packages,
.egg files, and unpacked .egg files.  It can also work in a limited way with
.zip files and with custom PEP 302 loaders that support the ``get_data()``
method.

This module is deprecated. Users are directed to :mod:`importlib.resources`,
:mod:`importlib.metadata` and :pypi:`packaging` instead.


    Used when there is an issue with a version or specifier not complying with
    PEP 440.
    
Return this platform's maximum compatible version.

    distutils.util.get_platform() normally reports the minimum version
    of macOS that would be required to *use* extensions produced by
    distutils.  But what we want when checking compatibility is to know the
    version of macOS that we are *running*.  To allow usage of packages that
    explicitly require a newer version of macOS, we must also know the
    current version of the OS.

    If this condition occurs for any other platform with a version in its
    platform strings, this function should be extended accordingly.
    
Abstract base for dependency resolution errors

    An already-installed version conflicts with the requested version.

    Should be initialized with the installed Distribution and the requested
    Requirement.
    

        If required_by is non-empty, return a version of self that is a
        ContextualVersionConflict.
        

    A VersionConflict that accepts a third parameter, the set of the
    requirements that required the installed Distribution.
    
A requested distribution was not found
Distribution doesn't have an "extra feature" of the given name
Register `provider_factory` to make providers for `loader_type`

    `loader_type` is the type or class of a PEP 302 ``module.__loader__``,
    and `provider_factory` is a function that, passed a *module* object,
    returns an ``IResourceProvider`` for that module.
    
Return an IResourceProvider for the named module or requirement
Return this platform's string for platform-specific distributions

    XXX Currently this is the same as ``distutils.util.get_platform()``, but it
    needs some hacks for Linux and macOS.
    
Can code for the `provided` platform run on the `required` platform?

    Returns true if either platform is ``None``, or the platforms are equal.

    XXX Needs compatibility checks for Linux and other unixy OSes.
    
Return a current distribution object for a Requirement or string
Return `name` entry point of `group` for `dist` or raise ImportError
Return the entry point map for `group`, or the full entry map
Return the EntryPoint object for `group`+`name`, or ``None``
Does the package's distribution contain the named metadata?
The named metadata resource as a string
Yield named metadata resource as list of non-blank non-comment lines

        Leading and trailing whitespace is stripped from each line, and lines
        with ``#`` as the first non-blank character are omitted.
Is the named metadata a directory?  (like ``os.path.isdir()``)
List of metadata names in the directory (like ``os.listdir()``)
Execute the named script in the supplied namespace dictionary
An object that provides access to package resources
Return a true filesystem path for `resource_name`

        `manager` must be a ``ResourceManager``
Return a readable file-like object for `resource_name`

        `manager` must be a ``ResourceManager``
Return the contents of `resource_name` as :obj:`bytes`

        `manager` must be a ``ResourceManager``
Does the package contain the named resource?
Is the named resource a directory?  (like ``os.path.isdir()``)
List of resource names in the directory (like ``os.listdir()``)
A collection of active distributions on sys.path (or a similar list)
Create working set from list of path entries (default=sys.path)

        Prepare the master working set.
        

        Build a working set from a requirement spec. Rewrites sys.path.
        
Add a path item to ``.entries``, finding any distributions on it

        ``find_distributions(entry, True)`` is used to find distributions
        corresponding to the path entry, and they are added.  `entry` is
        always appended to ``.entries``, even if it is already present.
        (This is because ``sys.path`` can contain the same value more than
        once, and the ``.entries`` of the ``sys.path`` WorkingSet should always
        equal ``sys.path``.)
        
True if `dist` is the active distribution for its project
Find a distribution matching requirement `req`

        If there is an active distribution for the requested project, this
        returns it as long as it meets the version requirement specified by
        `req`.  But, if there is an active distribution for the project and it
        does *not* meet the `req` requirement, ``VersionConflict`` is raised.
        If there is no active distribution for the requested project, ``None``
        is returned.
        
Yield entry point objects from `group` matching `name`

        If `name` is None, yields all entry points in `group` from all
        distributions in the working set, otherwise only ones matching
        both `group` and `name` are yielded (in distribution order).
        
Locate distribution for `requires` and run `script_name` script
Yield distributions for non-duplicate projects in the working set

        The yield order is the order in which the items' path entries were
        added to the working set.
        
Add `dist` to working set, associated with `entry`

        If `entry` is unspecified, it defaults to the ``.location`` of `dist`.
        On exit from this routine, `entry` is added to the end of the working
        set's ``.entries`` (if it wasn't already present).

        `dist` is only added to the working set if it's for a project that
        doesn't already have a distribution in the set, unless `replace=True`.
        If it's added, any callbacks registered with the ``subscribe()`` method
        will be called.
        
List all distributions needed to (recursively) meet `requirements`

        `requirements` must be a sequence of ``Requirement`` objects.  `env`,
        if supplied, should be an ``Environment`` instance.  If
        not supplied, it defaults to all distributions available within any
        entry or distribution in the working set.  `installer`, if supplied,
        will be invoked with each requirement that cannot be met by an
        already-installed distribution; it should return a ``Distribution`` or
        ``None``.

        Unless `replace_conflicting=True`, raises a VersionConflict exception
        if
        any requirements are found on the path that have the correct name but
        the wrong version.  Otherwise, if an `installer` is supplied it will be
        invoked to obtain the correct version of the requirement and activate
        it.

        `extras` is a list of the extras to be used with these requirements.
        This is important because extra requirements may look like `my_req;
        extra = "my_extra"`, which would otherwise be interpreted as a purely
        optional requirement.  Instead, we want to be able to assert that these
        requirements are truly required.
        
Find all activatable distributions in `plugin_env`

        Example usage::

            distributions, errors = working_set.find_plugins(
                Environment(plugin_dirlist)
            )
            # add plugins+libs to sys.path
            map(working_set.add, distributions)
            # display errors
            print('Could not load', errors)

        The `plugin_env` should be an ``Environment`` instance that contains
        only distributions that are in the project's "plugin directory" or
        directories. The `full_env`, if supplied, should be an ``Environment``
        contains all currently-available distributions.  If `full_env` is not
        supplied, one is created automatically from the ``WorkingSet`` this
        method is called on, which will typically mean that every directory on
        ``sys.path`` will be scanned for distributions.

        `installer` is a standard installer callback as used by the
        ``resolve()`` method. The `fallback` flag indicates whether we should
        attempt to resolve older versions of a plugin if the newest version
        cannot be resolved.

        This method returns a 2-tuple: (`distributions`, `error_info`), where
        `distributions` is a list of the distributions found in `plugin_env`
        that were loadable, along with any other distributions that are needed
        to resolve their dependencies.  `error_info` is a dictionary mapping
        unloadable plugin distributions to an exception instance describing the
        error that occurred. Usually this will be a ``DistributionNotFound`` or
        ``VersionConflict`` instance.
        
Ensure that distributions matching `requirements` are activated

        `requirements` must be a string or a (possibly-nested) sequence
        thereof, specifying the distributions and versions required.  The
        return value is a sequence of the distributions that needed to be
        activated to fulfill the requirements; all relevant distributions are
        included, even if they were already activated in this working set.
        
Invoke `callback` for all distributions

        If `existing=True` (default),
        call on all existing ones, as well.
        

    Map each requirement to the extras that demanded it.
    

        Evaluate markers for req against each extra that
        demanded it.

        Return False if the req has a marker and fails
        evaluation. Otherwise, return True.
        
Searchable snapshot of distributions on a search path
Snapshot distributions available on a search path

        Any distributions found on `search_path` are added to the environment.
        `search_path` should be a sequence of ``sys.path`` items.  If not
        supplied, ``sys.path`` is used.

        `platform` is an optional string specifying the name of the platform
        that platform-specific distributions must be compatible with.  If
        unspecified, it defaults to the current platform.  `python` is an
        optional string naming the desired version of Python (e.g. ``'3.6'``);
        it defaults to the current version.

        You may explicitly set `platform` (and/or `python`) to ``None`` if you
        wish to map *all* distributions, not just those compatible with the
        running platform or Python version.
        
Is distribution `dist` acceptable for this environment?

        The distribution must match the platform and python version
        requirements specified when this environment was created, or False
        is returned.
        
Remove `dist` from the environment
Scan `search_path` for distributions usable in this environment

        Any distributions found are added to the environment.
        `search_path` should be a sequence of ``sys.path`` items.  If not
        supplied, ``sys.path`` is used.  Only distributions conforming to
        the platform/python version defined at initialization are added.
        
Return a newest-to-oldest list of distributions for `project_name`

        Uses case-insensitive `project_name` comparison, assuming all the
        project's distributions use their project's name converted to all
        lowercase as their key.

        
Add `dist` if we ``can_add()`` it and it has not already been added
Find distribution best matching `req` and usable on `working_set`

        This calls the ``find(req)`` method of the `working_set` to see if a
        suitable distribution is already active.  (This may raise
        ``VersionConflict`` if an unsuitable version of the project is already
        active in the specified `working_set`.)  If a suitable distribution
        isn't active, this method returns the newest distribution in the
        environment that meets the ``Requirement`` in `req`.  If no suitable
        distribution is found, and `installer` is supplied, then the result of
        calling the environment's ``obtain(req, installer)`` method will be
        returned.
        
Obtain a distribution matching `requirement` (e.g. via download)

        Obtain a distro that matches requirement (e.g. via download).  In the
        base ``Environment`` class, this routine just returns
        ``installer(requirement)``, unless `installer` is None, in which case
        None is returned instead.  This method is a hook that allows subclasses
        to attempt other ways of obtaining a distribution before falling back
        to the `installer` argument.
Yield the unique project names of the available distributions
In-place addition of a distribution or environment
Add an environment or distribution to an environment
An error occurred extracting a resource

    The following attributes are available from instances of this exception:

    manager
        The resource manager that raised this exception

    cache_path
        The base directory for resource extraction

    original_error
        The exception instance that caused extraction to fail
    
Manage resource extraction and packages
Does the named resource exist?
Is the named resource an existing directory?
Return a true filesystem path for specified resource
Return a readable file-like object for specified resource
Return specified resource as :obj:`bytes`
List the contents of the named resource directory
Give an error message for problems extracting file(s)

            Can't extract file(s) to egg cache

            The following error occurred while trying to extract file(s)
            to the Python egg cache:

              {old_exc}

            The Python egg cache directory is currently set to:

              {cache_path}

            Perhaps your account does not have write access to this directory?
            You can change the cache directory by setting the PYTHON_EGG_CACHE
            environment variable to point to an accessible directory.
            
Return absolute location in cache for `archive_name` and `names`

        The parent directory of the resulting path will be created if it does
        not already exist.  `archive_name` should be the base filename of the
        enclosing egg (which may not be the name of the enclosing zipfile!),
        including its ".egg" extension.  `names`, if provided, should be a
        sequence of path name parts "under" the egg's extraction location.

        This method should only be called by resource providers that need to
        obtain an extraction location, and only for names they intend to
        extract, as it tracks the generated names for possible cleanup later.
        

        If the default extraction path is overridden and set to an insecure
        location, such as /tmp, it opens up an opportunity for an attacker to
        replace an extracted file with an unauthorized payload. Warn the user
        if a known insecure location is used.

        See Distribute #375 for more details.
        
Perform any platform-specific postprocessing of `tempname`

        This is where Mac header rewrites should be done; other platforms don't
        have anything special they should do.

        Resource providers should call this method ONLY after successfully
        extracting a compressed resource.  They must NOT call it on resources
        that are already in the filesystem.

        `tempname` is the current (temporary) name of the file, and `filename`
        is the name it will be renamed to by the caller after this routine
        returns.
        
Set the base path where resources will be extracted to, if needed.

        If you do not call this routine before any extractions take place, the
        path defaults to the return value of ``get_default_cache()``.  (Which
        is based on the ``PYTHON_EGG_CACHE`` environment variable, with various
        platform-specific fallbacks.  See that routine's documentation for more
        details.)

        Resources are extracted to subdirectories of this path based upon
        information given by the ``IResourceProvider``.  You may set this to a
        temporary directory, but then you must call ``cleanup_resources()`` to
        delete the extracted files when done.  There is no guarantee that
        ``cleanup_resources()`` will be able to remove all extracted files.

        (Note: you may not change the extraction path for a given resource
        manager once resources have been extracted, unless you first call
        ``cleanup_resources()``.)
        

        Delete all extracted resource files and directories, returning a list
        of the file and directory names that could not be successfully removed.
        This function does not have any concurrency protection, so it should
        generally only be called when the extraction path is a temporary
        directory exclusive to a single process.  This method is not
        automatically called; you must call it explicitly or register it as an
        ``atexit`` function if you wish to ensure cleanup of a temporary
        directory used for extractions.
        

    Return the ``PYTHON_EGG_CACHE`` environment variable
    or a platform-relevant user cache dir for an app
    named "Python-Eggs".
    
Convert an arbitrary string to a standard distribution name

    Any runs of non-alphanumeric/. characters are replaced with a single '-'.
    

    Convert an arbitrary string to a standard version string
    
Fallback when ``safe_version`` is not safe enough
    >>> parse_version(_forgiving_version('0.23ubuntu1'))
    <Version('0.23.dev0+sanitized.ubuntu1')>
    >>> parse_version(_forgiving_version('0.23-'))
    <Version('0.23.dev0+sanitized')>
    >>> parse_version(_forgiving_version('0.-_'))
    <Version('0.dev0+sanitized')>
    >>> parse_version(_forgiving_version('42.+?1'))
    <Version('42.dev0+sanitized.1')>
    >>> parse_version(_forgiving_version('hello world'))
    <Version('0.dev0+sanitized.hello.world')>
    
Convert an arbitrary string into a safe segment
Convert an arbitrary string to a standard 'extra' name

    Any runs of non-alphanumeric characters are replaced with a single '_',
    and the result is always lowercased.
    
Convert a project or version name to its filename-escaped form

    Any '-' characters are currently replaced with '_'.
    

    Validate text as a PEP 508 environment marker; return an exception
    if invalid or False otherwise.
    

    Evaluate a PEP 508 environment marker.
    Return a boolean indicating the marker result in this environment.
    Raise SyntaxError if marker is invalid.

    This implementation uses the 'pyparsing' module.
    
Try to implement resources and metadata for arbitrary PEP 302 loaders

        Validate the resource paths according to the docs.
        https://setuptools.pypa.io/en/latest/pkg_resources.html#basic-resource-access

        >>> warned = getfixture('recwarn')
        >>> warnings.simplefilter('always')
        >>> vrp = NullProvider._validate_resource_path
        >>> vrp('foo/bar.txt')
        >>> bool(warned)
        False
        >>> vrp('../foo/bar.txt')
        >>> bool(warned)
        True
        >>> warned.clear()
        >>> vrp('/foo/bar.txt')
        >>> bool(warned)
        True
        >>> vrp('foo/../../bar.txt')
        >>> bool(warned)
        True
        >>> warned.clear()
        >>> vrp('foo/f../bar.txt')
        >>> bool(warned)
        False

        Windows path separators are straight-up disallowed.
        >>> vrp(r'\\foo/bar.txt')
        Traceback (most recent call last):
        ...
        ValueError: Use of .. or absolute path in a resource path \
is not allowed.

        >>> vrp(r'C:\\foo/bar.txt')
        Traceback (most recent call last):
        ...
        ValueError: Use of .. or absolute path in a resource path \
is not allowed.

        Blank values are allowed

        >>> vrp('')
        >>> bool(warned)
        False

        Non-string values are not.

        >>> vrp(None)
        Traceback (most recent call last):
        ...
        AttributeError: ...
        

    yield all parents of path including path
    
Provider based on a virtual filesystem
Provides access to package resources in the filesystem
Provider that returns nothing for all requests

    zip manifest builder
    

        Build a dictionary similar to the zipimport directory
        caches, except instead of tuples, store ZipInfo objects.

        Use a platform-specific path separator (os.sep) for the path keys
        for compatibility with pypy on Windows.
        

    Memoized zipfile manifests.
    

        Load a manifest at path or return a suitable manifest already loaded.
        
Resource support for zips and eggs

        Return True if the file_path is current for this zip_path
        
Metadata handler for standalone PKG-INFO files

    Usage::

        metadata = FileMetadata("/path/to/PKG-INFO")

    This provider rejects all data and metadata requests except for PKG-INFO,
    which is treated as existing, and will be the contents of the file at
    the provided location.
    
Metadata provider for egg directories

    Usage::

        # Development eggs:

        egg_info = "/path/to/PackageName.egg-info"
        base_dir = os.path.dirname(egg_info)
        metadata = PathMetadata(base_dir, egg_info)
        dist_name = os.path.splitext(os.path.basename(egg_info))[0]
        dist = Distribution(basedir, project_name=dist_name, metadata=metadata)

        # Unpacked egg directories:

        egg_path = "/path/to/PackageName-ver-pyver-etc.egg"
        metadata = PathMetadata(egg_path, os.path.join(egg_path,'EGG-INFO'))
        dist = Distribution.from_filename(egg_path, metadata=metadata)
    
Metadata provider for .egg files
Create a metadata provider from a zipimporter
Register `distribution_finder` to find distributions in sys.path items

    `importer_type` is the type or class of a PEP 302 "Importer" (sys.path item
    handler), and `distribution_finder` is a callable that, passed a path
    item and the importer instance, yields ``Distribution`` instances found on
    that path item.  See ``pkg_resources.find_on_path`` for an example.
Yield distributions accessible via `path_item`

    Find eggs in zip files; possibly multiple nested eggs.
    
Yield distributions accessible on a sys.path directory
Return a dist_factory for the given entry.

    >>> bool(NoDists())
    False

    >>> list(NoDists()('anything'))
    []
    

    Attempt to list contents of path, but suppress some exceptions.
    

    Yield non-empty lines from file at path
    

    Given a path to an .egg-link, resolve distributions
    present in the referenced path.
    
Register `namespace_handler` to declare namespace packages

    `importer_type` is the type or class of a PEP 302 "Importer" (sys.path item
    handler), and `namespace_handler` is a callable like this::

        def namespace_handler(importer, path_entry, moduleName, module):
            # return a path_entry to use for child packages

    Namespace handlers are only called if the importer object has already
    agreed that it can handle the relevant path item, and they should only
    return a subpath if the module __path__ does not already contain an
    equivalent subpath.  For an example namespace handler, see
    ``pkg_resources.file_ns_handler``.
    
Ensure that named package includes a subpath of path_item (if needed)

    Rebuild module.__path__ ensuring that all entries are ordered
    corresponding to their sys.path order
    

        Workaround for #520 and #513.
        

        Return the ordinal of the path based on its position in sys.path
        
Declare that package 'packageName' is a namespace package
Ensure that previously-declared namespace packages include path_item
Compute an ns-package subpath for a filesystem or zipfile importer
Normalize a file/dir name for comparison purposes

    Contrary to POSIX 2008, on Cygwin, getcwd (3) contains
    symlink components. Using
    os.path.abspath() works around this limitation. A fix in os.getcwd()
    would probably better, in Cygwin even more so, except
    that this seems to be by design...
    

    Determine if given path appears to be an egg.
    

    Determine if given path appears to be an unpacked egg.
    

    (?P<name>[^-]+) (
        -(?P<ver>[^-]+) (
            -py(?P<pyver>[^-]+) (
                -(?P<plat>.+)
            )?
        )?
    )?
    
Object representing an advertised importable object

        Require packages for this EntryPoint, then resolve it.
        

        Resolve the entry point from its module and attrs.
        
Parse a single entry point from string `src`

        Entry point syntax follows the form::

            name = some.module:some.attr [extra1, extra2]

        The entry name and module name are required, but the ``:attrs`` and
        ``[extras]`` parts are optional
        
Parse an entry point group
Parse a map of entry point groups

    Given an iterable of lines from a Metadata file, return
    the value of the Version field, if present, or None otherwise.
    
Wrap an actual or potential sys.path entry w/metadata
!!\n\n
            *************************************************************************
            {str(ex)}\n{notes}

            This is a long overdue deprecation.
            For the time being, `pkg_resources` will use `{self._parsed_version}`
            as a replacement to avoid breaking existing environments,
            but no future compatibility is guaranteed.

            If you maintain package {self.project_name} you should implement
            the relevant changes to adequate the project to PEP 440 immediately.
            *************************************************************************
            \n\n!!
            

        A map of extra to its list of (direct) requirements
        for this distribution, including the null extra.
        

        Given a mapping of extras to dependencies, strip off
        environment markers and filter out any dependencies
        not matching the markers.
        
List of Requirements needed for this distro if `extras` are used

        Return the path to the given metadata file, if available.
        
Ensure distribution is importable on `path` (default=sys.path)
Return what this distribution's standard .egg filename should be
Delegate all unrecognized public attributes to .metadata provider
Return a ``Requirement`` that matches this distribution exactly
Return the `name` entry point of `group` or raise ImportError
Return the entry point map for `group`, or the full entry map
Return the EntryPoint object for `group`+`name`, or ``None``
Ensure self.location is on path

        If replace=False (default):
            - If location is already in path anywhere, do nothing.
            - Else:
              - If it's an egg and its parent directory is on path,
                insert just ahead of the parent.
              - Else: add to the end of path.
        If replace=True:
            - If location is already on path anywhere (not eggs)
              or higher priority than its parent (eggs)
              do nothing.
            - Else:
              - If it's an egg and its parent directory is on path,
                insert just ahead of the parent,
                removing any lower-priority entries.
              - Else: add it to the front of path.
        
Copy this distribution, substituting in any changed keyword args

        Packages installed by distutils (e.g. numpy or scipy),
        which uses an old safe_version, and so
        their version numbers can get mangled when
        converted to filenames (e.g., 1.11.0.dev0+2329eae to
        1.11.0.dev0_2329eae). These distributions will not be
        parsed properly
        downstream by Distribution and safe_version, so
        take an extra step and try to get the version number from
        the metadata file itself instead of the filename.
        

    Wrap an actual or potential sys.path entry
    w/metadata, .dist-info style.
    
Parse and cache metadata
Recompute this distribution's dependencies.

    Yield ``Requirement`` objects for each specification in `strs`.

    `strs` must be a string, or a (possibly-nested) iterable thereof.
    
DO NOT CALL THIS UNDOCUMENTED METHOD; use Requirement.parse()!

    Ensure object appears in the mro even
    for old-style classes.
    
Return an adapter factory for `ob` from `registry`
Ensure that the parent directory of `path` exists
Sandbox-bypassing version of ensure_directory()
Split a string or iterable thereof into (section, content) pairs

    Each ``section`` is a stripped version of the section header ("[section]")
    and each ``content`` is a list of stripped lines excluding blank lines and
    comment-only lines.  If there are any such lines before the first section
    header, they're returned in a first ``section`` of ``None``.
    

    Base class for warning about deprecations in ``pkg_resources``

    This class is not derived from ``DeprecationWarning``, and as such is
    visible by default.
    
See setuptools.unicode_utils._read_utf8_with_fallback
\
        ********************************************************************************
        `encoding="utf-8"` fails with {file!r}, trying `encoding={fallback_encoding!r}`.

        This fallback behaviour is considered **deprecated** and future versions of
        `setuptools/pkg_resources` may not implement it.

        Please encode {file!r} with "utf-8" to ensure future builds will succeed.

        If this file was produced by `setuptools` itself, cleaning up the cached files
        and re-building/re-installing the package with a newer version of `setuptools`
        (e.g. by updating `build-system.requires` in its `pyproject.toml`)
        might solve the problem.
        ********************************************************************************
        

    Prepare the master working set and make the ``require()``
    API available.

    This function has explicit effects on the global state
    of pkg_resources. It is intended to be invoked once at
    the initialization of this module.

    Invocation by other packages is unsupported and done
    at their own risk.
    

---



---

Base API.
Abstract base class for platform directories.

        Create a new platform directory.

        :param appname: See `appname`.
        :param appauthor: See `appauthor`.
        :param version: See `version`.
        :param roaming: See `roaming`.
        :param multipath: See `multipath`.
        :param opinion: See `opinion`.
        :param ensure_exists: See `ensure_exists`.

        

        The name of the app author or distributing body for this application.

        Typically, it is the owning company name. Defaults to `appname`. You may pass ``False`` to disable it.

        

        An optional version path element to append to the path.

        You might want to use this if you want multiple versions of your app to be able to run independently. If used,
        this would typically be ``<major>.<minor>``.

        

        Whether to use the roaming appdata directory on Windows.

        That means that for users on a Windows network setup for roaming profiles, this user data will be synced on
        login (see
        `here <https://technet.microsoft.com/en-us/library/cc766489(WS.10).aspx>`_).

        

        An optional parameter which indicates that the entire list of data dirs should be returned.

        By default, the first item would only be returned.

        

        Optionally create the directory (and any missing parents) upon access if it does not exist.

        By default, no directories are created.

        
:return: data directory tied to the user
:return: data directory shared by users
:return: config directory tied to the user
:return: config directory shared by the users
:return: cache directory tied to the user
:return: cache directory shared by users
:return: state directory tied to the user
:return: log directory tied to the user
:return: documents directory tied to the user
:return: downloads directory tied to the user
:return: pictures directory tied to the user
:return: videos directory tied to the user
:return: music directory tied to the user
:return: desktop directory tied to the user
:return: runtime directory tied to the user
:return: runtime directory shared by users
:return: data path tied to the user
:return: data path shared by users
:return: config path tied to the user
:return: config path shared by the users
:return: cache path tied to the user
:return: cache path shared by users
:return: state path tied to the user
:return: log path tied to the user
:return: documents a path tied to the user
:return: downloads path tied to the user
:return: pictures path tied to the user
:return: videos path tied to the user
:return: music path tied to the user
:return: desktop path tied to the user
:return: runtime path tied to the user
:return: runtime path shared by users
:yield: all user and site configuration directories.
:yield: all user and site data directories.
:yield: all user and site cache directories.
:yield: all user and site runtime directories.
:yield: all user and site configuration paths.
:yield: all user and site data paths.
:yield: all user and site cache paths.
:yield: all user and site runtime paths.

---

Unix.

    On Unix/Linux, we follow the `XDG Basedir Spec <https://specifications.freedesktop.org/basedir-spec/basedir-spec-
    latest.html>`_.

    The spec allows overriding directories with environment variables. The examples shown are the default values,
    alongside the name of the environment variable that overrides them. Makes use of the `appname
    <platformdirs.api.PlatformDirsABC.appname>`, `version <platformdirs.api.PlatformDirsABC.version>`, `multipath
    <platformdirs.api.PlatformDirsABC.multipath>`, `opinion <platformdirs.api.PlatformDirsABC.opinion>`, `ensure_exists
    <platformdirs.api.PlatformDirsABC.ensure_exists>`.

    

        :return: data directory tied to the user, e.g. ``~/.local/share/$appname/$version`` or
         ``$XDG_DATA_HOME/$appname/$version``
        

        :return: data directories shared by users (if `multipath <platformdirs.api.PlatformDirsABC.multipath>` is
         enabled and ``XDG_DATA_DIRS`` is set and a multi path the response is also a multi path separated by the
         OS path separator), e.g. ``/usr/local/share/$appname/$version`` or ``/usr/share/$appname/$version``
        

        :return: config directory tied to the user, e.g. ``~/.config/$appname/$version`` or
         ``$XDG_CONFIG_HOME/$appname/$version``
        

        :return: config directories shared by users (if `multipath <platformdirs.api.PlatformDirsABC.multipath>`
         is enabled and ``XDG_CONFIG_DIRS`` is set and a multi path the response is also a multi path separated by
         the OS path separator), e.g. ``/etc/xdg/$appname/$version``
        

        :return: cache directory tied to the user, e.g. ``~/.cache/$appname/$version`` or
         ``~/$XDG_CACHE_HOME/$appname/$version``
        
:return: cache directory shared by users, e.g. ``/var/cache/$appname/$version``

        :return: state directory tied to the user, e.g. ``~/.local/state/$appname/$version`` or
         ``$XDG_STATE_HOME/$appname/$version``
        
:return: log directory tied to the user, same as `user_state_dir` if not opinionated else ``log`` in it
:return: documents directory tied to the user, e.g. ``~/Documents``
:return: downloads directory tied to the user, e.g. ``~/Downloads``
:return: pictures directory tied to the user, e.g. ``~/Pictures``
:return: videos directory tied to the user, e.g. ``~/Videos``
:return: music directory tied to the user, e.g. ``~/Music``
:return: desktop directory tied to the user, e.g. ``~/Desktop``

        :return: runtime directory tied to the user, e.g. ``/run/user/$(id -u)/$appname/$version`` or
         ``$XDG_RUNTIME_DIR/$appname/$version``.

         For FreeBSD/OpenBSD/NetBSD, it would return ``/var/run/user/$(id -u)/$appname/$version`` if
         exists, otherwise ``/tmp/runtime-$(id -u)/$appname/$version``, if``$XDG_RUNTIME_DIR``
         is not set.
        

        :return: runtime directory shared by users, e.g. ``/run/$appname/$version`` or \
        ``$XDG_RUNTIME_DIR/$appname/$version``.

        Note that this behaves almost exactly like `user_runtime_dir` if ``$XDG_RUNTIME_DIR`` is set, but will
        fall back to paths associated to the root user instead of a regular logged-in user if it's not set.

        If you wish to ensure that a logged-in root user path is returned e.g. ``/run/user/0``, use `user_runtime_dir`
        instead.

        For FreeBSD/OpenBSD/NetBSD, it would return ``/var/run/$appname/$version`` if ``$XDG_RUNTIME_DIR`` is not set.
        
:return: data path shared by users. Only return the first item, even if ``multipath`` is set to ``True``
:return: config path shared by the users, returns the first item, even if ``multipath`` is set to ``True``
:return: cache path shared by users. Only return the first item, even if ``multipath`` is set to ``True``
:yield: all user and site configuration directories.
:yield: all user and site data directories.

    Return directory from user-dirs.dirs config file.

    See https://freedesktop.org/wiki/Software/xdg-user-dirs/.

    

---

Windows.

    `MSDN on where to store app data files <https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid>`_.

    Makes use of the `appname <platformdirs.api.PlatformDirsABC.appname>`, `appauthor
    <platformdirs.api.PlatformDirsABC.appauthor>`, `version <platformdirs.api.PlatformDirsABC.version>`, `roaming
    <platformdirs.api.PlatformDirsABC.roaming>`, `opinion <platformdirs.api.PlatformDirsABC.opinion>`, `ensure_exists
    <platformdirs.api.PlatformDirsABC.ensure_exists>`.

    

        :return: data directory tied to the user, e.g.
         ``%USERPROFILE%\\AppData\\Local\\$appauthor\\$appname`` (not roaming) or
         ``%USERPROFILE%\\AppData\\Roaming\\$appauthor\\$appname`` (roaming)
        
:return: data directory shared by users, e.g. ``C:\\ProgramData\\$appauthor\\$appname``
:return: config directory tied to the user, same as `user_data_dir`
:return: config directory shared by the users, same as `site_data_dir`

        :return: cache directory tied to the user (if opinionated with ``Cache`` folder within ``$appname``) e.g.
         ``%USERPROFILE%\\AppData\\Local\\$appauthor\\$appname\\Cache\\$version``
        
:return: cache directory shared by users, e.g. ``C:\\ProgramData\\$appauthor\\$appname\\Cache\\$version``
:return: state directory tied to the user, same as `user_data_dir`
:return: log directory tied to the user, same as `user_data_dir` if not opinionated else ``Logs`` in it
:return: documents directory tied to the user e.g. ``%USERPROFILE%\\Documents``
:return: downloads directory tied to the user e.g. ``%USERPROFILE%\\Downloads``
:return: pictures directory tied to the user e.g. ``%USERPROFILE%\\Pictures``
:return: videos directory tied to the user e.g. ``%USERPROFILE%\\Videos``
:return: music directory tied to the user e.g. ``%USERPROFILE%\\Music``
:return: desktop directory tied to the user, e.g. ``%USERPROFILE%\\Desktop``

        :return: runtime directory tied to the user, e.g.
         ``%USERPROFILE%\\AppData\\Local\\Temp\\$appauthor\\$appname``
        
:return: runtime directory shared by users, same as `user_runtime_dir`
Get folder from environment variables.
Get a folder for a CSIDL name that does not exist as an environment variable.

    Get folder from the registry.

    This is a fallback technique at best. I'm not sure if using the registry for these guarantees us the correct answer
    for all CSIDL_* names.

    
Get folder with ctypes.

---


Utilities for determining application-specific dirs.

See <https://github.com/platformdirs/platformdirs> for details and usage.



    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: data directory tied to the user
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param multipath: See `roaming <platformdirs.api.PlatformDirsABC.multipath>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: data directory shared by users
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: config directory tied to the user
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param multipath: See `roaming <platformdirs.api.PlatformDirsABC.multipath>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: config directory shared by the users
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: cache directory tied to the user
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: cache directory tied to the user
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: state directory tied to the user
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: log directory tied to the user
    
:returns: documents directory tied to the user
:returns: downloads directory tied to the user
:returns: pictures directory tied to the user
:returns: videos directory tied to the user
:returns: music directory tied to the user
:returns: desktop directory tied to the user

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: runtime directory tied to the user
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: runtime directory shared by users
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: data path tied to the user
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param multipath: See `multipath <platformdirs.api.PlatformDirsABC.multipath>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: data path shared by users
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: config path tied to the user
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param multipath: See `roaming <platformdirs.api.PlatformDirsABC.multipath>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: config path shared by the users
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: cache directory tied to the user
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: cache path tied to the user
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: state path tied to the user
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: log path tied to the user
    
:returns: documents a path tied to the user
:returns: downloads path tied to the user
:returns: pictures path tied to the user
:returns: videos path tied to the user
:returns: music path tied to the user
:returns: desktop path tied to the user

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: runtime path tied to the user
    

    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: runtime path shared by users
    

---

macOS.

    Platform directories for the macOS operating system.

    Follows the guidance from
    `Apple documentation <https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html>`_.
    Makes use of the `appname <platformdirs.api.PlatformDirsABC.appname>`,
    `version <platformdirs.api.PlatformDirsABC.version>`,
    `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.

    
:return: data directory tied to the user, e.g. ``~/Library/Application Support/$appname/$version``

        :return: data directory shared by users, e.g. ``/Library/Application Support/$appname/$version``.
          If we're using a Python binary managed by `Homebrew <https://brew.sh>`_, the directory
          will be under the Homebrew prefix, e.g. ``/opt/homebrew/share/$appname/$version``.
          If `multipath <platformdirs.api.PlatformDirsABC.multipath>` is enabled, and we're in Homebrew,
          the response is a multi-path string separated by ":", e.g.
          ``/opt/homebrew/share/$appname/$version:/Library/Application Support/$appname/$version``
        
:return: data path shared by users. Only return the first item, even if ``multipath`` is set to ``True``
:return: config directory tied to the user, same as `user_data_dir`
:return: config directory shared by the users, same as `site_data_dir`
:return: cache directory tied to the user, e.g. ``~/Library/Caches/$appname/$version``

        :return: cache directory shared by users, e.g. ``/Library/Caches/$appname/$version``.
          If we're using a Python binary managed by `Homebrew <https://brew.sh>`_, the directory
          will be under the Homebrew prefix, e.g. ``/opt/homebrew/var/cache/$appname/$version``.
          If `multipath <platformdirs.api.PlatformDirsABC.multipath>` is enabled, and we're in Homebrew,
          the response is a multi-path string separated by ":", e.g.
          ``/opt/homebrew/var/cache/$appname/$version:/Library/Caches/$appname/$version``
        
:return: cache path shared by users. Only return the first item, even if ``multipath`` is set to ``True``
:return: state directory tied to the user, same as `user_data_dir`
:return: log directory tied to the user, e.g. ``~/Library/Logs/$appname/$version``
:return: documents directory tied to the user, e.g. ``~/Documents``
:return: downloads directory tied to the user, e.g. ``~/Downloads``
:return: pictures directory tied to the user, e.g. ``~/Pictures``
:return: videos directory tied to the user, e.g. ``~/Movies``
:return: music directory tied to the user, e.g. ``~/Music``
:return: desktop directory tied to the user, e.g. ``~/Desktop``
:return: runtime directory tied to the user, e.g. ``~/Library/Caches/TemporaryItems/$appname/$version``
:return: runtime directory shared by users, same as `user_runtime_dir`

---

Main entry point.
Run the main entry point.

---

Android.

    Follows the guidance `from here <https://android.stackexchange.com/a/216132>`_.

    Makes use of the `appname <platformdirs.api.PlatformDirsABC.appname>`, `version
    <platformdirs.api.PlatformDirsABC.version>`, `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.

    
:return: data directory tied to the user, e.g. ``/data/user/<userid>/<packagename>/files/<AppName>``
:return: data directory shared by users, same as `user_data_dir`

        :return: config directory tied to the user, e.g. \
        ``/data/user/<userid>/<packagename>/shared_prefs/<AppName>``
        
:return: config directory shared by the users, same as `user_config_dir`
:return: cache directory tied to the user, e.g.,``/data/user/<userid>/<packagename>/cache/<AppName>``
:return: cache directory shared by users, same as `user_cache_dir`
:return: state directory tied to the user, same as `user_data_dir`

        :return: log directory tied to the user, same as `user_cache_dir` if not opinionated else ``log`` in it,
          e.g. ``/data/user/<userid>/<packagename>/cache/<AppName>/log``
        
:return: documents directory tied to the user e.g. ``/storage/emulated/0/Documents``
:return: downloads directory tied to the user e.g. ``/storage/emulated/0/Downloads``
:return: pictures directory tied to the user e.g. ``/storage/emulated/0/Pictures``
:return: videos directory tied to the user e.g. ``/storage/emulated/0/DCIM/Camera``
:return: music directory tied to the user e.g. ``/storage/emulated/0/Music``
:return: desktop directory tied to the user e.g. ``/storage/emulated/0/Desktop``

        :return: runtime directory tied to the user, same as `user_cache_dir` if not opinionated else ``tmp`` in it,
          e.g. ``/data/user/<userid>/<packagename>/cache/<AppName>/tmp``
        
:return: runtime directory shared by users, same as `user_runtime_dir`
:return: base folder for the Android OS or None if it cannot be found
:return: documents folder for the Android OS
:return: downloads folder for the Android OS
:return: pictures folder for the Android OS
:return: videos folder for the Android OS
:return: music folder for the Android OS

---


        Return a valid 1xx warning header value describing the cache
        adjustments.

        The response is provided too allow warnings like 113
        http://tools.ietf.org/html/rfc7234#section-5.5.4 where we need
        to explicitly say response is over 24 hours old.
        
Update the response headers with any new headers.

        NOTE: This SHOULD always include some Warning header to
              signify that the response was cached by the client, not
              by way of the provided headers.
        

    Cache the response by providing an expires 1 day in the
    future.
    

    Cache **all** requests for a defined time period.
    

    If there is no Expires header already, fall back on Last-Modified
    using the heuristic from
    http://tools.ietf.org/html/rfc7234#section-4.2.2
    to calculate a reasonable value.

    Firefox also does something like this per
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching_FAQ
    http://lxr.mozilla.org/mozilla-release/source/netwerk/protocol/http/nsHttpResponseHead.cpp#397
    Unlike mozilla we limit this to 24-hr.
    

---

Verify our vary headers match and construct a real urllib3
        HTTPResponse object.
        

---



---


        Send a request. Use the request information to see if it
        exists in the cache and cache the response if we need to and can.
        

        Build a response by making a request or using the cache.

        This will end up calling send and returning a potentially
        cached response
        

---


    Small wrapper around a fp object which will tee everything read into a
    buffer, and when that file is closed it will execute a callback with the
    contents of that buffer.

    All attributes are proxied to the underlying file object.

    This class uses members with a double underscore (__) leading prefix so as
    not to accidentally shadow an attribute.

    The data is stored in a temporary file until it is all available.  As long
    as the temporary files directory is disk-based (sometimes it's a
    memory-backed-``tmpfs`` on Linux), data will be unloaded to disk if memory
    pressure is high.  For small files the disk usually won't be used at all,
    it'll all be in the filesystem memory cache, so there should be no
    performance impact.
    

---


The cache object API for implementing caches. The default is a thread
safe in-memory dictionary.


    In this variant, the body is not stored mixed in with the metadata, but is
    passed in (as a bytes-like object) in a separate call to ``set_body()``.

    That is, the expected interaction pattern is::

        cache.set(key, serialized_metadata)
        cache.set_body(key)

    Similarly, the body should be loaded separately via ``get_body()``.
    

        Return the body as file-like object.
        

---

CacheControl import Interface.

Make it easy to import from cachecontrol without long namespaces.


---



---


The httplib2 algorithms ported for use with requests.

Parses a URI using the regex given in Appendix B of RFC 3986.

    (scheme, authority, path, query, fragment) = parse_uri(uri)
    
An interface to see if request should cached or not.
Normalize the URL to create a safe key for the cache

        Load a cached response, or return None if it's not available.
        

        Return a cached response if it exists in the cache, otherwise
        return False.
        

        Store the data in the cache.
        

        Algorithm for caching requests.

        This assumes a requests Response object.
        
On a 304 we will get a new set of headers that we want to
        update our cached value with, assuming we have one.

        This should only ever be called when we've sent an ETag and
        gotten a 304 as the response.
        

---

Shared implementation for both FileCache variants.

            NOTE: In order to use the FileCache you must have
            filelock installed. You can install it via pip:
              pip install cachecontrol[filecache]
            

        Safely write the data to the given path.
        

    Traditional FileCache: body is stored in memory, so not suitable for large
    downloads.
    

    Memory-efficient FileCache: body is stored in a separate file, reducing
    peak memory usage.
    
Return the file cache path based on the URL.

    This does not ensure the file exists!
    

---

Helper for clearing all the keys in a database. Use with
        caution!
Redis uses connection pooling, no need to close the connection.

---



---


Parser for the environment markers micro-language defined in PEP 508.


    This class is used to evaluate marker expressions.
    

        Evaluate a marker expression returned by the :func:`parse_requirement`
        function in the specified context.
        

    Interpret a marker and return a result depending on environment.

    :param marker: The marker to interpret.
    :type marker: str
    :param execution_context: The context used for name lookup.
    :type execution_context: mapping
    

---


    Parse a marker string and return a dictionary containing a marker expression.

    The dictionary will contain keys "op", "lhs" and "rhs" for non-terminals in
    the expression grammar, or strings. A string contained in quotes is to be
    interpreted as a literal string, and a string not contained in quotes is a
    variable (such as os_name).
    

    Parse a requirement passed in as a string. Return a Container
    whose attributes contain the various parts of the requirement.
    

                Return a list of operator, version tuples if any are
                specified, else None.
                
Find destinations for resources files
Return 'pathname' as a name that will work on the native filesystem.

    The path is split on '/' and put back together again using the current
    directory separator.  Needed because filenames in the setup script are
    always supplied in Unix style, and have to be converted to the local
    convention before we can actually use them in the filesystem.  Raises
    ValueError on non-Unix-ish systems if 'pathname' either starts or
    ends with a slash.
    
Tell if the target is newer than the source.

        Returns true if 'source' exists and is more recently modified than
        'target', or if 'source' exists and 'target' doesn't.

        Returns false if both exist and 'target' is the same age or younger
        than 'source'. Raise PackagingFileError if 'source' does not exist.

        Note that this test is not very accurate: files created in the same
        second will have the same "age".
        
Copy a file respecting dry-run and force flags.
        

        Commit recorded changes, turn off recording, return
        changes.
        

    Return the default base location for distlib caches. If the directory does
    not exist, it is created. Use the suffix provided for the base directory,
    and default to '.distlib' if it isn't provided.

    On Windows, if LOCALAPPDATA is defined in the environment, then it is
    assumed to be a directory, and will be the parent directory of the result.
    On POSIX, and on Windows if LOCALAPPDATA is not defined, the user's home
    directory - using os.expanduser('~') - will be the parent directory of
    the result.

    The result is just the directory '.distlib' in the parent directory as
    determined above, or with the name specified with ``suffix``.
    

    Convert an absolute path to a directory name for use in a cache.

    The algorithm used is:

    #. On Windows, any ``':'`` in the drive is replaced with ``'---'``.
    #. Any occurrence of ``os.sep`` is replaced with ``'--'``.
    #. ``'.cache'`` is appended.
    

    Extract name, version, python version from a filename (no extension)

    Return name, version, pyver or None
    

    A utility method used to get name and version from a string.

    From e.g. a Provides-Dist value.

    :param p: A value in a form 'foo (1.0)'
    :return: The name and version as a tuple.
    

    A class implementing a cache for resources that need to live in the file system
    e.g. shared libraries. This class was moved from resources to here because it
    could be used by other modules, e.g. the wheel module.
    

        Initialise an instance.

        :param base: The base directory where the cache should be located.
        

        Converts a resource prefix to a directory name in the cache.
        

        Clear the cache.
        

    A very simple publish/subscribe system.
    

        Add a subscriber for an event.

        :param event: The name of an event.
        :param subscriber: The subscriber to be added (and called when the
                           event is published).
        :param append: Whether to append or prepend the subscriber to an
                       existing subscriber list for the event.
        

        Remove a subscriber for an event.

        :param event: The name of an event.
        :param subscriber: The subscriber to be removed.
        

        Return an iterator for the subscribers for an event.
        :param event: The event to return subscribers for.
        

        Publish a event and return a list of values returned by its
        subscribers.

        :param event: The event to publish.
        :param args: The positional arguments to pass to the event's
                     subscribers.
        :param kwargs: The keyword arguments to pass to the event's
                       subscribers.
        
Run tarfile.tar_filter, but raise the expected ValueError
zip a directory tree into a BytesIO object
Extended globbing function that supports ** and {opt1,opt2,opt3}.
invalid glob %r: recursive glob "**" must be used alone
invalid glob %r: mismatching set marker '{' or '}'

            This is called to create a connection instance. Normally you'd
            pass a connection class to do_open, but it doesn't actually check for
            a class, and just expects a callable. As long as we behave just as a
            constructor would have, we should be OK. If it ever changes so that
            we *must* pass a class, we'll create an UnsafeHTTPSConnection class
            which just sets check_domain to False in the class definition, and
            choose which one to pass to do_open.
            
Default converter for the inc:// protocol.

    Mixin for running subprocesses and capturing their output
    

        Read lines from a subprocess' output stream and either pass to a progress
        callable (if specified) or write progress information to sys.stderr.
        
Normalize a python package name a la PEP 503

# Get the distutils command for interacting with PyPI configurations.
# :return: the command.
# 

    Read the PyPI access configuration as supported by distutils.
    
Return a string that identifies the current platform.  This is used mainly to
    distinguish platform-specific build directories and platform-specific built
    distributions.  Typically includes the OS name and version and the
    architecture (as supplied by 'os.uname()'), although the exact information
    included depends on the OS; eg. on Linux, the kernel version isn't
    particularly important.

    Examples of returned values:
       linux-i586
       linux-alpha (?)
       solaris-2.6-sun4u

    Windows will return one of:
       win-amd64 (64bit Windows on AMD64 (aka x86_64, Intel64, EM64T, etc)
       win32 (all others - specifically, sys.platform is returned)

    For other non-POSIX platforms, currently just returns 'sys.platform'.

    

---


Implementation of a flexible versioning scheme providing support for PEP-440,
setuptools-compatible and semantic versioning.

This is an unsupported version.

        Check if the provided version matches the constraints.

        :param version: The version to match against this instance.
        :type version: String or :class:`Version` instance.
        
A rational version.

    Good:
        1.2         # equivalent to "1.2.0"
        1.2.0
        1.2a1
        1.2.3a2
        1.2.3b1
        1.2.3c1
        1.2.3.4
        TODO: fill this out

    Bad:
        1           # minimum two numbers
        1.2a        # release level must have a release serial
        1.2.3b
    

    Try to suggest a semantic form for a version for which
    _suggest_normalized_version couldn't come up with anything.
    
Suggest a normalized version close to the given version string.

    If you have a version string that isn't rational (i.e. NormalizedVersion
    doesn't like it) then you might be able to get an equivalent (or close)
    rational version from this function.

    This does a number of simple normalizations to the given string, based
    on observation of versions currently in use on PyPI. Given a dump of
    those version during PyCon 2009, 4287 of them:
    - 2312 (53.93%) match NormalizedVersion without change
      with the automatic suggestion
    - 3474 (81.04%) match when using this suggestion method

    @param s {str} An irrational version string.
    @returns A rational version string, or None, if couldn't determine one.
    

        Used for processing some metadata fields
        

---


    A class to copy or create scripts from source scripts or callable
    specifications.
    

            Determine if the specified executable is a script
            (contains a #! line)
            

        Build a shebang line. In the simple case (on Windows, or a shebang line
        which is not too long or contains spaces) use a simple formulation for
        the shebang. Otherwise, use /bin/sh as the executable, with a contrived
        shebang which allows the script to run either under Python or sh, using
        suitable quoting. Thanks to Harald Nordgren for his input.

        See also: http://www.in-ulm.de/~mascheck/various/shebang/#length
                  https://hg.mozilla.org/mozilla-central/file/tip/mach
        

        Make a script.

        :param specification: The specification, which is either a valid export
                              entry specification (to make a script from a
                              callable) or a filename (to make a script by
                              copying from a source location).
        :param options: A dictionary of options controlling script generation.
        :return: A list of all absolute pathnames written to.
        

        Take a list of specifications and make scripts from them,
        :param specifications: A list of specifications.
        :return: A list of all absolute pathnames written to,
        

---

PEP 376 implementation.

    A simple cache mapping names and .dist-info paths to distributions
    

        Initialise an instance. There is normally one for each DistributionPath.
        

        Clear the cache, setting it to its initial state.
        

        Add a distribution to the cache.
        :param dist: The distribution to add.
        

    Represents a set of distributions installed on a path (typically sys.path).
    

        Create an instance from a path, optionally including legacy (distutils/
        setuptools/distribute) distributions.
        :param path: The path to use, as a list of directories. If not specified,
                     sys.path is used.
        :param include_egg: If True, this instance will look for and return legacy
                            distributions as well as those based on PEP 376.
        

        Clears the internal cache.
        

        Yield .dist-info and/or .egg(-info) distributions.
        

        Scan the path for distributions and populate the cache with
        those that are found.
        

        The *name* and *version* parameters are converted into their
        filename-escaped form, i.e. any ``'-'`` characters are replaced
        with ``'_'`` other than the one in ``'dist-info'`` and the one
        separating the name from the version number.

        :parameter name: is converted to a standard distribution name by replacing
                         any runs of non- alphanumeric characters with a single
                         ``'-'``.
        :type name: string
        :parameter version: is converted to a standard version string. Spaces
                            become dots, and all other non-alphanumeric characters
                            (except dots) become dashes, with runs of multiple
                            dashes condensed to a single dash.
        :type version: string
        :returns: directory name
        :rtype: string

        Provides an iterator that looks for distributions and returns
        :class:`InstalledDistribution` or
        :class:`EggInfoDistribution` instances for each one of them.

        :rtype: iterator of :class:`InstalledDistribution` and
                :class:`EggInfoDistribution` instances
        

        Looks for a named distribution on the path.

        This function only returns the first result found, as no more than one
        value is expected. If nothing is found, ``None`` is returned.

        :rtype: :class:`InstalledDistribution`, :class:`EggInfoDistribution`
                or ``None``
        

        Iterates over all distributions to find which distributions provide *name*.
        If a *version* is provided, it will be used to filter the results.

        This function only returns the first result found, since no more than
        one values are expected. If the directory is not found, returns ``None``.

        :parameter version: a version specifier that indicates the version
                            required, conforming to the format in ``PEP-345``

        :type name: string
        :type version: string
        

        Return the path to a resource file.
        

        Return all of the exported entries in a particular category.

        :param category: The category to search for entries.
        :param name: If specified, only entries with that name are returned.
        

    A base class for distributions, whether installed or from indexes.
    Either way, it must have some metadata, so that's all that's needed
    for construction.
    

    Set to True if it's known to be only a build-time dependency (i.e.
    not needed after installation).
    
A boolean that indicates whether the ``REQUESTED`` metadata file is
    present (in other words, whether the package was installed by user
    request or it was installed as a dependency).

        Initialise an instance.
        :param metadata: The instance of :class:`Metadata` describing this
        distribution.
        

        The source archive download URL for this distribution.
        

        A utility property which displays the name and version in parentheses.
        

        A set of distribution names and versions provided by this distribution.
        :return: A set of "name (version)" strings.
        

        Say if this instance matches (fulfills) a requirement.
        :param req: The requirement to match.
        :rtype req: str
        :return: True if it matches, else False.
        

        Return a textual representation of this instance,
        

        See if this distribution is the same as another.
        :param other: The distribution to compare with. To be equal to one
                      another. distributions must have the same type, name,
                      version and source_url.
        :return: True if it is the same, else False.
        

        Compute hash in a way which matches the equality test.
        

    This is the base class for installed distributions (whether PEP 376 or
    legacy).
    

        Initialise an instance.
        :param metadata: An instance of :class:`Metadata` which describes the
                         distribution. This will normally have been initialised
                         from a metadata file in the ``path``.
        :param path:     The path of the ``.dist-info`` or ``.egg-info``
                         directory for the distribution.
        :param env:      This is normally the :class:`DistributionPath`
                         instance where this distribution was found.
        

        Get the hash of some data, using a particular hash algorithm, if
        specified.

        :param data: The data to be hashed.
        :type data: bytes
        :param hasher: The name of a hash implementation, supported by hashlib,
                       or ``None``. Examples of valid values are ``'sha1'``,
                       ``'sha224'``, ``'sha384'``, '``sha256'``, ``'md5'`` and
                       ``'sha512'``. If no hasher is specified, the ``hasher``
                       attribute of the :class:`InstalledDistribution` instance
                       is used. If the hasher is determined to be ``None``, MD5
                       is used as the hashing algorithm.
        :returns: The hash of the data. If a hasher was explicitly specified,
                  the returned hash will be prefixed with the specified hasher
                  followed by '='.
        :rtype: str
        

    Created with the *path* of the ``.dist-info`` directory provided to the
    constructor. It reads the metadata contained in ``pydist.json`` when it is
    instantiated., or uses a passed in Metadata instance (useful for when
    dry-run mode is being used).
    

        Get the list of installed files for the distribution
        :return: A list of tuples of path, hash and size. Note that hash and
                 size might be ``None`` for some entries. The path is exactly
                 as stored in the file (which is as in PEP 376).
        

        Return the information exported by this distribution.
        :return: A dictionary of exports, mapping an export category to a dict
                 of :class:`ExportEntry` instances describing the individual
                 export entries, and keyed by name.
        

        Read exports data from a file in .ini format.

        :return: A dictionary of exports, mapping an export category to a list
                 of :class:`ExportEntry` instances describing the individual
                 export entries.
        

        Write a dictionary of exports to a file in .ini format.
        :param exports: A dictionary of exports, mapping an export category to
                        a list of :class:`ExportEntry` instances describing the
                        individual export entries.
        

        NOTE: This API may change in the future.

        Return the absolute path to a resource file with the given relative
        path.

        :param relative_path: The path, relative to .dist-info, of the resource
                              of interest.
        :return: The absolute path where the resource is to be found.
        

        Iterates over the ``RECORD`` entries and returns a tuple
        ``(path, hash, size)`` for each line.

        :returns: iterator of (path, hash, size)
        

        Writes the ``RECORD`` file, using the ``paths`` iterable passed in. Any
        existing ``RECORD`` file is silently overwritten.

        prefix is used to determine when to write absolute paths.
        

        Checks that the hashes and sizes of the files in ``RECORD`` are
        matched by the files themselves. Returns a (possibly empty) list of
        mismatches. Each entry in the mismatch list will be a tuple consisting
        of the path, 'exists', 'size' or 'hash' according to what didn't match
        (existence is checked first, then size, then hash), the expected
        value and the actual value.
        

        A dictionary of shared locations whose keys are in the set 'prefix',
        'purelib', 'platlib', 'scripts', 'headers', 'data' and 'namespace'.
        The corresponding value is the absolute path of that category for
        this distribution, and takes into account any paths selected by the
        user at installation time (e.g. via command-line arguments). In the
        case of the 'namespace' key, this would be a list of absolute paths
        for the roots of namespace packages in this distribution.

        The first time this property is accessed, the relevant information is
        read from the SHARED file in the .dist-info directory.
        

        Write shared location information to the SHARED file in .dist-info.
        :param paths: A dictionary as described in the documentation for
        :meth:`shared_locations`.
        :param dry_run: If True, the action is logged but no file is actually
                        written.
        :return: The path of the file written to.
        

        Returns a path located under the ``.dist-info`` directory. Returns a
        string representing the path.

        :parameter path: a ``'/'``-separated path relative to the
                         ``.dist-info`` directory or an absolute path;
                         If *path* is an absolute path and doesn't start
                         with the ``.dist-info`` directory path,
                         a :class:`DistlibException` is raised
        :type path: str
        :rtype: str
        

        Iterates over the ``RECORD`` entries and returns paths for each line if
        the path is pointing to a file located in the ``.dist-info`` directory
        or one of its subdirectories.

        :returns: iterator of paths
        
Created with the *path* of the ``.egg-info`` directory or file provided
    to the constructor. It reads the metadata contained in the file itself, or
    if the given path happens to be a directory, the metadata is read from the
    file ``PKG-INFO`` under that directory.
Create a list of dependencies from a requires.txt file.

            *data*: the contents of a setuptools-produced requires.txt file.
            
Create a list of dependencies from a requires.txt file.

            *req_path*: the path to a setuptools-produced requires.txt file.
            

        Checks that the hashes and sizes of the files in ``RECORD`` are
        matched by the files themselves. Returns a (possibly empty) list of
        mismatches. Each entry in the mismatch list will be a tuple consisting
        of the path, 'exists', 'size' or 'hash' according to what didn't match
        (existence is checked first, then size, then hash), the expected
        value and the actual value.
        

        Iterates over the ``installed-files.txt`` entries and returns a tuple
        ``(path, hash, size)`` for each line.

        :returns: a list of (path, hash, size)
        

        Iterates over the ``installed-files.txt`` entries and returns paths for
        each line if the path is pointing to a file located in the
        ``.egg-info`` directory or one of its subdirectories.

        :parameter absolute: If *absolute* is ``True``, each returned path is
                          transformed into a local absolute path. Otherwise the
                          raw value from ``installed-files.txt`` is returned.
        :type absolute: boolean
        :returns: iterator of paths
        

    Represents a dependency graph between distributions.

    The dependency relationships are stored in an ``adjacency_list`` that maps
    distributions to a list of ``(other, label)`` tuples where  ``other``
    is a distribution and the edge is labeled with ``label`` (i.e. the version
    specifier, if such was provided). Also, for more efficient traversal, for
    every distribution ``x``, a list of predecessors is kept in
    ``reverse_list[x]``. An edge from distribution ``a`` to
    distribution ``b`` means that ``a`` depends on ``b``. If any missing
    dependencies are found, they are stored in ``missing``, which is a
    dictionary that maps distributions to a list of requirements that were not
    provided by any other distributions.
    
Add the *distribution* to the graph.

        :type distribution: :class:`distutils2.database.InstalledDistribution`
                            or :class:`distutils2.database.EggInfoDistribution`
        
Add an edge from distribution *x* to distribution *y* with the given
        *label*.

        :type x: :class:`distutils2.database.InstalledDistribution` or
                 :class:`distutils2.database.EggInfoDistribution`
        :type y: :class:`distutils2.database.InstalledDistribution` or
                 :class:`distutils2.database.EggInfoDistribution`
        :type label: ``str`` or ``None``
        

        Add a missing *requirement* for the given *distribution*.

        :type distribution: :class:`distutils2.database.InstalledDistribution`
                            or :class:`distutils2.database.EggInfoDistribution`
        :type requirement: ``str``
        
Prints only a subgraph
Writes a DOT output for the graph to the provided file *f*.

        If *skip_disconnected* is set to ``True``, then all distributions
        that are not dependent on any other distribution are skipped.

        :type f: has to support ``file``-like operations
        :type skip_disconnected: ``bool``
        

        Perform a topological sort of the graph.
        :return: A tuple, the first element of which is a topologically sorted
                 list of distributions, and the second element of which is a
                 list of distributions that cannot be sorted because they have
                 circular dependencies and so form a cycle.
        
Representation of the graph
Makes a dependency graph from the given distributions.

    :parameter dists: a list of distributions
    :type dists: list of :class:`distutils2.database.InstalledDistribution` and
                 :class:`distutils2.database.EggInfoDistribution` instances
    :rtype: a :class:`DependencyGraph` instance
    
Recursively generate a list of distributions from *dists* that are
    dependent on *dist*.

    :param dists: a list of distributions
    :param dist: a distribution, member of *dists* for which we are interested
    
Recursively generate a list of distributions from *dists* that are
    required by *dist*.

    :param dists: a list of distributions
    :param dist: a distribution, member of *dists* for which we are interested
                 in finding the dependencies.
    

    A convenience method for making a dist given just a name and version.
    

---


Class representing the list of files in a distribution.

Equivalent to distutils.filelist, but fixes some problems.


    A list of files built by exploring the filesystem and filtered by applying various
    patterns to what we find there.
    

        Initialise an instance.

        :param base: The base directory to explore under.
        
Find all files under the base and set ``allfiles`` to the absolute
        pathnames of files found.
        

        Add a file to the manifest.

        :param item: The pathname to add. This can be relative to the base.
        

        Add a list of files to the manifest.

        :param items: The pathnames to add. These can be relative to the base.
        

        Return sorted files in directory order
        
Clear all collected files.

        Process a directive which either adds some files from ``allfiles`` to
        ``files``, or removes some files from ``files``.

        :param directive: The directive to process. This should be in a format
                     compatible with distutils ``MANIFEST.in`` files:

                     http://docs.python.org/distutils/sourcedist.html#commands
        

        Validate a directive.
        :param directive: The directive to validate.
        :return: A tuple of action, patterns, thedir, dir_patterns
        
Select strings (presumably filenames) from 'self.files' that
        match 'pattern', a Unix-style wildcard (glob) pattern.

        Patterns are not quite the same as implemented by the 'fnmatch'
        module: '*' and '?'  match non-special characters, where "special"
        is platform-dependent: slash on Unix; colon, slash, and backslash on
        DOS/Windows; and colon on Mac OS.

        If 'anchor' is true (the default), then the pattern match is more
        stringent: "*.py" will match "foo.py" but not "foo/bar.py".  If
        'anchor' is false, both of these will match.

        If 'prefix' is supplied, then only filenames starting with 'prefix'
        (itself a pattern) and ending with 'pattern', with anything in between
        them, will match.  'anchor' is ignored in this case.

        If 'is_regex' is true, 'anchor' and 'prefix' are ignored, and
        'pattern' is assumed to be either a string containing a regex or a
        regex object -- no translation is done, the regex is just compiled
        and used as-is.

        Selected strings will be added to self.files.

        Return True if files are found.
        
Remove strings (presumably filenames) from 'files' that match
        'pattern'.

        Other parameters are the same as for 'include_pattern()', above.
        The list 'self.files' is modified in place. Return True if files are
        found.

        This API is public to allow e.g. exclusion of SCM subdirs, e.g. when
        packaging source distributions
        
Translate a shell-like wildcard pattern to a compiled regular
        expression.

        Return the compiled regex.  If 'is_regex' true,
        then 'pattern' is directly compiled to a regex (if it's a string)
        or just returned as-is (assumes it's a regex object).
        
Translate a shell-like glob pattern to a regular expression.

        Return a string containing the regex.  Differs from
        'fnmatch.translate()' in that '*' does not match "special characters"
        (which are platform-specific).
        

---


    This class represents a package index compatible with PyPI, the Python
    Package Index.
    

        Initialise an instance.

        :param url: The URL of the index. If not specified, the URL for PyPI is
                    used.
        

        Get the distutils command for interacting with PyPI configurations.
        :return: the command.
        

        Read the PyPI access configuration as supported by distutils. This populates
        ``username``, ``password``, ``realm`` and ``url`` attributes from the
        configuration.
        

        Save the PyPI access configuration. You must have set ``username`` and
        ``password`` attributes before calling this method.
        

        Check that ``username`` and ``password`` have been set, and raise an
        exception if not.
        

        Register a distribution on PyPI, using the provided metadata.

        :param metadata: A :class:`Metadata` instance defining at least a name
                         and version number for the distribution to be
                         registered.
        :return: The HTTP response received from PyPI upon submission of the
                request.
        

        Thread runner for reading lines of from a subprocess into a buffer.

        :param name: The logical name of the stream (used for logging only).
        :param stream: The stream to read from. This will typically a pipe
                       connected to the output stream of a subprocess.
        :param outbuf: The list to append the read lines to.
        

        Return a suitable command for signing a file.

        :param filename: The pathname to the file to be signed.
        :param signer: The identifier of the signer of the file.
        :param sign_password: The passphrase for the signer's
                              private key used for signing.
        :param keystore: The path to a directory which contains the keys
                         used in verification. If not specified, the
                         instance's ``gpg_home`` attribute is used instead.
        :return: The signing command as a list suitable to be
                 passed to :class:`subprocess.Popen`.
        

        Run a command in a child process , passing it any input data specified.

        :param cmd: The command to run.
        :param input_data: If specified, this must be a byte string containing
                           data to be sent to the child process.
        :return: A tuple consisting of the subprocess' exit code, a list of
                 lines read from the subprocess' ``stdout``, and a list of
                 lines read from the subprocess' ``stderr``.
        

        Sign a file.

        :param filename: The pathname to the file to be signed.
        :param signer: The identifier of the signer of the file.
        :param sign_password: The passphrase for the signer's
                              private key used for signing.
        :param keystore: The path to a directory which contains the keys
                         used in signing. If not specified, the instance's
                         ``gpg_home`` attribute is used instead.
        :return: The absolute pathname of the file where the signature is
                 stored.
        

        Upload a release file to the index.

        :param metadata: A :class:`Metadata` instance defining at least a name
                         and version number for the file to be uploaded.
        :param filename: The pathname of the file to be uploaded.
        :param signer: The identifier of the signer of the file.
        :param sign_password: The passphrase for the signer's
                              private key used for signing.
        :param filetype: The type of the file being uploaded. This is the
                        distutils command which produced that file, e.g.
                        ``sdist`` or ``bdist_wheel``.
        :param pyversion: The version of Python which the release relates
                          to. For code compatible with any Python, this would
                          be ``source``, otherwise it would be e.g. ``3.2``.
        :param keystore: The path to a directory which contains the keys
                         used in signing. If not specified, the instance's
                         ``gpg_home`` attribute is used instead.
        :return: The HTTP response received from PyPI upon submission of the
                request.
        

        Upload documentation to the index.

        :param metadata: A :class:`Metadata` instance defining at least a name
                         and version number for the documentation to be
                         uploaded.
        :param doc_dir: The pathname of the directory which contains the
                        documentation. This should be the directory that
                        contains the ``index.html`` for the documentation.
        :return: The HTTP response received from PyPI upon submission of the
                request.
        

        Return a suitable command for verifying a file.

        :param signature_filename: The pathname to the file containing the
                                   signature.
        :param data_filename: The pathname to the file containing the
                              signed data.
        :param keystore: The path to a directory which contains the keys
                         used in verification. If not specified, the
                         instance's ``gpg_home`` attribute is used instead.
        :return: The verifying command as a list suitable to be
                 passed to :class:`subprocess.Popen`.
        

        Verify a signature for a file.

        :param signature_filename: The pathname to the file containing the
                                   signature.
        :param data_filename: The pathname to the file containing the
                              signed data.
        :param keystore: The path to a directory which contains the keys
                         used in verification. If not specified, the
                         instance's ``gpg_home`` attribute is used instead.
        :return: True if the signature was verified, else False.
        

        This is a convenience method for downloading a file from an URL.
        Normally, this will be a file from the index, though currently
        no check is made for this (i.e. a file can be downloaded from
        anywhere).

        The method is just like the :func:`urlretrieve` function in the
        standard library, except that it allows digest computation to be
        done during download and checking that the downloaded data
        matched any expected value.

        :param url: The URL of the file to be downloaded (assumed to be
                    available via an HTTP GET request).
        :param destfile: The pathname where the downloaded file is to be
                         saved.
        :param digest: If specified, this must be a (hasher, value)
                       tuple, where hasher is the algorithm used (e.g.
                       ``'md5'``) and ``value`` is the expected value.
        :param reporthook: The same as for :func:`urlretrieve` in the
                           standard library.
        

        Send a standard library :class:`Request` to PyPI and return its
        response.

        :param req: The request to send.
        :return: The HTTP response from PyPI (a standard library HTTPResponse).
        

        Encode fields and files for posting to an HTTP server.

        :param fields: The fields to send as a list of (fieldname, value)
                       tuples.
        :param files: The files to send as a list of (fieldname, filename,
                      file_bytes) tuple.
        

---

Implementation of the Metadata for Python packages PEPs.

Supports all metadata formats (1.0, 1.1, 1.2, 1.3/2.1 and 2.2).

A required metadata is missing
Attempt to read or write metadata fields that are conflictual.
Unknown metadata version number.
A metadata value is invalid
Detect the best version depending on the fields used.
Return the distribution name with version.

    If for_filename is true, return a filename-escaped form.
The legacy metadata of a release.

    Supports versions 1.0, 1.1, 1.2, 2.0 and 1.3/2.1 (auto-detected). You can
    instantiate the class with one of these arguments (or none):
    - *path*, the path to a metadata file
    - *fileobj* give a file-like object with metadata as content
    - *mapping* is a dict-like object
    - *scheme* is a version scheme name
    

        Return the distribution name with version.

        If filesafe is true, return a filename-escaped form.
        
return True if name is a valid metadata key
Read the metadata values from a file path.
Read the metadata values from a file object.
Write the metadata fields to filepath.
Write the PKG-INFO format data to a file object.
Set metadata values from the given iterable `other` and kwargs.

        Behavior is like `dict.update`: If `other` has a ``keys`` method,
        they are looped over and ``self[key]`` is assigned ``other[key]``.
        Else, ``other`` is an iterable of ``(key, value)`` iterables.

        Keys that don't match a metadata field or that have an empty value are
        dropped.
        
Control then set a metadata field.
Get a metadata field.
Check if the metadata is compliant. If strict is True then raise if
        no Name or Version are provided
Return fields as a dict.

        Field names will be converted to use the underscore-lowercase style
        instead of hyphen-mixed case (i.e. home_page instead of Home-page).
        This is as per https://www.python.org/dev/peps/pep-0566/#id17.
        

    The metadata of a release. This implementation uses 2.1
    metadata where possible. If not possible, it wraps a LegacyMetadata
    instance which handles the key-value metadata format.
    

        Base method to get dependencies, given a set of extras
        to satisfy and an optional environment context.
        :param reqts: A list of sometimes-wanted dependencies,
                      perhaps dependent on extras and environment.
        :param extras: A list of optional components being requested.
        :param env: An optional environment for marker evaluation.
        

---


    Return all distribution names known by an index.
    :param url: The URL of the index.
    :return: A list of all known distribution names.
    

    A class to work around a bug in some Python 3.2.x releases.
    

    A base class for locators - things that locate distributions.
    

        Initialise an instance.
        :param scheme: Because locators look for most recent versions, they
                       need to know the version scheme to use. This specifies
                       the current PEP-recommended scheme - use ``'legacy'``
                       if you need to support existing distributions on PyPI.
        

        Return any errors which have occurred.
        

        Clear any errors which may have been logged.
        

        For a given project, get a dictionary mapping available versions to Distribution
        instances.

        This should be implemented in subclasses.

        If called from a locate() request, self.matcher will be set to a
        matcher for the requirement to satisfy, otherwise it will be None.
        

        Return all the distribution names known to this locator.
        

        For a given project, get a dictionary mapping available versions to Distribution
        instances.

        This calls _get_project to do all the work, and just implements a caching layer on top.
        

        Give an url a score which can be used to choose preferred URLs
        for a given project release.
        

        Choose one of two URLs where both are candidates for distribution
        archives for the same version of a distribution (for example,
        .tar.gz vs. zip).

        The current implementation favours https:// URLs over http://, archives
        from PyPI over those from other locations, wheel compatibility (if a
        wheel) and then the archive name.
        

        Attempt to split a filename in project name, version and Python version.
        

        See if a URL is a candidate for a download URL for a project (the URL
        has typically been scraped from an HTML page).

        If it is, a dictionary is returned with keys "name", "version",
        "filename" and "url"; otherwise, None is returned.
        

        Get a digest from a dictionary by looking at a "digests" dictionary
        or keys of the form 'algo_digest'.

        Returns a 2-tuple (algo, digest) if found, else None. Currently
        looks only for SHA256, then MD5.
        

        Update a result dictionary (the final result from _get_project) with a
        dictionary for a specific version, which typically holds information
        gleaned from a filename or URL for an archive for the distribution.
        

        Find the most recent distribution which matches the given
        requirement.

        :param requirement: A requirement of the form 'foo (1.0)' or perhaps
                            'foo (>= 1.0, < 2.0, != 1.3)'
        :param prereleases: If ``True``, allow pre-release versions
                            to be located. Otherwise, pre-release versions
                            are not returned.
        :return: A :class:`Distribution` instance, or ``None`` if no such
                 distribution could be located.
        

    This locator uses XML-RPC to locate distributions. It therefore
    cannot be used with simple mirrors (that only mirror file content).
    

        Initialise an instance.

        :param url: The URL to use for XML-RPC.
        :param kwargs: Passed to the superclass constructor.
        

        Return all the distribution names known to this locator.
        

    This locator uses PyPI's JSON interface. It's very limited in functionality
    and probably not worth using.
    

        Return all the distribution names known to this locator.
        

    This class represents a scraped HTML page.
    

(rel\\s*=\\s*(?:"(?P<rel1>[^"]*)"|'(?P<rel2>[^']*)'|(?P<rel3>[^>\\s\n]*))\\s+)?
href\\s*=\\s*(?:"(?P<url1>[^"]*)"|'(?P<url2>[^']*)'|(?P<url3>[^>\\s\n]*))
(\\s+rel\\s*=\\s*(?:"(?P<rel4>[^"]*)"|'(?P<rel5>[^']*)'|(?P<rel6>[^>\\s\n]*)))?

<base\s+href\s*=\s*['"]?([^'">]+)

        Initialise an instance with the Unicode page contents and the URL they
        came from.
        

        Return the URLs of all the links on a page together with information
        about their "rel" attribute, for determining which ones to treat as
        downloads and which ones to queue for further scraping.
        

    A locator which scrapes HTML pages to locate downloads for a distribution.
    This runs multiple threads to do the I/O; performance is at least as good
    as pip's PackageFinder, which works in an analogous fashion.
    

        Initialise an instance.
        :param url: The root URL to use for scraping.
        :param timeout: The timeout, in seconds, to be applied to requests.
                        This defaults to ``None`` (no timeout specified).
        :param num_workers: The number of worker threads you want to do I/O,
                            This defaults to 10.
        :param kwargs: Passed to the superclass.
        

        Threads are created only when get_project is called, and terminate
        before it returns. They are there primarily to parallelise I/O (i.e.
        fetching web pages).
        

        Tell all the threads to terminate (by sending a sentinel value) and
        wait for them to do so.
        

        Does an URL refer to a platform-specific download?
        

        See if an URL is a suitable download for a project.

        If it is, register information in the result dictionary (for
        _get_project) about the specific version it's for.

        Note that the return value isn't actually used other than as a boolean
        value.
        

        Determine whether a link URL from a referring page and with a
        particular "rel" attribute should be queued for scraping.
        

        Get a URL to fetch from the work queue, get the HTML page, examine its
        links for download candidates and candidates for further scraping.

        This is a handy method to run in a thread.
        

        Get the HTML for an URL, possibly from an in-memory cache.

        XXX TODO Note: this cache is never actually cleared. It's assumed that
        the data won't get stale over the lifetime of a locator instance (not
        necessarily true for the default_locator).
        

        Return all the distribution names known to this locator.
        

    This class locates distributions in a directory tree.
    

        Initialise an instance.
        :param path: The root of the directory tree to search.
        :param kwargs: Passed to the superclass constructor,
                       except for:
                       * recursive - if True (the default), subdirectories are
                         recursed into. If False, only the top-level directory
                         is searched,
        

        Should a filename be considered as a candidate for a distribution
        archive? As well as the filename, the directory which contains it
        is provided, though not used by the current implementation.
        

        Return all the distribution names known to this locator.
        

    This locator uses special extended metadata (not available on PyPI) and is
    the basis of performant dependency resolution in distlib. Other locators
    require archive downloads before dependencies can be determined! As you
    might imagine, that can be slow.
    

        Return all the distribution names known to this locator.
        

    This locator finds installed distributions in a path. It can be useful for
    adding to an :class:`AggregatingLocator`.
    

        Initialise an instance.

        :param distpath: A :class:`DistributionPath` instance to search.
        

    This class allows you to chain and/or merge a list of locators.
    

        Initialise an instance.

        :param locators: The list of locators to search.
        :param kwargs: Passed to the superclass constructor,
                       except for:
                       * merge - if False (the default), the first successful
                         search from any of the locators is returned. If True,
                         the results from all locators are merged (this can be
                         slow).
        

        Return all the distribution names known to this locator.
        

    Locate dependencies for distributions.
    

        Initialise an instance, using the specified locator
        to locate distributions.
        

        Add a distribution to the finder. This will update internal information
        about who provides what.
        :param dist: The distribution to add.
        

        Remove a distribution from the finder. This will update internal
        information about who provides what.
        :param dist: The distribution to remove.
        

        Get a version matcher for a requirement.
        :param reqt: The requirement
        :type reqt: str
        :return: A version matcher (an instance of
                 :class:`distlib.version.Matcher`).
        

        Find the distributions which can fulfill a requirement.

        :param reqt: The requirement.
         :type reqt: str
        :return: A set of distribution which can fulfill the requirement.
        

        Attempt to replace one provider with another. This is typically used
        when resolving dependencies from multiple sources, e.g. A requires
        (B >= 1.0) while C requires (B >= 1.1).

        For successful replacement, ``provider`` must meet all the requirements
        which ``other`` fulfills.

        :param provider: The provider we are trying to replace with.
        :param other: The provider we're trying to replace.
        :param problems: If False is returned, this will contain what
                         problems prevented replacement. This is currently
                         a tuple of the literal string 'cantreplace',
                         ``provider``, ``other``  and the set of requirements
                         that ``provider`` couldn't fulfill.
        :return: True if we can replace ``other`` with ``provider``, else
                 False.
        

        Find a distribution and all distributions it depends on.

        :param requirement: The requirement specifying the distribution to
                            find, or a Distribution instance.
        :param meta_extras: A list of meta extras such as :test:, :build: and
                            so on.
        :param prereleases: If ``True``, allow pre-release versions to be
                            returned - otherwise, don't return prereleases
                            unless they're all that's available.

        Return a set of :class:`Distribution` instances and a set of
        problems.

        The distributions returned should be such that they have the
        :attr:`required` attribute set to ``True`` if they were
        from the ``requirement`` passed to ``find()``, and they have the
        :attr:`build_time_dependency` attribute set to ``True`` unless they
        are post-installation dependencies of the ``requirement``.

        The problems should be a tuple consisting of the string
        ``'unsatisfied'`` and the requirement which couldn't be satisfied
        by any distribution known to the locator.
        

---


    Class to build and install from Wheel files (PEP 427).
    

        Initialise an instance using a (valid) filename.
        

        Build and return a filename from the various components.
        

        Build a wheel from files in specified paths, and use any specified tags
        when determining the name of the wheel.
        

        Determine whether an archive entry should be skipped when verifying
        or installing.
        

        Install a wheel to the specified paths. If kwarg ``warner`` is
        specified, it should be a callable, which will be called with two
        tuples indicating the wheel version of this software and the wheel
        version in the file, if there is a discrepancy in the versions.
        This can be used to issue any warnings to raise any exceptions.
        If kwarg ``lib_only`` is True, only the purelib/platlib files are
        installed, and the headers, scripts, data and dist-info metadata are
        not written. If kwarg ``bytecode_hashed_invalidation`` is True, written
        bytecode will try to use file-hash based invalidation (PEP-552) on
        supported interpreter versions (CPython 3.7+).

        The return value is a :class:`InstalledDistribution` instance unless
        ``options.lib_only`` is True, in which case the return value is ``None``.
        

        Determine if a wheel is compatible with the running system.
        

        Determine if a wheel is asserted as mountable by its metadata.
        

        Update the contents of a wheel in a generic way. The modifier should
        be a callable which expects a dictionary argument: its keys are
        archive-entry paths, and its values are absolute filesystem paths
        where the contents the corresponding archive entries can be found. The
        modifier is free to change the contents of the files pointed to, add
        new entries and remove entries, before returning. This method will
        extract the entire contents of the wheel to a temporary location, call
        the modifier, and then use the passed (and possibly updated)
        dictionary to write a new wheel. If ``dest_dir`` is specified, the new
        wheel is written there -- otherwise, the original wheel is overwritten.

        The modifier should return True if it updated the wheel, else False.
        This method returns the same value the modifier returns.
        

    Return (pyver, abi, arch) tuples compatible with this Python.
    

---



---

splituser('user[:passwd]@host[:port]') --> 'user[:passwd]', 'host[:port]'.
Matching according to RFC 6125, section 6.4.3

        http://tools.ietf.org/html/rfc6125#section-6.4.3
        
Verify that *cert* (in decoded format as returned by
        SSLSocket.getpeercert()) matches the *hostname*.  RFC 2818 and RFC 6125
        rules are followed, but IP addresses are not accepted for *hostname*.

        CertificateError is raised on failure. On success, the function
        returns nothing.
        

        A generic container for when multiple values need to be returned
        
Given a command, mode, and a PATH string, return the path which
        conforms to the given mode on the PATH, or None if there is no such
        file.

        `mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
        of os.environ.get("PATH"), or can be overridden with a custom search
        path.

        
Return a string identifying the Python implementation.
Imitates get_normal_name in tokenizer.c.

        The detect_encoding() function is used to detect the encoding that should
        be used to decode a Python source file.  It requires one argument, readline,
        in the same way as the tokenize() generator.

        It will call readline a maximum of twice, and return the encoding used
        (as a string) and a list of any lines (left as bytes) it has read in.

        It detects the encoding from the presence of a utf-8 bom or an encoding
        cookie as specified in pep-0263.  If both a bom and a cookie are present,
        but disagree, a SyntaxError will be raised.  If the encoding cookie is an
        invalid charset, raise a SyntaxError.  Note that if a utf-8 bom is found,
        'utf-8-sig' is returned.

        If no encoding is specified, then the default of 'utf-8' will be returned.
        
A converting dictionary wrapper.
A converting list wrapper.
A converting tuple wrapper.

        The configurator base class which defines some useful defaults.
        

            Resolve strings to objects using standard import and attribute
            syntax.
            
Default converter for the ext:// protocol.
Default converter for the cfg:// protocol.

            Convert values to an appropriate type. dicts, lists and tuples are
            replaced by their converting alternatives. Strings are checked to
            see if they have a conversion format and are converted if they do.
            
Configure an object with a user-supplied factory.
Utility function which converts lists to tuples.

---


        Is the cache stale for the given resource?

        :param resource: The :class:`Resource` being cached.
        :param path: The path of the resource in the cache.
        :return: True if the cache is stale.
        

        Get a resource into the cache,

        :param resource: A :class:`Resource` instance.
        :return: The pathname of the resource in the cache.
        

    A class representing an in-package resource, such as a data file. This is
    not normally instantiated by user code, but rather by a
    :class:`ResourceFinder` which manages the resource.
    

        Get the resource as a stream.

        This is not a property to make it obvious that it returns a new stream
        each time.
        

    Resource finder for file system resources.
    

    Resource finder for resources in .zip files.
    

    Return a resource finder for a package.
    :param package: The name of the package.
    :return: A :class:`ResourceFinder` instance for the package.
    

    Return a resource finder for a path, which should represent a container.

    :param path: The path.
    :return: A :class:`ResourceFinder` instance for the path.
    

---

Delegate class to provider progress reporting for the resolver.
Called before the resolution actually starts.
Called before each round of resolution starts.

        The index is zero-based.
        
Called before each round of resolution ends.

        This is NOT called if the resolution ends at this round. Use `ending`
        if you want to report finalization. The index is zero-based.
        
Called before the resolution ends successfully.
Called when adding a new requirement into the resolve criteria.

        :param requirement: The additional requirement to be applied to filter
            the available candidaites.
        :param parent: The candidate that requires ``requirement`` as a
            dependency, or None if ``requirement`` is one of the root
            requirements passed in from ``Resolver.resolve()``.
        
Called when starting to attempt requirement conflict resolution.

        :param causes: The information on the collision that caused the backtracking.
        
Called when rejecting a candidate during backtracking.
Called when adding a candidate to the potential solution.

---

Delegate class to provide the required interface for the resolver.
Given a requirement or candidate, return an identifier for it.

        This is used to identify, e.g. whether two requirements
        should have their specifier parts merged or a candidate matches a
        requirement via ``find_matches()``.
        
Produce a sort key for given requirement based on preference.

        As this is a sort key it will be called O(n) times per backtrack
        step, where n is the number of `identifier`s, if you have a check
        which is expensive in some sense. E.g. It needs to make O(n) checks
        per call or takes significant wall clock time, consider using
        `narrow_requirement_selection` to filter the `identifier`s, which
        is applied before this sort key is called.

        The preference is defined as "I think this requirement should be
        resolved first". The lower the return value is, the more preferred
        this group of arguments is.

        :param identifier: An identifier as returned by ``identify()``. This
            identifies the requirement being considered.
        :param resolutions: Mapping of candidates currently pinned by the
            resolver. Each key is an identifier, and the value is a candidate.
            The candidate may conflict with requirements from ``information``.
        :param candidates: Mapping of each dependency's possible candidates.
            Each value is an iterator of candidates.
        :param information: Mapping of requirement information of each package.
            Each value is an iterator of *requirement information*.
        :param backtrack_causes: Sequence of *requirement information* that are
            the requirements that caused the resolver to most recently
            backtrack.

        A *requirement information* instance is a named tuple with two members:

        * ``requirement`` specifies a requirement contributing to the current
          list of candidates.
        * ``parent`` specifies the candidate that provides (depended on) the
          requirement, or ``None`` to indicate a root requirement.

        The preference could depend on various issues, including (not
        necessarily in this order):

        * Is this package pinned in the current resolution result?
        * How relaxed is the requirement? Stricter ones should probably be
          worked on first? (I don't know, actually.)
        * How many possibilities are there to satisfy this requirement? Those
          with few left should likely be worked on first, I guess?
        * Are there any known conflicts for this requirement? We should
          probably work on those with the most known conflicts.

        A sortable value should be returned (this will be used as the ``key``
        parameter of the built-in sorting function). The smaller the value is,
        the more preferred this requirement is (i.e. the sorting function
        is called with ``reverse=False``).
        
Find all possible candidates that satisfy the given constraints.

        :param identifier: An identifier as returned by ``identify()``. All
            candidates returned by this method should produce the same
            identifier.
        :param requirements: A mapping of requirements that all returned
            candidates must satisfy. Each key is an identifier, and the value
            an iterator of requirements for that dependency.
        :param incompatibilities: A mapping of known incompatibile candidates of
            each dependency. Each key is an identifier, and the value an
            iterator of incompatibilities known to the resolver. All
            incompatibilities *must* be excluded from the return value.

        This should try to get candidates based on the requirements' types.
        For VCS, local, and archive requirements, the one-and-only match is
        returned, and for a "named" requirement, the index(es) should be
        consulted to find concrete candidates for this requirement.

        The return value should produce candidates ordered by preference; the
        most preferred candidate should come first. The return type may be one
        of the following:

        * A callable that returns an iterator that yields candidates.
        * An collection of candidates.
        * An iterable of candidates. This will be consumed immediately into a
          list of candidates.
        
Whether the given requirement can be satisfied by a candidate.

        The candidate is guaranteed to have been generated from the
        requirement.

        A boolean should be returned to indicate whether ``candidate`` is a
        viable solution to the requirement.
        
Get dependencies of a candidate.

        This should return a collection of requirements that `candidate`
        specifies as its dependencies.
        

        An optional method to narrow the selection of requirements being
        considered during resolution. This method is called O(1) time per
        backtrack step.

        :param identifiers: An iterable of `identifiers` as returned by
            ``identify()``. These identify all requirements currently being
            considered.
        :param resolutions: A mapping of candidates currently pinned by the
            resolver. Each key is an identifier, and the value is a candidate
            that may conflict with requirements from ``information``.
        :param candidates: A mapping of each dependency's possible candidates.
            Each value is an iterator of candidates.
        :param information: A mapping of requirement information for each package.
            Each value is an iterator of *requirement information*.
        :param backtrack_causes: A sequence of *requirement information* that are
            the requirements causing the resolver to most recently
            backtrack.

        A *requirement information* instance is a named tuple with two members:

        * ``requirement`` specifies a requirement contributing to the current
          list of candidates.
        * ``parent`` specifies the candidate that provides (is depended on for)
          the requirement, or ``None`` to indicate a root requirement.

        Must return a non-empty subset of `identifiers`, with the default
        implementation being to return `identifiers` unchanged. Those `identifiers`
        will then be passed to the sort key `get_preference` to pick the most
        prefered requirement to attempt to pin, unless `narrow_requirement_selection`
        returns only 1 requirement, in which case that will be used without
        calling the sort key `get_preference`.

        This method is designed to be used by the provider to optimize the
        dependency resolution, e.g. if a check cost is O(m) and it can be done
        against all identifiers at once then filtering the requirement selection
        here will cost O(m) but making it part of the sort key in `get_preference`
        will cost O(m*n), where n is the number of `identifiers`.

        Returns:
            Iterable[KT]: A non-empty subset of `identifiers`.
        

---

Resolution state in a round.
A graph structure with directed edges.
Return a shallow copy of this graph.
Add a new vertex to the graph.
Remove a vertex from the graph, disconnecting all edges from/to it.
Connect two existing vertices.

        Nothing happens if the vertices are already connected.
        
Wrap an iterator factory returned by `find_matches()`.

    Calling `iter()` on this class would invoke the underlying iterator
    factory, making it a "collection with ordering" that can be iterated
    through multiple times, but lacks random access methods presented in
    built-in Python sequence types.
    
Wrap an iterable returned by find_matches().

    This is essentially just a proxy to the underlying sequence that provides
    the same interface as `_FactoryIterableView`.
    
Build an iterable view from the value returned by `find_matches()`.

---



---

A base class for all exceptions raised by this module.

    Exceptions derived by this class should all be handled in this module. Any
    bubbling pass the resolver should be treated as a bug.
    

---

Stateful resolution object.

    This is designed as a one-off object that holds information to kick start
    the resolution process, and holds the results afterwards.
    
Push a new state into history.

        This new state will be used to hold resolution results of the next
        coming round.
        
Remove information from parents of criteria.

        Concretely, removes all values from each criterion's ``information``
        field that have one of ``parents`` as provider of the requirement.

        :param criteria: The criteria to update.
        :param parents: Identifiers for which to remove information from all criteria.
        
Perform backjumping.

        When we enter here, the stack is like this::

            [ state Z ]
            [ state Y ]
            [ state X ]
            .... earlier states are irrelevant.

        1. No pins worked for Z, so it does not have a pin.
        2. We want to reset state Y to unpinned, and pin another candidate.
        3. State X holds what state Y was before the pin, but does not
           have the incompatibility information gathered in state Y.

        Each iteration of the loop will:

        1.  Identify Z. The incompatibility is not always caused by the latest
            state. For example, given three requirements A, B and C, with
            dependencies A1, B1 and C1, where A1 and B1 are incompatible: the
            last state might be related to C, so we want to discard the
            previous state.
        2.  Discard Z.
        3.  Discard Y but remember its incompatibility information gathered
            previously, and the failure we're dealing with right now.
        4.  Push a new state Y' based on X, and apply the incompatibility
            information from Y to Y'.
        5a. If this causes Y' to conflict, we need to backtrack again. Make Y'
            the new Z and go back to step 2.
        5b. If the incompatibilities apply cleanly, end backtracking.
        
Extract causes from list of criterion and deduplicate
The thing that performs the actual resolution work.
Take a collection of constraints, spit out the resolution result.

        The return value is a representation to the final resolution result. It
        is a tuple subclass with three public members:

        * `mapping`: A dict of resolved candidates. Each key is an identifier
            of a requirement (as returned by the provider's `identify` method),
            and the value is the resolved candidate.
        * `graph`: A `DirectedGraph` instance representing the dependency tree.
            The vertices are keys of `mapping`, and each edge represents *why*
            a particular package is included. A special vertex `None` is
            included to represent parents of user-supplied requirements.
        * `criteria`: A dict of "criteria" that hold detailed information on
            how edges in the graph are derived. Each key is an identifier of a
            requirement, and the value is a `Criterion` instance.

        The following exceptions may be raised if a resolution cannot be found:

        * `ResolutionImpossible`: A resolution cannot be found for the given
            combination of requirements. The `causes` attribute of the
            exception is a list of (requirement, parent), giving the
            requirements that could not be satisfied.
        * `ResolutionTooDeep`: The dependency tree is too deeply nested and
            the resolver gave up. This is usually caused by a circular
            dependency, but you can try to resolve this by increasing the
            `max_rounds` argument.
        

---

The thing that performs the actual resolution work.
Take a collection of constraints, spit out the resolution result.

        This returns a representation of the final resolution state, with one
        guarenteed attribute ``mapping`` that contains resolved candidates as
        values. The keys are their respective identifiers.

        :param requirements: A collection of constraints.
        :param kwargs: Additional keyword arguments that subclasses may accept.

        :raises: ``self.base_exception`` or its subclass.
        

---

Representation of possible resolution results of a package.

    This holds three attributes:

    * `information` is a collection of `RequirementInformation` pairs.
      Each pair is a requirement contributing to this criterion, and the
      candidate that provides the requirement.
    * `incompatibilities` is a collection of all known not-to-work candidates
      to exclude from consideration.
    * `candidates` is a collection containing all possible candidates deducted
      from the union of contributing requirements and known incompatibilities.
      It should never be empty, except when the criterion is an attribute of a
      raised `RequirementsConflicted` (in which case it is always empty).

    .. note::
        This class is intended to be externally immutable. **Do not** mutate
        any of its attribute containers.
    

---



---

A protocol for the subprocess runner.
Will be raised if the backend cannot be imported in the hook process.
Will be raised on missing hooks (if a fallback can't be used).
May be raised by build_sdist if the backend indicates that it can't.
The default method of calling the wrapper subprocess.

    This uses :func:`subprocess.check_call` under the hood.
    
Call the subprocess while suppressing output.

    This uses :func:`subprocess.check_output` under the hood.
    
Normalise and check a backend path.

    Ensure that the requested backend path is specified as a relative path,
    and resolves to a location under the given source tree.

    Return an absolute version of the requested path.
    
A wrapper to call the build backend hooks for a source directory.

        :param source_dir: The source directory to invoke the build backend for
        :param build_backend: The build backend spec
        :param backend_path: Additional path entries for the build backend spec
        :param runner: The :ref:`subprocess runner <Subprocess Runners>` to use
        :param python_executable:
            The Python executable used to invoke the build backend
        
A context manager for temporarily overriding the default
        :ref:`subprocess runner <Subprocess Runners>`.

        :param runner: The new subprocess runner to use within the context.

        .. code-block:: python

            hook_caller = BuildBackendHookCaller(...)
            with hook_caller.subprocess_runner(quiet_subprocess_runner):
                ...
        
Return the list of optional features supported by the backend.
Get additional dependencies required for building a wheel.

        :param config_settings: The configuration settings for the build backend
        :returns: A list of :pep:`dependency specifiers <508>`.

        .. admonition:: Fallback

            If the build backend does not defined a hook with this name, an
            empty list will be returned.
        
Prepare a ``*.dist-info`` folder with metadata for this project.

        :param metadata_directory: The directory to write the metadata to
        :param config_settings: The configuration settings for the build backend
        :param _allow_fallback:
            Whether to allow the fallback to building a wheel and extracting
            the metadata from it. Should be passed as a keyword argument only.

        :returns: Name of the newly created subfolder within
                  ``metadata_directory``, containing the metadata.

        .. admonition:: Fallback

            If the build backend does not define a hook with this name and
            ``_allow_fallback`` is truthy, the backend will be asked to build a
            wheel via the ``build_wheel`` hook and the dist-info extracted from
            that will be returned.
        
Build a wheel from this project.

        :param wheel_directory: The directory to write the wheel to
        :param config_settings: The configuration settings for the build backend
        :param metadata_directory: The directory to reuse existing metadata from
        :returns:
            The name of the newly created wheel within ``wheel_directory``.

        .. admonition:: Interaction with fallback

            If the ``build_wheel`` hook was called in the fallback for
            :meth:`prepare_metadata_for_build_wheel`, the build backend would
            not be invoked. Instead, the previously built wheel will be copied
            to ``wheel_directory`` and the name of that file will be returned.
        
Get additional dependencies required for building an editable wheel.

        :param config_settings: The configuration settings for the build backend
        :returns: A list of :pep:`dependency specifiers <508>`.

        .. admonition:: Fallback

            If the build backend does not defined a hook with this name, an
            empty list will be returned.
        
Prepare a ``*.dist-info`` folder with metadata for this project.

        :param metadata_directory: The directory to write the metadata to
        :param config_settings: The configuration settings for the build backend
        :param _allow_fallback:
            Whether to allow the fallback to building a wheel and extracting
            the metadata from it. Should be passed as a keyword argument only.
        :returns: Name of the newly created subfolder within
                  ``metadata_directory``, containing the metadata.

        .. admonition:: Fallback

            If the build backend does not define a hook with this name and
            ``_allow_fallback`` is truthy, the backend will be asked to build a
            wheel via the ``build_editable`` hook and the dist-info
            extracted from that will be returned.
        
Build an editable wheel from this project.

        :param wheel_directory: The directory to write the wheel to
        :param config_settings: The configuration settings for the build backend
        :param metadata_directory: The directory to reuse existing metadata from
        :returns:
            The name of the newly created wheel within ``wheel_directory``.

        .. admonition:: Interaction with fallback

            If the ``build_editable`` hook was called in the fallback for
            :meth:`prepare_metadata_for_build_editable`, the build backend
            would not be invoked. Instead, the previously built wheel will be
            copied to ``wheel_directory`` and the name of that file will be
            returned.
        
Get additional dependencies required for building an sdist.

        :returns: A list of :pep:`dependency specifiers <508>`.
        
Build an sdist from this project.

        :returns:
            The name of the newly created sdist within ``wheel_directory``.
        

---

Wrappers to call pyproject.toml-based build backend hooks.


---

This is a subpackage because the directory is on sys.path for _in_process.py

The subpackage should stay as empty as possible to avoid shadowing modules that
the backend might import.


---

This is invoked in a subprocess to call the build backend hooks.

It expects:
- Command line args: hook_name, control_dir
- Environment variables:
      _PYPROJECT_HOOKS_BUILD_BACKEND=entry.point:spec
      _PYPROJECT_HOOKS_BACKEND_PATH=paths (separated with os.pathsep)
- control_dir/input.json:
  - {"kwargs": {...}}

Results:
- control_dir/output.json
  - {"return_val": ...}

Raised if we cannot import the backend
Raised if a hook is missing and we are not executing the fallback
Find and load the build backend
Implements the MetaPathFinder interface to locate modules in ``backend-path``.

    Since the environment provided by the frontend can contain all sorts of
    MetaPathFinders, the only way to ensure the backend is loaded from the
    right place is to prepend our own.
    
Return the list of options features supported by the backend.

    Returns a list of strings.
    The only possible value is 'build_editable'.
    
Invoke the optional get_requires_for_build_wheel hook

    Returns [] if the hook is not defined.
    
Invoke the optional get_requires_for_build_editable hook

    Returns [] if the hook is not defined.
    
Invoke optional prepare_metadata_for_build_wheel

    Implements a fallback by building a wheel if the hook isn't defined,
    unless _allow_fallback is False in which case HookMissing is raised.
    
Invoke optional prepare_metadata_for_build_editable

    Implements a fallback by building an editable wheel if the hook isn't
    defined, unless _allow_fallback is False in which case HookMissing is
    raised.
    
Identify the .dist-info folder inside a wheel ZipFile.
Extract the metadata from a wheel.

    Fallback for when the build backend does not
    define the 'get_wheel_metadata' hook.
    
Check for a wheel already built during the get_wheel_metadata hook.
Invoke the mandatory build_wheel hook.

    If a wheel was already built in the
    prepare_metadata_for_build_wheel fallback, this
    will copy it rather than rebuilding the wheel.
    
Invoke the optional build_editable hook.

    If a wheel was already built in the
    prepare_metadata_for_build_editable fallback, this
    will copy it rather than rebuilding the wheel.
    
Invoke the optional get_requires_for_build_wheel hook

    Returns [] if the hook is not defined.
    
Nothing should ever raise this exception
For internal use when backend raises UnsupportedOperation
Invoke the mandatory build_sdist hook.

---


    pygments.style
    ~~~~~~~~~~~~~~

    Basic style object.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


---


    pygments.scanner
    ~~~~~~~~~~~~~~~~

    This library implements a regex based scanner. Some languages
    like Pascal are easy to parse but have some keywords that
    depend on the context. Because of this it's impossible to lex
    that just by using a regular expression lexer like the
    `RegexLexer`.

    Have a look at the `DelphiLexer` to get an idea of how to use
    this scanner.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


    Raise if end of text is reached and the user
    tried to call a match function.
    

    Simple scanner

    All method patterns are regular expression strings (not
    compiled expressions!)
    

        :param text:    The text which should be scanned
        :param flags:   default regular expression flags
        
`True` if the scanner reached the end of text.

        Apply `pattern` on the current position and return
        the match object. (Doesn't touch pos). Use this for
        lookahead.
        
Apply a pattern on the current position and check
        if it patches. Doesn't touch pos.
        

        Scan the text for the given pattern and update pos/match
        and related fields. The return value is a boolean that
        indicates if the pattern matched. The matched value is
        stored on the instance as ``match``, the last value is
        stored as ``last``. ``start_pos`` is the position of the
        pointer before the pattern was matched, ``pos`` is the
        end position.
        
Scan exactly one char.

---


    pygments.util
    ~~~~~~~~~~~~~

    Utility functions.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.

Raised if one of the lookup functions didn't find a matching class.

    This exception will be raised by all option processing functions if
    the type or value of the argument is not correct.
    

    If the key `optname` from the dictionary is not in the sequence
    `allowed`, raise an error, otherwise return it.
    

    Intuitively, this is `options.get(optname, default)`, but restricted to
    Boolean value. The Booleans can be represented as string, in order to accept
    Boolean value from the command line arguments. If the key `optname` is
    present in the dictionary `options` and is not associated with a Boolean,
    raise an `OptionError`. If it is absent, `default` is returned instead.

    The valid string values for ``True`` are ``1``, ``yes``, ``true`` and
    ``on``, the ones for ``False`` are ``0``, ``no``, ``false`` and ``off``
    (matched case-insensitively).
    
As :func:`get_bool_opt`, but interpret the value as an integer.

    If the key `optname` from the dictionary `options` is a string,
    split it at whitespace and return it. If it is already a list
    or a tuple, it is returned as a list.
    
Return a static text analyser function that returns float values.
Check if the given regular expression matches the last part of the
    shebang if one exists.

        >>> from pygments.util import shebang_matches
        >>> shebang_matches('#!/usr/bin/env python', r'python(2\.\d)?')
        True
        >>> shebang_matches('#!/usr/bin/python2.4', r'python(2\.\d)?')
        True
        >>> shebang_matches('#!/usr/bin/python-ruby', r'python(2\.\d)?')
        False
        >>> shebang_matches('#!/usr/bin/python/ruby', r'python(2\.\d)?')
        False
        >>> shebang_matches('#!/usr/bin/startsomethingwith python',
        ...                 r'python(2\.\d)?')
        True

    It also checks for common windows executable file extensions::

        >>> shebang_matches('#!C:\\Python2.4\\Python.exe', r'python(2\.\d)?')
        True

    Parameters (``'-f'`` or ``'--foo'`` are ignored so ``'perl'`` does
    the same as ``'perl -e'``)

    Note that this method automatically searches the whole string (eg:
    the regular expression is wrapped in ``'^$'``)
    
Check if the doctype matches a regular expression (if present).

    Note that this method only checks the first part of a DOCTYPE.
    eg: 'html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"'
    
Check if the file looks like it has a html doctype.
Check if a doctype exists or if we have some tags.
Given a unicode character code with length greater than 16 bits,
    return the two 16 bit surrogate pair.
    
Formats a sequence of strings for output.

    Returns a list with duplicates removed from the iterable `it`.

    Order is preserved.
    
Generic class to defer some work.

    Handled specially in RegexLexerMeta, to support regex string construction at
    first use.
    
Decode *text* with guessed encoding.

    First try UTF-8; this should fail for non-UTF-8 encodings.
    Then try the preferred locale encoding.
    Fall back to latin-1, which always works.
    
Decode *text* coming from terminal *term*.

    First try the terminal encoding, if given.
    Then try UTF-8.  Then try the preferred locale encoding.
    Fall back to latin-1, which always works.
    
Return our best guess of encoding for the given *term*.

---


    pygments.sphinxext
    ~~~~~~~~~~~~~~~~~~

    Sphinx extension to generate automatic documentation of lexers,
    formatters and filters.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


    A directive to collect all lexers/formatters/filters and generate
    autoclass directives for them.
    
Generate a tabular overview of all lexers.

        The columns are the lexer name, the extensions handled by this lexer
        (or "None"), the aliases and a link to the lexer class.
Format a table row
Write a table separator row

---


    pygments.regexopt
    ~~~~~~~~~~~~~~~~~

    An algorithm that generates optimized regexes for matching long lists of
    literal strings.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.

Return a regex that matches any string in the sorted list of strings.
Return a compiled regex that matches any string in the given list.

    The strings to match must be literal strings, not regexes.  They will be
    regex-escaped.

    *prefix* and *suffix* are pre- and appended to the final regex.
    

---


    pygments.modeline
    ~~~~~~~~~~~~~~~~~

    A simple modeline parser (based on pymodeline).

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


    Scan the buffer for modelines and return filetype if one is found.
    

---


    pygments.filter
    ~~~~~~~~~~~~~~~

    Module that implements the default filter.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


    Use this method to apply an iterable of filters to
    a stream. If lexer is given it's forwarded to the
    filter, otherwise the filter receives `None`.
    

    Decorator that converts a function into a filter::

        @simplefilter
        def lowercase(self, lexer, stream, options):
            for ttype, value in stream:
                yield ttype, value.lower()
    

    Default filter. Subclass this class or use the `simplefilter`
    decorator to create own filters.
    

    Abstract class used by `simplefilter` to create simple
    function filters on the fly. The `simplefilter` decorator
    automatically creates subclasses of this class for
    functions passed to it.
    

---


    pygments.token
    ~~~~~~~~~~~~~~

    Basic token types and the standard tokens.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


    Return True if ``ttype`` is a subtype of ``other``.

    exists for backwards compatibility. use ``ttype in other`` now.
    

    Convert a string into a token type::

        >>> string_to_token('String.Double')
        Token.Literal.String.Double
        >>> string_to_token('Token.Literal.Number')
        Token.Literal.Number
        >>> string_to_token('')
        Token

    Tokens that are already tokens are returned unchanged:

        >>> string_to_token(String)
        Token.Literal.String
    

---


    pygments.console
    ~~~~~~~~~~~~~~~~

    Format colored console output.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


    Format ``text`` with a color and/or some attributes::

        color       normal color
        *color*     bold color
        _color_     underlined color
        +color+     blinking color
    

---


    pygments.lexer
    ~~~~~~~~~~~~~~

    Base lexer classes.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


    This metaclass automagically converts ``analyse_text`` methods into
    static methods which always return float values.
    

    Lexer for a specific language.

    See also :doc:`lexerdevelopment`, a high-level guide to writing
    lexers.

    Lexer classes have attributes used for choosing the most appropriate
    lexer based on various criteria.

    .. autoattribute:: name
       :no-value:
    .. autoattribute:: aliases
       :no-value:
    .. autoattribute:: filenames
       :no-value:
    .. autoattribute:: alias_filenames
    .. autoattribute:: mimetypes
       :no-value:
    .. autoattribute:: priority

    Lexers included in Pygments should have two additional attributes:

    .. autoattribute:: url
       :no-value:
    .. autoattribute:: version_added
       :no-value:

    Lexers included in Pygments may have additional attributes:

    .. autoattribute:: _example
       :no-value:

    You can pass options to the constructor. The basic options recognized
    by all lexers and processed by the base `Lexer` class are:

    ``stripnl``
        Strip leading and trailing newlines from the input (default: True).
    ``stripall``
        Strip all leading and trailing whitespace from the input
        (default: False).
    ``ensurenl``
        Make sure that the input ends with a newline (default: True).  This
        is required for some lexers that consume input linewise.

        .. versionadded:: 1.3

    ``tabsize``
        If given and greater than 0, expand tabs in the input (default: 0).
    ``encoding``
        If given, must be an encoding name. This encoding will be used to
        convert the input string to Unicode, if it is not already a Unicode
        string (default: ``'guess'``, which uses a simple UTF-8 / Locale /
        Latin1 detection.  Can also be ``'chardet'`` to use the chardet
        library, if it is installed.
    ``inencoding``
        Overrides the ``encoding`` if given.
    

        This constructor takes arbitrary options as keyword arguments.
        Every subclass must first process its own options and then call
        the `Lexer` constructor, since it processes the basic
        options like `stripnl`.

        An example looks like this:

        .. sourcecode:: python

           def __init__(self, **options):
               self.compress = options.get('compress', '')
               Lexer.__init__(self, **options)

        As these options must all be specifiable as strings (due to the
        command line usage), there are various utility functions
        available to help with that, see `Utilities`_.
        

        Add a new stream filter to this lexer.
        

        A static method which is called for lexer guessing.

        It should analyse the text and return a float in the range
        from ``0.0`` to ``1.0``.  If it returns ``0.0``, the lexer
        will not be selected as the most probable one, if it returns
        ``1.0``, it will be selected immediately.  This is used by
        `guess_lexer`.

        The `LexerMeta` metaclass automatically wraps this function so
        that it works like a static method (no ``self`` or ``cls``
        parameter) and the return value is automatically converted to
        `float`. If the return value is an object that is boolean `False`
        it's the same as if the return values was ``0.0``.
        
Apply preprocessing such as decoding the input, removing BOM and normalizing newlines.

        This method is the basic interface of a lexer. It is called by
        the `highlight()` function. It must process the text and return an
        iterable of ``(tokentype, value)`` pairs from `text`.

        Normally, you don't need to override this method. The default
        implementation processes the options recognized by all lexers
        (`stripnl`, `stripall` and so on), and then yields all tokens
        from `get_tokens_unprocessed()`, with the ``index`` dropped.

        If `unfiltered` is set to `True`, the filtering mechanism is
        bypassed even if filters are defined.
        

        This method should process the text and return an iterable of
        ``(index, tokentype, value)`` tuples where ``index`` is the starting
        position of the token within the input text.

        It must be overridden by subclasses. It is recommended to
        implement it as a generator to maximize effectiveness.
        

    This lexer takes two lexer as arguments. A root lexer and
    a language lexer. First everything is scanned using the language
    lexer, afterwards all ``Other`` tokens are lexed using the root
    lexer.

    The lexers from the ``template`` lexer package use this base lexer.
    

    Indicates that a state should include rules from another state.
    

    Indicates the a state should inherit from its superclass.
    

    Indicates a state combined from multiple states.
    

    A pseudo match object constructed from a string.
    

    Callback that yields multiple actions for each group in the match.
    

    Special singleton used for indicating the caller class.
    Used by ``using``.
    

    Callback that processes the match with a different lexer.

    The keyword arguments are forwarded to the lexer, except `state` which
    is handled separately.

    `state` specifies the state that the new lexer will start in, and can
    be an enumerable such as ('root', 'inline', 'string') or a simple
    string which is assumed to be on top of the root state.

    Note: For that to work, `_other` must not be an `ExtendedRegexLexer`.
    

    Indicates a state or state action (e.g. #pop) to apply.
    For example default('#pop') is equivalent to ('', Token, '#pop')
    Note that state tuples may be used as well.

    .. versionadded:: 2.0
    

    Indicates a list of literal words that is transformed into an optimized
    regex that matches any of the words.

    .. versionadded:: 2.0
    

    Metaclass for RegexLexer, creates the self._tokens attribute from
    self.tokens on the first instantiation.
    
Preprocess the regular expression component of a token definition.
Preprocess the token component of a token definition.
Preprocess the state transition action of a token definition.
Preprocess a single state definition.
Preprocess a dictionary of token definitions.

        Merge tokens from superclasses in MRO order, returning a single tokendef
        dictionary.

        Any state that is not defined by a subclass will be inherited
        automatically.  States that *are* defined by subclasses will, by
        default, override that state in the superclass.  If a subclass wishes to
        inherit definitions from a superclass, it can use the special value
        "inherit", which will cause the superclass' state definition to be
        included at that point in the state.
        
Instantiate cls after preprocessing its token definitions.

    Base for simple stateful regular expression-based lexers.
    Simplifies the lexing process so that you need only
    provide a list of states and regular expressions.
    

        Split ``text`` into (tokentype, text) pairs.

        ``stack`` is the initial stack (default: ``['root']``)
        

    A helper object that holds lexer position data.
    

    A RegexLexer that uses a context object to store its state.
    

        Split ``text`` into (tokentype, text) pairs.
        If ``context`` is given, use this lexer context instead.
        

    Helper for lexers which must combine the results of several
    sublexers.

    ``insertions`` is a list of ``(index, itokens)`` pairs.
    Each ``itokens`` iterable should be inserted at position
    ``index`` into the token stream given by the ``tokens``
    argument.

    The result is a combined token stream.

    TODO: clean up the code here.
    
Metaclass for ProfilingRegexLexer, collects regex timing info.
Drop-in replacement for RegexLexer that does profiling of its regexes.

---


    Pygments
    ~~~~~~~~

    Pygments is a syntax highlighting package written in Python.

    It is a generic syntax highlighter for general use in all kinds of software
    such as forum systems, wikis or other applications that need to prettify
    source code. Highlights are:

    * a wide range of common languages and markup formats is supported
    * special attention is paid to details, increasing quality by a fair amount
    * support for new languages and formats are added easily
    * a number of output formats, presently HTML, LaTeX, RTF, SVG, all image
      formats that PIL supports, and ANSI sequences
    * it is usable as a command-line tool and as a library
    * ... and it highlights even Brainfuck!

    The `Pygments master branch`_ is installable with ``easy_install Pygments==dev``.

    .. _Pygments master branch:
       https://github.com/pygments/pygments/archive/master.zip#egg=Pygments-dev

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


    Lex `code` with the `lexer` (must be a `Lexer` instance)
    and return an iterable of tokens. Currently, this only calls
    `lexer.get_tokens()`.
    

    Format ``tokens`` (an iterable of tokens) with the formatter ``formatter``
    (a `Formatter` instance).

    If ``outfile`` is given and a valid file object (an object with a
    ``write`` method), the result will be written to it, otherwise it
    is returned as a string.
    

    This is the most high-level highlighting function. It combines `lex` and
    `format` in one function.
    

---


    pygments.__main__
    ~~~~~~~~~~~~~~~~~

    Main entry point for ``python -m pygments``.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


---


    pygments.unistring
    ~~~~~~~~~~~~~~~~~~

    Strings of all Unicode characters of a certain category.
    Used for matching in Unicode-aware languages. Run to regenerate.

    Inspired by chartypes_create.py from the MoinMoin project.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


---


    pygments.formatter
    ~~~~~~~~~~~~~~~~~~

    Base formatter class.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


    Converts a token stream to text.

    Formatters should have attributes to help selecting them. These
    are similar to the corresponding :class:`~pygments.lexer.Lexer`
    attributes.

    .. autoattribute:: name
       :no-value:

    .. autoattribute:: aliases
       :no-value:

    .. autoattribute:: filenames
       :no-value:

    You can pass options as keyword arguments to the constructor.
    All formatters accept these basic options:

    ``style``
        The style to use, can be a string or a Style subclass
        (default: "default"). Not used by e.g. the
        TerminalFormatter.
    ``full``
        Tells the formatter to output a "full" document, i.e.
        a complete self-contained document. This doesn't have
        any effect for some formatters (default: false).
    ``title``
        If ``full`` is true, the title that should be used to
        caption the document (default: '').
    ``encoding``
        If given, must be an encoding name. This will be used to
        convert the Unicode token strings to byte strings in the
        output. If it is "" or None, Unicode strings will be written
        to the output file, which most file-like objects do not
        support (default: None).
    ``outencoding``
        Overrides ``encoding`` if given.

    

        As with lexers, this constructor takes arbitrary optional arguments,
        and if you override it, you should first process your own options, then
        call the base class implementation.
        

        This method must return statements or declarations suitable to define
        the current style for subsequent highlighted text (e.g. CSS classes
        in the `HTMLFormatter`).

        The optional argument `arg` can be used to modify the generation and
        is formatter dependent (it is standardized because it can be given on
        the command line).

        This method is called by the ``-S`` :doc:`command-line option <cmdline>`,
        the `arg` is then given by the ``-a`` option.
        

        This method must format the tokens from the `tokensource` iterable and
        write the formatted version to the file object `outfile`.

        Formatter options can control how exactly the tokens are converted.
        

---


    pygments.plugin
    ~~~~~~~~~~~~~~~

    Pygments plugin interface.

    lexer plugins::

        [pygments.lexers]
        yourlexer = yourmodule:YourLexer

    formatter plugins::

        [pygments.formatters]
        yourformatter = yourformatter:YourFormatter
        /.ext = yourformatter:YourFormatter

    As you can see, you can define extensions for the formatter
    with a leading slash.

    syntax plugins::

        [pygments.styles]
        yourstyle = yourstyle:YourStyle

    filter plugin::

        [pygments.filter]
        yourfilter = yourfilter:YourFilter


    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


---


    pygments.filters
    ~~~~~~~~~~~~~~~~

    Module containing filter lookup functions and default
    filters.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.

Lookup a filter by name. Return None if not found.
Return an instantiated filter.

    Options are passed to the filter initializer if wanted.
    Raise a ClassNotFound if not found.
    
Return a generator of all filter names.
Highlight special code tags in comments and docstrings.

    Options accepted:

    `codetags` : list of strings
       A list of strings that are flagged as code tags.  The default is to
       highlight ``XXX``, ``TODO``, ``FIXME``, ``BUG`` and ``NOTE``.

    .. versionchanged:: 2.13
       Now recognizes ``FIXME`` by default.
    
Convert mathematical symbols such as \\<longrightarrow> in Isabelle
    or \\longrightarrow in LaTeX into Unicode characters.

    This is mostly useful for HTML or console output when you want to
    approximate the source rendering you'd see in an IDE.

    Options accepted:

    `lang` : string
       The symbol language. Must be one of ``'isabelle'`` or
       ``'latex'``.  The default is ``'isabelle'``.
    
Convert keywords to lowercase or uppercase or capitalize them, which
    means first letter uppercase, rest lowercase.

    This can be useful e.g. if you highlight Pascal code and want to adapt the
    code to your styleguide.

    Options accepted:

    `case` : string
       The casing to convert keywords to. Must be one of ``'lower'``,
       ``'upper'`` or ``'capitalize'``.  The default is ``'lower'``.
    
Highlight a normal Name (and Name.*) token with a different token type.

    Example::

        filter = NameHighlightFilter(
            names=['foo', 'bar', 'baz'],
            tokentype=Name.Function,
        )

    This would highlight the names "foo", "bar" and "baz"
    as functions. `Name.Function` is the default token type.

    Options accepted:

    `names` : list of strings
      A list of names that should be given the different token type.
      There is no default.
    `tokentype` : TokenType or string
      A token type or a string containing a token type name that is
      used for highlighting the strings in `names`.  The default is
      `Name.Function`.
    
Raise an exception when the lexer generates an error token.

    Options accepted:

    `excclass` : Exception class
      The exception class to raise.
      The default is `pygments.filters.ErrorToken`.

    .. versionadded:: 0.8
    
Convert tabs, newlines and/or spaces to visible characters.

    Options accepted:

    `spaces` : string or bool
      If this is a one-character string, spaces will be replaces by this string.
      If it is another true value, spaces will be replaced by ``·`` (unicode
      MIDDLE DOT).  If it is a false value, spaces will not be replaced.  The
      default is ``False``.
    `tabs` : string or bool
      The same as for `spaces`, but the default replacement character is ``»``
      (unicode RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK).  The default value
      is ``False``.  Note: this will not work if the `tabsize` option for the
      lexer is nonzero, as tabs will already have been expanded then.
    `tabsize` : int
      If tabs are to be replaced by this filter (see the `tabs` option), this
      is the total number of characters that a tab should be expanded to.
      The default is ``8``.
    `newlines` : string or bool
      The same as for `spaces`, but the default replacement character is ``¶``
      (unicode PILCROW SIGN).  The default value is ``False``.
    `wstokentype` : bool
      If true, give whitespace the special `Whitespace` token type.  This allows
      styling the visible whitespace differently (e.g. greyed out), but it can
      disrupt background colors.  The default is ``True``.

    .. versionadded:: 0.8
    
Gobbles source code lines (eats initial characters).

    This filter drops the first ``n`` characters off every line of code.  This
    may be useful when the source code fed to the lexer is indented by a fixed
    amount of space that isn't desired in the output.

    Options accepted:

    `n` : int
       The number of characters to gobble.

    .. versionadded:: 1.2
    
Merges consecutive tokens with the same token type in the output
    stream of a lexer.

    .. versionadded:: 1.2
    

---



---


    pygments.styles
    ~~~~~~~~~~~~~~~

    Contains built-in styles.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


    Return a style class by its short name. The names of the builtin styles
    are listed in :data:`pygments.styles.STYLE_MAP`.

    Will raise :exc:`pygments.util.ClassNotFound` if no style of that name is
    found.
    
Return a generator for all styles by name, both builtin and plugin.

---



---


    pygments.lexers
    ~~~~~~~~~~~~~~~

    Pygments lexers.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.

Return whether the supplied file name fn matches pattern filename.
Load a lexer (and all others in the module too).
Return a generator of tuples in the form ``(name, aliases,
    filenames, mimetypes)`` of all know lexers.

    If *plugins* is true (the default), plugin lexers supplied by entrypoints
    are also returned.  Otherwise, only builtin ones are considered.
    

    Return the `Lexer` subclass that with the *name* attribute as given by
    the *name* argument.
    

    Return the `Lexer` subclass that has `alias` in its aliases list, without
    instantiating it.

    Like `get_lexer_by_name`, but does not instantiate the class.

    Will raise :exc:`pygments.util.ClassNotFound` if no lexer with that alias is
    found.

    .. versionadded:: 2.2
    

    Return an instance of a `Lexer` subclass that has `alias` in its
    aliases list. The lexer is given the `options` at its
    instantiation.

    Will raise :exc:`pygments.util.ClassNotFound` if no lexer with that alias is
    found.
    
Load a lexer from a file.

    This method expects a file located relative to the current working
    directory, which contains a Lexer class. By default, it expects the
    Lexer to be name CustomLexer; you can specify your own class name
    as the second argument to this function.

    Users should be very careful with the input, because this method
    is equivalent to running eval on the input file.

    Raises ClassNotFound if there are any problems importing the Lexer.

    .. versionadded:: 2.2
    
Get a lexer for a filename.

    If multiple lexers match the filename pattern, use ``analyse_text()`` to
    figure out which one is more appropriate.

    Returns None if not found.
    
Get a lexer for a filename.

    Return a `Lexer` subclass instance that has a filename pattern
    matching `fn`. The lexer is given the `options` at its
    instantiation.

    Raise :exc:`pygments.util.ClassNotFound` if no lexer for that filename
    is found.

    If multiple lexers match the filename pattern, use their ``analyse_text()``
    methods to figure out which one is more appropriate.
    

    Return a `Lexer` subclass instance that has `mime` in its mimetype
    list. The lexer is given the `options` at its instantiation.

    Will raise :exc:`pygments.util.ClassNotFound` if not lexer for that mimetype
    is found.
    
Return an iterator over all lexer classes.

    As :func:`guess_lexer()`, but only lexers which have a pattern in `filenames`
    or `alias_filenames` that matches `filename` are taken into consideration.

    :exc:`pygments.util.ClassNotFound` is raised if no lexer thinks it can
    handle the content.
    

    Return a `Lexer` subclass instance that's guessed from the text in
    `text`. For that, the :meth:`.analyse_text()` method of every known lexer
    class is called with the text as argument, and the lexer which returned the
    highest value will be instantiated and returned.

    :exc:`pygments.util.ClassNotFound` is raised if no lexer thinks it can
    handle the content.
    
Automatically import lexers.

---


    pygments.lexers.python
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexers for Python and related languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


    For Python source code (version 3.x).

    .. versionchanged:: 2.5
       This is now the default ``PythonLexer``.  It is still available as the
       alias ``Python3Lexer``.
    
(?:.|\n)*?
)',
             bygroups(String.Affix, String.Double),
             combined('rfstringescape', 'tdqf')),
            ("(?i)(rf|fr)(''')",
             bygroups(String.Affix, String.Single),
             combined('rfstringescape', 'tsqf')),
            ('(?i)(rf|fr)(")',
             bygroups(String.Affix, String.Double),
             combined('rfstringescape', 'dqf')),
            ("(?i)(rf|fr)(')",
             bygroups(String.Affix, String.Single),
             combined('rfstringescape', 'sqf')),
            # non-raw f-strings
            ('([fF])(
)',
             bygroups(String.Affix, String.Double), 'tdqs'),
            ("(?i)(rb|br|r)(''')",
             bygroups(String.Affix, String.Single), 'tsqs'),
            ('(?i)(rb|br|r)(")',
             bygroups(String.Affix, String.Double), 'dqs'),
            ("(?i)(rb|br|r)(')",
             bygroups(String.Affix, String.Single), 'sqs'),
            # non-raw strings
            ('([uU]?)(
)', bygroups(String.Affix, String.Double),
             combined('bytesescape', 'tdqs')),
            ("([bB])(''')", bygroups(String.Affix, String.Single),
             combined('bytesescape', 'tsqs')),
            ('([bB])(")', bygroups(String.Affix, String.Double),
             combined('bytesescape', 'dqs')),
            ("([bB])(')", bygroups(String.Affix, String.Single),
             combined('bytesescape', 'sqs')),

            (r'[^\S\n]+', Text),
            include('numbers'),
            (r'!=|==|<<|>>|:=|[-~+/*%=<>&^|.]', Operator),
            (r'[]{}:(),;[]', Punctuation),
            (r'(in|is|and|or|not)\b', Operator.Word),
            include('expr-keywords'),
            include('builtins'),
            include('magicfuncs'),
            include('magicvars'),
            include('name'),
        ],
        'expr-inside-fstring': [
            (r'[{([]', Punctuation, 'expr-inside-fstring-inner'),
            # without format specifier
            (r'(=\s*)?'         # debug (https://bugs.python.org/issue36817)
             r'(\![sraf])?'     # conversion
             r'\}', String.Interpol, '#pop'),
            # with format specifier
            # we'll catch the remaining '}' in the outer scope
            (r'(=\s*)?'         # debug (https://bugs.python.org/issue36817)
             r'(\![sraf])?'     # conversion
             r':', String.Interpol, '#pop'),
            (r'\s+', Whitespace),  # allow new lines
            include('expr'),
        ],
        'expr-inside-fstring-inner': [
            (r'[{([]', Punctuation, 'expr-inside-fstring-inner'),
            (r'[])}]', Punctuation, '#pop'),
            (r'\s+', Whitespace),  # allow new lines
            include('expr'),
        ],
        'expr-keywords': [
            # Based on https://docs.python.org/3/reference/expressions.html
            (words((
                'async for', 'await', 'else', 'for', 'if', 'lambda',
                'yield', 'yield from'), suffix=r'\b'),
             Keyword),
            (words(('True', 'False', 'None'), suffix=r'\b'), Keyword.Constant),
        ],
        'keywords': [
            (words((
                'assert', 'async', 'await', 'break', 'continue', 'del', 'elif',
                'else', 'except', 'finally', 'for', 'global', 'if', 'lambda',
                'pass', 'raise', 'nonlocal', 'return', 'try', 'while', 'yield',
                'yield from', 'as', 'with'), suffix=r'\b'),
             Keyword),
            (words(('True', 'False', 'None'), suffix=r'\b'), Keyword.Constant),
        ],
        'soft-keywords': [
            # `match`, `case` and `_` soft keywords
            (r'(^[ \t]*)'              # at beginning of line + possible indentation
             r'(match|case)\b'         # a possible keyword
             r'(?![ \t]*(?:'           # not followed by...
             r'[:,;=^&|@~)\]}]|(?:' +  # characters and keywords that mean this isn't
                                       # pattern matching (but None/True/False is ok)
             r'|'.join(k for k in keyword.kwlist if k[0].islower()) + r')\b))',
             bygroups(Text, Keyword), 'soft-keywords-inner'),
        ],
        'soft-keywords-inner': [
            # optional `_` keyword
            (r'(\s+)([^\n_]*)(_\b)', bygroups(Whitespace, using(this), Keyword)),
            default('#pop')
        ],
        'builtins': [
            (words((
                '__import__', 'abs', 'aiter', 'all', 'any', 'bin', 'bool', 'bytearray',
                'breakpoint', 'bytes', 'callable', 'chr', 'classmethod', 'compile',
                'complex', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval',
                'filter', 'float', 'format', 'frozenset', 'getattr', 'globals',
                'hasattr', 'hash', 'hex', 'id', 'input', 'int', 'isinstance',
                'issubclass', 'iter', 'len', 'list', 'locals', 'map', 'max',
                'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow',
                'print', 'property', 'range', 'repr', 'reversed', 'round', 'set',
                'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super',
                'tuple', 'type', 'vars', 'zip'), prefix=r'(?<!\.)', suffix=r'\b'),
             Name.Builtin),
            (r'(?<!\.)(self|Ellipsis|NotImplemented|cls)\b', Name.Builtin.Pseudo),
            (words((
                'ArithmeticError', 'AssertionError', 'AttributeError',
                'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning',
                'EOFError', 'EnvironmentError', 'Exception', 'FloatingPointError',
                'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
                'ImportWarning', 'IndentationError', 'IndexError', 'KeyError',
                'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError',
                'NotImplementedError', 'OSError', 'OverflowError',
                'PendingDeprecationWarning', 'ReferenceError', 'ResourceWarning',
                'RuntimeError', 'RuntimeWarning', 'StopIteration',
                'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',
                'TabError', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
                'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError',
                'UnicodeWarning', 'UserWarning', 'ValueError', 'VMSError',
                'Warning', 'WindowsError', 'ZeroDivisionError',
                # new builtin exceptions from PEP 3151
                'BlockingIOError', 'ChildProcessError', 'ConnectionError',
                'BrokenPipeError', 'ConnectionAbortedError', 'ConnectionRefusedError',
                'ConnectionResetError', 'FileExistsError', 'FileNotFoundError',
                'InterruptedError', 'IsADirectoryError', 'NotADirectoryError',
                'PermissionError', 'ProcessLookupError', 'TimeoutError',
                # others new in Python 3
                'StopAsyncIteration', 'ModuleNotFoundError', 'RecursionError',
                'EncodingWarning'),
                prefix=r'(?<!\.)', suffix=r'\b'),
             Name.Exception),
        ],
        'magicfuncs': [
            (words((
                '__abs__', '__add__', '__aenter__', '__aexit__', '__aiter__',
                '__and__', '__anext__', '__await__', '__bool__', '__bytes__',
                '__call__', '__complex__', '__contains__', '__del__', '__delattr__',
                '__delete__', '__delitem__', '__dir__', '__divmod__', '__enter__',
                '__eq__', '__exit__', '__float__', '__floordiv__', '__format__',
                '__ge__', '__get__', '__getattr__', '__getattribute__',
                '__getitem__', '__gt__', '__hash__', '__iadd__', '__iand__',
                '__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__',
                '__imul__', '__index__', '__init__', '__instancecheck__',
                '__int__', '__invert__', '__ior__', '__ipow__', '__irshift__',
                '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__',
                '__len__', '__length_hint__', '__lshift__', '__lt__', '__matmul__',
                '__missing__', '__mod__', '__mul__', '__ne__', '__neg__',
                '__new__', '__next__', '__or__', '__pos__', '__pow__',
                '__prepare__', '__radd__', '__rand__', '__rdivmod__', '__repr__',
                '__reversed__', '__rfloordiv__', '__rlshift__', '__rmatmul__',
                '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__',
                '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__',
                '__rxor__', '__set__', '__setattr__', '__setitem__', '__str__',
                '__sub__', '__subclasscheck__', '__truediv__',
                '__xor__'), suffix=r'\b'),
             Name.Function.Magic),
        ],
        'magicvars': [
            (words((
                '__annotations__', '__bases__', '__class__', '__closure__',
                '__code__', '__defaults__', '__dict__', '__doc__', '__file__',
                '__func__', '__globals__', '__kwdefaults__', '__module__',
                '__mro__', '__name__', '__objclass__', '__qualname__',
                '__self__', '__slots__', '__weakref__'), suffix=r'\b'),
             Name.Variable.Magic),
        ],
        'numbers': [
            (r'(\d(?:_?\d)*\.(?:\d(?:_?\d)*)?|(?:\d(?:_?\d)*)?\.\d(?:_?\d)*)'
             r'([eE][+-]?\d(?:_?\d)*)?', Number.Float),
            (r'\d(?:_?\d)*[eE][+-]?\d(?:_?\d)*j?', Number.Float),
            (r'0[oO](?:_?[0-7])+', Number.Oct),
            (r'0[bB](?:_?[01])+', Number.Bin),
            (r'0[xX](?:_?[a-fA-F0-9])+', Number.Hex),
            (r'\d(?:_?\d)*', Number.Integer),
        ],
        'name': [
            (r'@' + uni_name, Name.Decorator),
            (r'@', Operator),  # new matrix multiplication operator
            (uni_name, Name),
        ],
        'funcname': [
            include('magicfuncs'),
            (uni_name, Name.Function, '#pop'),
            default('#pop'),
        ],
        'classname': [
            (uni_name, Name.Class, '#pop'),
        ],
        'import': [
            (r'(\s+)(as)(\s+)', bygroups(Whitespace, Keyword, Whitespace)),
            (r'\.', Name.Namespace),
            (uni_name, Name.Namespace),
            (r'(\s*)(,)(\s*)', bygroups(Whitespace, Operator, Whitespace)),
            default('#pop')  # all else: go back
        ],
        'fromimport': [
            (r'(\s+)(import)\b', bygroups(Whitespace, Keyword.Namespace), '#pop'),
            (r'\.', Name.Namespace),
            # if None occurs here, it's "raise x from None", since None can
            # never be a module name
            (r'None\b', Keyword.Constant, '#pop'),
            (uni_name, Name.Namespace),
            default('#pop'),
        ],
        'rfstringescape': [
            (r'\{\{', String.Escape),
            (r'\}\}', String.Escape),
        ],
        'fstringescape': [
            include('rfstringescape'),
            include('stringescape'),
        ],
        'bytesescape': [
            (r'\\([\\abfnrtv"\']|\n|x[a-fA-F0-9]{2}|[0-7]{1,3})', String.Escape)
        ],
        'stringescape': [
            (r'\\(N\{.*?\}|u[a-fA-F0-9]{4}|U[a-fA-F0-9]{8})', String.Escape),
            include('bytesescape')
        ],
        'fstrings-single': fstring_rules(String.Single),
        'fstrings-double': fstring_rules(String.Double),
        'strings-single': innerstring_rules(String.Single),
        'strings-double': innerstring_rules(String.Double),
        'dqf': [
            (r'"', String.Double, '#pop'),
            (r'\\\\|\\"|\\\n', String.Escape),  # included here for raw strings
            include('fstrings-double')
        ],
        'sqf': [
            (r"'", String.Single, '#pop'),
            (r"\\\\|\\'|\\\n", String.Escape),  # included here for raw strings
            include('fstrings-single')
        ],
        'dqs': [
            (r'"', String.Double, '#pop'),
            (r'\\\\|\\"|\\\n', String.Escape),  # included here for raw strings
            include('strings-double')
        ],
        'sqs': [
            (r"'", String.Single, '#pop'),
            (r"\\\\|\\'|\\\n", String.Escape),  # included here for raw strings
            include('strings-single')
        ],
        'tdqf': [
            (r'
', String.Double, '#pop'),
            include('strings-double'),
            (r'\n', String.Double)
        ],
        'tsqs': [
            (r"'''", String.Single, '#pop'),
            include('strings-single'),
            (r'\n', String.Single)
        ],
    }

    def analyse_text(text):
        return shebang_matches(text, r'pythonw?(3(\.\d)?)?') or \
            'import ' in text[:1000]


Python3Lexer = PythonLexer


class Python2Lexer(RegexLexer):
    


    name = 'Python 2.x'
    url = 'https://www.python.org'
    aliases = ['python2', 'py2']
    filenames = []  # now taken over by PythonLexer (3.x)
    mimetypes = ['text/x-python2', 'application/x-python2']
    version_added = ''

    def innerstring_rules(ttype):
        return [
            # the old style '%s' % (...) string formatting
            (r'%(\(\w+\))?[-#0 +]*([0-9]+|[*])?(\.([0-9]+|[*]))?'
             '[hlL]?[E-GXc-giorsux%]', String.Interpol),
            # backslashes, quotes and formatting signs must be parsed one at a time
            (r'[^\\\'"%\n]+', ttype),
            (r'[\'"\\]', ttype),
            # unhandled string formatting sign
            (r'%', ttype),
            # newlines are an error (use "nl" state)
        ]

    tokens = {
        'root': [
            (r'\n', Whitespace),
            (r'^(\s*)([rRuUbB]{,2})(
)',
             bygroups(Whitespace, String.Affix, String.Doc)),
            (r"^(\s*)([rRuUbB]{,2})('''(?:.|\n)*?''')",
             bygroups(Whitespace, String.Affix, String.Doc)),
            (r'[^\S\n]+', Text),
            (r'\A#!.+$', Comment.Hashbang),
            (r'#.*$', Comment.Single),
            (r'[]{}:(),;[]', Punctuation),
            (r'\\\n', Text),
            (r'\\', Text),
            (r'(in|is|and|or|not)\b', Operator.Word),
            (r'!=|==|<<|>>|[-~+/*%=<>&^|.]', Operator),
            include('keywords'),
            (r'(def)((?:\s|\\\s)+)', bygroups(Keyword, Whitespace), 'funcname'),
            (r'(class)((?:\s|\\\s)+)', bygroups(Keyword, Whitespace), 'classname'),
            (r'(from)((?:\s|\\\s)+)', bygroups(Keyword.Namespace, Whitespace),
             'fromimport'),
            (r'(import)((?:\s|\\\s)+)', bygroups(Keyword.Namespace, Whitespace),
             'import'),
            include('builtins'),
            include('magicfuncs'),
            include('magicvars'),
            include('backtick'),
            ('([rR]|[uUbB][rR]|[rR][uUbB])(
)', bygroups(String.Affix, String.Double),
             combined('stringescape', 'tdqs')),
            ("([uUbB]?)(''')", bygroups(String.Affix, String.Single),
             combined('stringescape', 'tsqs')),
            ('([uUbB]?)(")', bygroups(String.Affix, String.Double),
             combined('stringescape', 'dqs')),
            ("([uUbB]?)(')", bygroups(String.Affix, String.Single),
             combined('stringescape', 'sqs')),
            include('name'),
            include('numbers'),
        ],
        'keywords': [
            (words((
                'assert', 'break', 'continue', 'del', 'elif', 'else', 'except',
                'exec', 'finally', 'for', 'global', 'if', 'lambda', 'pass',
                'print', 'raise', 'return', 'try', 'while', 'yield',
                'yield from', 'as', 'with'), suffix=r'\b'),
             Keyword),
        ],
        'builtins': [
            (words((
                '__import__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin',
                'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod',
                'cmp', 'coerce', 'compile', 'complex', 'delattr', 'dict', 'dir', 'divmod',
                'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float',
                'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'hex', 'id',
                'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len',
                'list', 'locals', 'long', 'map', 'max', 'min', 'next', 'object',
                'oct', 'open', 'ord', 'pow', 'property', 'range', 'raw_input', 'reduce',
                'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
                'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type',
                'unichr', 'unicode', 'vars', 'xrange', 'zip'),
                prefix=r'(?<!\.)', suffix=r'\b'),
             Name.Builtin),
            (r'(?<!\.)(self|None|Ellipsis|NotImplemented|False|True|cls'
             r')\b', Name.Builtin.Pseudo),
            (words((
                'ArithmeticError', 'AssertionError', 'AttributeError',
                'BaseException', 'DeprecationWarning', 'EOFError', 'EnvironmentError',
                'Exception', 'FloatingPointError', 'FutureWarning', 'GeneratorExit',
                'IOError', 'ImportError', 'ImportWarning', 'IndentationError',
                'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
                'MemoryError', 'NameError',
                'NotImplementedError', 'OSError', 'OverflowError', 'OverflowWarning',
                'PendingDeprecationWarning', 'ReferenceError',
                'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration',
                'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',
                'TabError', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
                'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError',
                'UnicodeWarning', 'UserWarning', 'ValueError', 'VMSError', 'Warning',
                'WindowsError', 'ZeroDivisionError'), prefix=r'(?<!\.)', suffix=r'\b'),
             Name.Exception),
        ],
        'magicfuncs': [
            (words((
                '__abs__', '__add__', '__and__', '__call__', '__cmp__', '__coerce__',
                '__complex__', '__contains__', '__del__', '__delattr__', '__delete__',
                '__delitem__', '__delslice__', '__div__', '__divmod__', '__enter__',
                '__eq__', '__exit__', '__float__', '__floordiv__', '__ge__', '__get__',
                '__getattr__', '__getattribute__', '__getitem__', '__getslice__', '__gt__',
                '__hash__', '__hex__', '__iadd__', '__iand__', '__idiv__', '__ifloordiv__',
                '__ilshift__', '__imod__', '__imul__', '__index__', '__init__',
                '__instancecheck__', '__int__', '__invert__', '__iop__', '__ior__',
                '__ipow__', '__irshift__', '__isub__', '__iter__', '__itruediv__',
                '__ixor__', '__le__', '__len__', '__long__', '__lshift__', '__lt__',
                '__missing__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__',
                '__nonzero__', '__oct__', '__op__', '__or__', '__pos__', '__pow__',
                '__radd__', '__rand__', '__rcmp__', '__rdiv__', '__rdivmod__', '__repr__',
                '__reversed__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__',
                '__rop__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
                '__rtruediv__', '__rxor__', '__set__', '__setattr__', '__setitem__',
                '__setslice__', '__str__', '__sub__', '__subclasscheck__', '__truediv__',
                '__unicode__', '__xor__'), suffix=r'\b'),
             Name.Function.Magic),
        ],
        'magicvars': [
            (words((
                '__bases__', '__class__', '__closure__', '__code__', '__defaults__',
                '__dict__', '__doc__', '__file__', '__func__', '__globals__',
                '__metaclass__', '__module__', '__mro__', '__name__', '__self__',
                '__slots__', '__weakref__'),
                suffix=r'\b'),
             Name.Variable.Magic),
        ],
        'numbers': [
            (r'(\d+\.\d*|\d*\.\d+)([eE][+-]?[0-9]+)?j?', Number.Float),
            (r'\d+[eE][+-]?[0-9]+j?', Number.Float),
            (r'0[0-7]+j?', Number.Oct),
            (r'0[bB][01]+', Number.Bin),
            (r'0[xX][a-fA-F0-9]+', Number.Hex),
            (r'\d+L', Number.Integer.Long),
            (r'\d+j?', Number.Integer)
        ],
        'backtick': [
            ('`.*?`', String.Backtick),
        ],
        'name': [
            (r'@[\w.]+', Name.Decorator),
            (r'[a-zA-Z_]\w*', Name),
        ],
        'funcname': [
            include('magicfuncs'),
            (r'[a-zA-Z_]\w*', Name.Function, '#pop'),
            default('#pop'),
        ],
        'classname': [
            (r'[a-zA-Z_]\w*', Name.Class, '#pop')
        ],
        'import': [
            (r'(?:[ \t]|\\\n)+', Text),
            (r'as\b', Keyword.Namespace),
            (r',', Operator),
            (r'[a-zA-Z_][\w.]*', Name.Namespace),
            default('#pop')  # all else: go back
        ],
        'fromimport': [
            (r'(?:[ \t]|\\\n)+', Text),
            (r'import\b', Keyword.Namespace, '#pop'),
            # if None occurs here, it's "raise x from None", since None can
            # never be a module name
            (r'None\b', Name.Builtin.Pseudo, '#pop'),
            # sadly, in "raise x from y" y will be highlighted as namespace too
            (r'[a-zA-Z_.][\w.]*', Name.Namespace),
            # anything else here also means "raise x from y" and is therefore
            # not an error
            default('#pop'),
        ],
        'stringescape': [
            (r'\\([\\abfnrtv"\']|\n|N\{.*?\}|u[a-fA-F0-9]{4}|'
             r'U[a-fA-F0-9]{8}|x[a-fA-F0-9]{2}|[0-7]{1,3})', String.Escape)
        ],
        'strings-single': innerstring_rules(String.Single),
        'strings-double': innerstring_rules(String.Double),
        'dqs': [
            (r'"', String.Double, '#pop'),
            (r'\\\\|\\"|\\\n', String.Escape),  # included here for raw strings
            include('strings-double')
        ],
        'sqs': [
            (r"'", String.Single, '#pop'),
            (r"\\\\|\\'|\\\n", String.Escape),  # included here for raw strings
            include('strings-single')
        ],
        'tdqs': [
            (r'
Auxiliary lexer for `PythonConsoleLexer`.

    Code tokens are output as ``Token.Other.Code``, traceback tokens as
    ``Token.Other.Traceback``.
    

    For Python console output or doctests, such as:

    .. sourcecode:: pycon

        >>> a = 'foo'
        >>> print(a)
        foo
        >>> 1 / 0
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        ZeroDivisionError: integer division or modulo by zero

    Additional options:

    `python3`
        Use Python 3 lexer for code.  Default is ``True``.

        .. versionadded:: 1.0
        .. versionchanged:: 2.5
           Now defaults to ``True``.
    

    For Python 3.x tracebacks, with support for chained exceptions.

    .. versionchanged:: 2.5
       This is now the default ``PythonTracebackLexer``.  It is still available
       as the alias ``Python3TracebackLexer``.
    

    For Python tracebacks.

    .. versionchanged:: 2.5
       This class has been renamed from ``PythonTracebackLexer``.
       ``PythonTracebackLexer`` now refers to the Python 3 variant.
    

    For Pyrex and Cython source code.
    
(?:.|\n)*?
', String, 'tdqs'),
            ("(?:[rR]|[uU][rR]|[rR][uU])'''", String, 'tsqs'),
            ('(?:[rR]|[uU][rR]|[rR][uU])"', String, 'dqs'),
            ("(?:[rR]|[uU][rR]|[rR][uU])'", String, 'sqs'),
            ('[uU]?
', String, '#pop'),
            include('strings'),
            include('nl')
        ],
        'tsqs': [
            (r"'''", String, '#pop'),
            include('strings'),
            include('nl')
        ],
    }


class DgLexer(RegexLexer):
    

    name = 'dg'
    aliases = ['dg']
    filenames = ['*.dg']
    mimetypes = ['text/x-dg']
    url = 'http://pyos.github.io/dg'
    version_added = '1.6'

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'#.*?$', Comment.Single),

            (r'(?i)0b[01]+', Number.Bin),
            (r'(?i)0o[0-7]+', Number.Oct),
            (r'(?i)0x[0-9a-f]+', Number.Hex),
            (r'(?i)[+-]?[0-9]+\.[0-9]+(e[+-]?[0-9]+)?j?', Number.Float),
            (r'(?i)[+-]?[0-9]+e[+-]?\d+j?', Number.Float),
            (r'(?i)[+-]?[0-9]+j?', Number.Integer),

            (r"(?i)(br|r?b?)'''", String, combined('stringescape', 'tsqs', 'string')),
            (r'(?i)(br|r?b?)
', String, '#pop')
        ],
        'tsqs': [
            (r"'''", String, '#pop')
        ],
    }


class NumPyLexer(PythonLexer):
    

---



---


    pygments.formatters
    ~~~~~~~~~~~~~~~~~~~

    Pygments formatters.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.

Return whether the supplied file name fn matches pattern filename.
Load a formatter (and all others in the module too).
Return a generator for all formatter classes.
Lookup a formatter by alias.

    Returns None if not found.
    

    Return an instance of a :class:`.Formatter` subclass that has `alias` in its
    aliases list. The formatter is given the `options` at its instantiation.

    Will raise :exc:`pygments.util.ClassNotFound` if no formatter with that
    alias is found.
    

    Return a `Formatter` subclass instance loaded from the provided file, relative
    to the current directory.

    The file is expected to contain a Formatter class named ``formattername``
    (by default, CustomFormatter). Users should be very careful with the input, because
    this method is equivalent to running ``eval()`` on the input file. The formatter is
    given the `options` at its instantiation.

    :exc:`pygments.util.ClassNotFound` is raised if there are any errors loading
    the formatter.

    .. versionadded:: 2.2
    

    Return a :class:`.Formatter` subclass instance that has a filename pattern
    matching `fn`. The formatter is given the `options` at its instantiation.

    Will raise :exc:`pygments.util.ClassNotFound` if no formatter for that filename
    is found.
    
Automatically import formatters.

---


The ``distro`` package (``distro`` stands for Linux Distribution) provides
information about the Linux distribution it runs on, such as a reliable
machine-readable distro ID, or version information.

It is the recommended replacement for Python's original
:py:func:`platform.linux_distribution` function, but it provides much more
functionality. An alternative implementation became necessary because Python
3.5 deprecated this function, and Python 3.8 removed it altogether. Its
predecessor function :py:func:`platform.dist` was already deprecated since
Python 2.6 and removed in Python 3.8. Still, there are many cases in which
access to OS distribution information is needed. See `Python issue 1322
<https://bugs.python.org/issue1322>`_ for more information.


    .. deprecated:: 1.6.0

        :func:`distro.linux_distribution()` is deprecated. It should only be
        used as a compatibility shim with Python's
        :py:func:`platform.linux_distribution()`. Please use :func:`distro.id`,
        :func:`distro.version` and :func:`distro.name` instead.

    Return information about the current OS distribution as a tuple
    ``(id_name, version, codename)`` with items as follows:

    * ``id_name``:  If *full_distribution_name* is false, the result of
      :func:`distro.id`. Otherwise, the result of :func:`distro.name`.

    * ``version``:  The result of :func:`distro.version`.

    * ``codename``:  The extra item (usually in parentheses) after the
      os-release version number, or the result of :func:`distro.codename`.

    The interface of this function is compatible with the original
    :py:func:`platform.linux_distribution` function, supporting a subset of
    its parameters.

    The data it returns may not exactly be the same, because it uses more data
    sources than the original function, and that may lead to different data if
    the OS distribution is not consistent across multiple data sources it
    provides (there are indeed such distributions ...).

    Another reason for differences is the fact that the :func:`distro.id`
    method normalizes the distro ID string to a reliable machine-readable value
    for a number of popular OS distributions.
    

    Return the distro ID of the current distribution, as a
    machine-readable string.

    For a number of OS distributions, the returned distro ID value is
    *reliable*, in the sense that it is documented and that it does not change
    across releases of the distribution.

    This package maintains the following reliable distro ID values:

    ==============  =========================================
    Distro ID       Distribution
    ==============  =========================================
    "ubuntu"        Ubuntu
    "debian"        Debian
    "rhel"          RedHat Enterprise Linux
    "centos"        CentOS
    "fedora"        Fedora
    "sles"          SUSE Linux Enterprise Server
    "opensuse"      openSUSE
    "amzn"          Amazon Linux
    "arch"          Arch Linux
    "buildroot"     Buildroot
    "cloudlinux"    CloudLinux OS
    "exherbo"       Exherbo Linux
    "gentoo"        GenToo Linux
    "ibm_powerkvm"  IBM PowerKVM
    "kvmibm"        KVM for IBM z Systems
    "linuxmint"     Linux Mint
    "mageia"        Mageia
    "mandriva"      Mandriva Linux
    "parallels"     Parallels
    "pidora"        Pidora
    "raspbian"      Raspbian
    "oracle"        Oracle Linux (and Oracle Enterprise Linux)
    "scientific"    Scientific Linux
    "slackware"     Slackware
    "xenserver"     XenServer
    "openbsd"       OpenBSD
    "netbsd"        NetBSD
    "freebsd"       FreeBSD
    "midnightbsd"   MidnightBSD
    "rocky"         Rocky Linux
    "aix"           AIX
    "guix"          Guix System
    "altlinux"      ALT Linux
    ==============  =========================================

    If you have a need to get distros for reliable IDs added into this set,
    or if you find that the :func:`distro.id` function returns a different
    distro ID for one of the listed distros, please create an issue in the
    `distro issue tracker`_.

    **Lookup hierarchy and transformations:**

    First, the ID is obtained from the following sources, in the specified
    order. The first available and non-empty value is used:

    * the value of the "ID" attribute of the os-release file,

    * the value of the "Distributor ID" attribute returned by the lsb_release
      command,

    * the first part of the file name of the distro release file,

    The so determined ID value then passes the following transformations,
    before it is returned by this method:

    * it is translated to lower case,

    * blanks (which should not be there anyway) are translated to underscores,

    * a normalization of the ID is performed, based upon
      `normalization tables`_. The purpose of this normalization is to ensure
      that the ID is as reliable as possible, even across incompatible changes
      in the OS distributions. A common reason for an incompatible change is
      the addition of an os-release file, or the addition of the lsb_release
      command, with ID values that differ from what was previously determined
      from the distro release file name.
    

    Return the name of the current OS distribution, as a human-readable
    string.

    If *pretty* is false, the name is returned without version or codename.
    (e.g. "CentOS Linux")

    If *pretty* is true, the version and codename are appended.
    (e.g. "CentOS Linux 7.1.1503 (Core)")

    **Lookup hierarchy:**

    The name is obtained from the following sources, in the specified order.
    The first available and non-empty value is used:

    * If *pretty* is false:

      - the value of the "NAME" attribute of the os-release file,

      - the value of the "Distributor ID" attribute returned by the lsb_release
        command,

      - the value of the "<name>" field of the distro release file.

    * If *pretty* is true:

      - the value of the "PRETTY_NAME" attribute of the os-release file,

      - the value of the "Description" attribute returned by the lsb_release
        command,

      - the value of the "<name>" field of the distro release file, appended
        with the value of the pretty version ("<version_id>" and "<codename>"
        fields) of the distro release file, if available.
    

    Return the version of the current OS distribution, as a human-readable
    string.

    If *pretty* is false, the version is returned without codename (e.g.
    "7.0").

    If *pretty* is true, the codename in parenthesis is appended, if the
    codename is non-empty (e.g. "7.0 (Maipo)").

    Some distributions provide version numbers with different precisions in
    the different sources of distribution information. Examining the different
    sources in a fixed priority order does not always yield the most precise
    version (e.g. for Debian 8.2, or CentOS 7.1).

    Some other distributions may not provide this kind of information. In these
    cases, an empty string would be returned. This behavior can be observed
    with rolling releases distributions (e.g. Arch Linux).

    The *best* parameter can be used to control the approach for the returned
    version:

    If *best* is false, the first non-empty version number in priority order of
    the examined sources is returned.

    If *best* is true, the most precise version number out of all examined
    sources is returned.

    **Lookup hierarchy:**

    In all cases, the version number is obtained from the following sources.
    If *best* is false, this order represents the priority order:

    * the value of the "VERSION_ID" attribute of the os-release file,
    * the value of the "Release" attribute returned by the lsb_release
      command,
    * the version number parsed from the "<version_id>" field of the first line
      of the distro release file,
    * the version number parsed from the "PRETTY_NAME" attribute of the
      os-release file, if it follows the format of the distro release files.
    * the version number parsed from the "Description" attribute returned by
      the lsb_release command, if it follows the format of the distro release
      files.
    

    Return the version of the current OS distribution as a tuple
    ``(major, minor, build_number)`` with items as follows:

    * ``major``:  The result of :func:`distro.major_version`.

    * ``minor``:  The result of :func:`distro.minor_version`.

    * ``build_number``:  The result of :func:`distro.build_number`.

    For a description of the *best* parameter, see the :func:`distro.version`
    method.
    

    Return the major version of the current OS distribution, as a string,
    if provided.
    Otherwise, the empty string is returned. The major version is the first
    part of the dot-separated version string.

    For a description of the *best* parameter, see the :func:`distro.version`
    method.
    

    Return the minor version of the current OS distribution, as a string,
    if provided.
    Otherwise, the empty string is returned. The minor version is the second
    part of the dot-separated version string.

    For a description of the *best* parameter, see the :func:`distro.version`
    method.
    

    Return the build number of the current OS distribution, as a string,
    if provided.
    Otherwise, the empty string is returned. The build number is the third part
    of the dot-separated version string.

    For a description of the *best* parameter, see the :func:`distro.version`
    method.
    

    Return a space-separated list of distro IDs of distributions that are
    closely related to the current OS distribution in regards to packaging
    and programming interfaces, for example distributions the current
    distribution is a derivative from.

    **Lookup hierarchy:**

    This information item is only provided by the os-release file.
    For details, see the description of the "ID_LIKE" attribute in the
    `os-release man page
    <http://www.freedesktop.org/software/systemd/man/os-release.html>`_.
    

    Return the codename for the release of the current OS distribution,
    as a string.

    If the distribution does not have a codename, an empty string is returned.

    Note that the returned codename is not always really a codename. For
    example, openSUSE returns "x86_64". This function does not handle such
    cases in any special way and just returns the string it finds, if any.

    **Lookup hierarchy:**

    * the codename within the "VERSION" attribute of the os-release file, if
      provided,

    * the value of the "Codename" attribute returned by the lsb_release
      command,

    * the value of the "<codename>" field of the distro release file.
    

    Return certain machine-readable information items about the current OS
    distribution in a dictionary, as shown in the following example:

    .. sourcecode:: python

        {
            'id': 'rhel',
            'version': '7.0',
            'version_parts': {
                'major': '7',
                'minor': '0',
                'build_number': ''
            },
            'like': 'fedora',
            'codename': 'Maipo'
        }

    The dictionary structure and keys are always the same, regardless of which
    information items are available in the underlying data sources. The values
    for the various keys are as follows:

    * ``id``:  The result of :func:`distro.id`.

    * ``version``:  The result of :func:`distro.version`.

    * ``version_parts -> major``:  The result of :func:`distro.major_version`.

    * ``version_parts -> minor``:  The result of :func:`distro.minor_version`.

    * ``version_parts -> build_number``:  The result of
      :func:`distro.build_number`.

    * ``like``:  The result of :func:`distro.like`.

    * ``codename``:  The result of :func:`distro.codename`.

    For a description of the *pretty* and *best* parameters, see the
    :func:`distro.version` method.
    

    Return a dictionary containing key-value pairs for the information items
    from the os-release file data source of the current OS distribution.

    See `os-release file`_ for details about these information items.
    

    Return a dictionary containing key-value pairs for the information items
    from the lsb_release command data source of the current OS distribution.

    See `lsb_release command output`_ for details about these information
    items.
    

    Return a dictionary containing key-value pairs for the information items
    from the distro release file data source of the current OS distribution.

    See `distro release file`_ for details about these information items.
    

    Return a dictionary containing key-value pairs for the information items
    from the distro release file data source of the current OS distribution.
    

    Return a single named information item from the os-release file data source
    of the current OS distribution.

    Parameters:

    * ``attribute`` (string): Key of the information item.

    Returns:

    * (string): Value of the information item, if the item exists.
      The empty string, if the item does not exist.

    See `os-release file`_ for details about these information items.
    

    Return a single named information item from the lsb_release command output
    data source of the current OS distribution.

    Parameters:

    * ``attribute`` (string): Key of the information item.

    Returns:

    * (string): Value of the information item, if the item exists.
      The empty string, if the item does not exist.

    See `lsb_release command output`_ for details about these information
    items.
    

    Return a single named information item from the distro release file
    data source of the current OS distribution.

    Parameters:

    * ``attribute`` (string): Key of the information item.

    Returns:

    * (string): Value of the information item, if the item exists.
      The empty string, if the item does not exist.

    See `distro release file`_ for details about these information items.
    

    Return a single named information item from the distro release file
    data source of the current OS distribution.

    Parameters:

    * ``attribute`` (string): Key of the information item.

    Returns:

    * (string): Value of the information item, if the item exists.
                The empty string, if the item does not exist.
    
A version of @property which caches the value.  On access, it calls the
        underlying function and sets the value in `__dict__` so future accesses
        will not re-call the property.
        

    Provides information about a OS distribution.

    This package creates a private module-global instance of this class with
    default initialization arguments, that is used by the
    `consolidated accessor functions`_ and `single source accessor functions`_.
    By using default initialization arguments, that module-global instance
    returns data about the current OS distribution (i.e. the distro this
    package runs on).

    Normally, it is not necessary to create additional instances of this class.
    However, in situations where control is needed over the exact data sources
    that are used, instances of this class can be created with a specific
    distro release file, or a specific os-release file, or without invoking the
    lsb_release command.
    

        The initialization method of this class gathers information from the
        available data sources, and stores that in private instance attributes.
        Subsequent access to the information items uses these private instance
        attributes, so that the data sources are read only once.

        Parameters:

        * ``include_lsb`` (bool): Controls whether the
          `lsb_release command output`_ is included as a data source.

          If the lsb_release command is not available in the program execution
          path, the data source for the lsb_release command will be empty.

        * ``os_release_file`` (string): The path name of the
          `os-release file`_ that is to be used as a data source.

          An empty string (the default) will cause the default path name to
          be used (see `os-release file`_ for details).

          If the specified or defaulted os-release file does not exist, the
          data source for the os-release file will be empty.

        * ``distro_release_file`` (string): The path name of the
          `distro release file`_ that is to be used as a data source.

          An empty string (the default) will cause a default search algorithm
          to be used (see `distro release file`_ for details).

          If the specified distro release file does not exist, or if no default
          distro release file can be found, the data source for the distro
          release file will be empty.

        * ``include_uname`` (bool): Controls whether uname command output is
          included as a data source. If the uname command is not available in
          the program execution path the data source for the uname command will
          be empty.

        * ``root_dir`` (string): The absolute path to the root directory to use
          to find distro-related information files. Note that ``include_*``
          parameters must not be enabled in combination with ``root_dir``.

        * ``include_oslevel`` (bool): Controls whether (AIX) oslevel command
          output is included as a data source. If the oslevel command is not
          available in the program execution path the data source will be
          empty.

        Public instance attributes:

        * ``os_release_file`` (string): The path name of the
          `os-release file`_ that is actually used as a data source. The
          empty string if no distro release file is used as a data source.

        * ``distro_release_file`` (string): The path name of the
          `distro release file`_ that is actually used as a data source. The
          empty string if no distro release file is used as a data source.

        * ``include_lsb`` (bool): The result of the ``include_lsb`` parameter.
          This controls whether the lsb information will be loaded.

        * ``include_uname`` (bool): The result of the ``include_uname``
          parameter. This controls whether the uname information will
          be loaded.

        * ``include_oslevel`` (bool): The result of the ``include_oslevel``
          parameter. This controls whether (AIX) oslevel information will be
          loaded.

        * ``root_dir`` (string): The result of the ``root_dir`` parameter.
          The absolute path to the root directory to use to find distro-related
          information files.

        Raises:

        * :py:exc:`ValueError`: Initialization parameters combination is not
           supported.

        * :py:exc:`OSError`: Some I/O issue with an os-release file or distro
          release file.

        * :py:exc:`UnicodeError`: A data source has unexpected characters or
          uses an unexpected encoding.
        
Return repr of all info

        Return information about the OS distribution that is compatible
        with Python's :func:`platform.linux_distribution`, supporting a subset
        of its parameters.

        For details, see :func:`distro.linux_distribution`.
        
Return the distro ID of the OS distribution, as a string.

        For details, see :func:`distro.id`.
        

        Return the name of the OS distribution, as a string.

        For details, see :func:`distro.name`.
        

        Return the version of the OS distribution, as a string.

        For details, see :func:`distro.version`.
        

        Return the version of the OS distribution, as a tuple of version
        numbers.

        For details, see :func:`distro.version_parts`.
        

        Return the major version number of the current distribution.

        For details, see :func:`distro.major_version`.
        

        Return the minor version number of the current distribution.

        For details, see :func:`distro.minor_version`.
        

        Return the build number of the current distribution.

        For details, see :func:`distro.build_number`.
        

        Return the IDs of distributions that are like the OS distribution.

        For details, see :func:`distro.like`.
        

        Return the codename of the OS distribution.

        For details, see :func:`distro.codename`.
        

        Return certain machine-readable information about the OS
        distribution.

        For details, see :func:`distro.info`.
        

        Return a dictionary containing key-value pairs for the information
        items from the os-release file data source of the OS distribution.

        For details, see :func:`distro.os_release_info`.
        

        Return a dictionary containing key-value pairs for the information
        items from the lsb_release command data source of the OS
        distribution.

        For details, see :func:`distro.lsb_release_info`.
        

        Return a dictionary containing key-value pairs for the information
        items from the distro release file data source of the OS
        distribution.

        For details, see :func:`distro.distro_release_info`.
        

        Return a dictionary containing key-value pairs for the information
        items from the uname command data source of the OS distribution.

        For details, see :func:`distro.uname_info`.
        

        Return AIX' oslevel command output.
        

        Return a single named information item from the os-release file data
        source of the OS distribution.

        For details, see :func:`distro.os_release_attr`.
        

        Return a single named information item from the lsb_release command
        output data source of the OS distribution.

        For details, see :func:`distro.lsb_release_attr`.
        

        Return a single named information item from the distro release file
        data source of the OS distribution.

        For details, see :func:`distro.distro_release_attr`.
        

        Return a single named information item from the uname command
        output data source of the OS distribution.

        For details, see :func:`distro.uname_attr`.
        

        Get the information items from the specified os-release file.

        Returns:
            A dictionary containing all information items.
        

        Parse the lines of an os-release file.

        Parameters:

        * lines: Iterable through the lines in the os-release file.
                 Each line must be a unicode string or a UTF-8 encoded byte
                 string.

        Returns:
            A dictionary containing all information items.
        

        Get the information items from the lsb_release command output.

        Returns:
            A dictionary containing all information items.
        

        Parse the output of the lsb_release command.

        Parameters:

        * lines: Iterable through the lines of the lsb_release output.
                 Each line must be a unicode string or a UTF-8 encoded byte
                 string.

        Returns:
            A dictionary containing all information items.
        

        Get the information items from the specified distro release file.

        Returns:
            A dictionary containing all information items.
        

        Parse a distro release file.

        Parameters:

        * filepath: Path name of the distro release file.

        Returns:
            A dictionary containing all information items.
        

        Parse a line from a distro release file.

        Parameters:
        * line: Line from the distro release file. Must be a unicode string
                or a UTF-8 encoded byte string.

        Returns:
            A dictionary containing all information items.
        

---



---



---

Base class for some exceptions raised while unpacking.

    NOTE: unpack may raise exception other than subclass of
    UnpackException.  If you want to catch all error, catch
    Exception instead.
    
Invalid msgpack format
Too nested
ExtraData is raised when there is trailing data.

    This exception is raised while only one-shot (not streaming)
    unpack.
    

---

Fallback pure Python implementation of msgpack

    Unpack an object from `packed`.

    Raises ``ExtraData`` when *packed* contains extra bytes.
    Raises ``ValueError`` when *packed* is incomplete.
    Raises ``FormatError`` when *packed* is not valid msgpack.
    Raises ``StackError`` when *packed* contains too nested.
    Other exceptions can be raised during unpacking.

    See :class:`Unpacker` for options.
    
Streaming unpacker.

    Arguments:

    :param file_like:
        File-like object having `.read(n)` method.
        If specified, unpacker reads serialized data from it and `.feed()` is not usable.

    :param int read_size:
        Used as `file_like.read(read_size)`. (default: `min(16*1024, max_buffer_size)`)

    :param bool use_list:
        If true, unpack msgpack array to Python list.
        Otherwise, unpack to Python tuple. (default: True)

    :param bool raw:
        If true, unpack msgpack raw to Python bytes.
        Otherwise, unpack to Python str by decoding with UTF-8 encoding (default).

    :param int timestamp:
        Control how timestamp type is unpacked:

            0 - Timestamp
            1 - float  (Seconds from the EPOCH)
            2 - int  (Nanoseconds from the EPOCH)
            3 - datetime.datetime  (UTC).

    :param bool strict_map_key:
        If true (default), only str or bytes are accepted for map (dict) keys.

    :param object_hook:
        When specified, it should be callable.
        Unpacker calls it with a dict argument after unpacking msgpack map.
        (See also simplejson)

    :param object_pairs_hook:
        When specified, it should be callable.
        Unpacker calls it with a list of key-value pairs after unpacking msgpack map.
        (See also simplejson)

    :param str unicode_errors:
        The error handler for decoding unicode. (default: 'strict')
        This option should be used only when you have msgpack data which
        contains invalid UTF-8 string.

    :param int max_buffer_size:
        Limits size of data waiting unpacked.  0 means 2**32-1.
        The default value is 100*1024*1024 (100MiB).
        Raises `BufferFull` exception when it is insufficient.
        You should set this parameter when unpacking data from untrusted source.

    :param int max_str_len:
        Deprecated, use *max_buffer_size* instead.
        Limits max length of str. (default: max_buffer_size)

    :param int max_bin_len:
        Deprecated, use *max_buffer_size* instead.
        Limits max length of bin. (default: max_buffer_size)

    :param int max_array_len:
        Limits max length of array.
        (default: max_buffer_size)

    :param int max_map_len:
        Limits max length of map.
        (default: max_buffer_size//2)

    :param int max_ext_len:
        Deprecated, use *max_buffer_size* instead.
        Limits max size of ext type.  (default: max_buffer_size)

    Example of streaming deserialize from file-like object::

        unpacker = Unpacker(file_like)
        for o in unpacker:
            process(o)

    Example of streaming deserialize from socket::

        unpacker = Unpacker()
        while True:
            buf = sock.recv(1024**2)
            if not buf:
                break
            unpacker.feed(buf)
            for o in unpacker:
                process(o)

    Raises ``ExtraData`` when *packed* contains extra bytes.
    Raises ``OutOfData`` when *packed* is incomplete.
    Raises ``FormatError`` when *packed* is not valid msgpack.
    Raises ``StackError`` when *packed* contains too nested.
    Other exceptions can be raised during unpacking.
    
Gets rid of the used parts of the buffer.

    MessagePack Packer

    Usage::

        packer = Packer()
        astream.write(packer.pack(a))
        astream.write(packer.pack(b))

    Packer's constructor has some keyword arguments:

    :param default:
        When specified, it should be callable.
        Convert user type to builtin type that Packer supports.
        See also simplejson's document.

    :param bool use_single_float:
        Use single precision float type for float. (default: False)

    :param bool autoreset:
        Reset buffer after each pack and return its content as `bytes`. (default: True).
        If set this to false, use `bytes()` to get content and `.reset()` to clear buffer.

    :param bool use_bin_type:
        Use bin type introduced in msgpack spec 2.0 for bytes.
        It also enables str8 type for unicode. (default: True)

    :param bool strict_types:
        If set to true, types will be checked to be exact. Derived classes
        from serializable types will not be serialized and will be
        treated as unsupported type and forwarded to default.
        Additionally tuples will not be serialized as lists.
        This is useful when trying to implement accurate serialization
        for python types.

    :param bool datetime:
        If set to true, datetime with tzinfo is packed into Timestamp type.
        Note that the tzinfo is stripped in the timestamp.
        You can get UTC datetime with `timestamp=3` option of the Unpacker.

    :param str unicode_errors:
        The error handler for encoding unicode. (default: 'strict')
        DO NOT USE THIS!!  This option is kept for very specific usage.

    :param int buf_size:
        Internal buffer size. This option is used only for C implementation.
    
Return internal buffer contents as bytes object
Reset internal buffer.

        This method is useful only when autoreset=False.
        
Return view of internal buffer.

---

ExtType represents ext type in msgpack.
Timestamp represents the Timestamp extension type in msgpack.

    When built with Cython, msgpack uses C methods to pack and unpack `Timestamp`.
    When using pure-Python msgpack, :func:`to_bytes` and :func:`from_bytes` are used to pack and
    unpack `Timestamp`.

    This class is immutable: Do not override seconds and nanoseconds.
    
Initialize a Timestamp object.

        :param int seconds:
            Number of seconds since the UNIX epoch (00:00:00 UTC Jan 1 1970, minus leap seconds).
            May be negative.

        :param int nanoseconds:
            Number of nanoseconds to add to `seconds` to get fractional time.
            Maximum is 999_999_999.  Default is 0.

        Note: Negative times (before the UNIX epoch) are represented as neg. seconds + pos. ns.
        
String representation of Timestamp.
Check for equality with another Timestamp object
not-equals method (see :func:`__eq__()`)
Unpack bytes into a `Timestamp` object.

        Used for pure-Python msgpack unpacking.

        :param b: Payload from msgpack ext message with code -1
        :type b: bytes

        :returns: Timestamp object unpacked from msgpack ext payload
        :rtype: Timestamp
        
Pack this Timestamp object into bytes.

        Used for pure-Python msgpack packing.

        :returns data: Payload for EXT message with code -1 (timestamp type)
        :rtype: bytes
        
Create a Timestamp from posix timestamp in seconds.

        :param unix_float: Posix timestamp in seconds.
        :type unix_float: int or float
        
Get the timestamp as a floating-point value.

        :returns: posix timestamp
        :rtype: float
        
Create a Timestamp from posix timestamp in nanoseconds.

        :param int unix_ns: Posix timestamp in nanoseconds.
        :rtype: Timestamp
        
Get the timestamp as a unixtime in nanoseconds.

        :returns: posix timestamp in nanoseconds
        :rtype: int
        
Get the timestamp as a UTC datetime.

        :rtype: `datetime.datetime`
        
Create a Timestamp from datetime with tzinfo.

        :rtype: Timestamp
        

---


    Pack object `o` and write it to `stream`

    See :class:`Packer` for options.
    

    Pack object `o` and return packed bytes

    See :class:`Packer` for options.
    

    Unpack an object from `stream`.

    Raises `ExtraData` when `stream` contains extra bytes.
    See :class:`Unpacker` for options.
    

---


requests.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Requests' exceptions.

There was an ambiguous exception that occurred while handling your
    request.
    
Initialize RequestException with `request` and `response` objects.
A JSON error occurred.
Couldn't decode the text into json

        Construct the JSONDecodeError instance first with all
        args. Then use it's args to construct the IOError so that
        the json specific args aren't used as IOError specific args
        and the error message from JSONDecodeError is preserved.
        

        The __reduce__ method called when pickling the object must
        be the one from the JSONDecodeError (be it json/simplejson)
        as it expects all the arguments for instantiation, not just
        one like the IOError, and the MRO would by default call the
        __reduce__ method from the IOError due to the inheritance order.
        
An HTTP error occurred.
A Connection error occurred.
A proxy error occurred.
An SSL error occurred.
The request timed out.

    Catching this error will catch both
    :exc:`~requests.exceptions.ConnectTimeout` and
    :exc:`~requests.exceptions.ReadTimeout` errors.
    
The request timed out while trying to connect to the remote server.

    Requests that produced this error are safe to retry.
    
The server did not send any data in the allotted amount of time.
A valid URL is required to make a request.
Too many redirects.
The URL scheme (e.g. http or https) is missing.
The URL scheme provided is either invalid or unsupported.
The URL provided was somehow invalid.
The header value provided was somehow invalid.
The proxy URL provided is invalid.
The server declared chunked encoding but sent an invalid chunk.
Failed to decode response content.
The content for this response was already consumed.
Custom retries logic failed
Requests encountered an error when trying to rewind a body.
Base warning for Requests.
A file was opened in text mode, but Requests determined its binary length.
An imported dependency doesn't match the expected version range.

---


requests.auth
~~~~~~~~~~~~~

This module contains the authentication handlers for Requests.

Returns a Basic Auth string.
Base class that all auth implementations derive from
Attaches HTTP Basic Authentication to the given Request object.
Attaches HTTP Proxy Authentication to a given Request object.
Attaches HTTP Digest Authentication to the given Request object.

        :rtype: str
        
Reset num_401_calls counter on redirects.

        Takes the given response and tries digest-auth, if needed.

        :rtype: requests.Response
        

---


requests.api
~~~~~~~~~~~~

This module implements the Requests API.

:copyright: (c) 2012 by Kenneth Reitz.
:license: Apache2, see LICENSE for more details.

Constructs and sends a :class:`Request <Request>`.

    :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content_type'`` is a string
        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
        to add for the file.
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read
        timeout) <timeouts>` tuple.
    :type timeout: float or tuple
    :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
    :type allow_redirects: bool
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    Usage::

      >>> import requests
      >>> req = requests.request('GET', 'https://httpbin.org/get')
      >>> req
      <Response [200]>
    
Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
Sends an OPTIONS request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
Sends a HEAD request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes. If
        `allow_redirects` is not provided, it will be set to `False` (as
        opposed to the default :meth:`request` behavior).
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
Sends a PUT request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
Sends a PATCH request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
Sends a DELETE request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    

---


requests.adapters
~~~~~~~~~~~~~~~~~

This module contains the transport adapters that Requests uses to define
and maintain connections.

The Base Transport Adapter
Sends PreparedRequest object. Returns Response object.

        :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
        :param stream: (optional) Whether to stream the request content.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use
        :param cert: (optional) Any user-provided SSL certificate to be trusted.
        :param proxies: (optional) The proxies dictionary to apply to the request.
        
Cleans up adapter specific items.
The built-in HTTP Adapter for urllib3.

    Provides a general-case interface for Requests sessions to contact HTTP and
    HTTPS urls by implementing the Transport Adapter interface. This class will
    usually be created by the :class:`Session <Session>` class under the
    covers.

    :param pool_connections: The number of urllib3 connection pools to cache.
    :param pool_maxsize: The maximum number of connections to save in the pool.
    :param max_retries: The maximum number of retries each connection
        should attempt. Note, this applies only to failed DNS lookups, socket
        connections and connection timeouts, never to requests where data has
        made it to the server. By default, Requests does not retry failed
        connections. If you need granular control over the conditions under
        which we retry a request, import urllib3's ``Retry`` class and pass
        that instead.
    :param pool_block: Whether the connection pool should block for connections.

    Usage::

      >>> import requests
      >>> s = requests.Session()
      >>> a = requests.adapters.HTTPAdapter(max_retries=3)
      >>> s.mount('http://', a)
    
Initializes a urllib3 PoolManager.

        This method should not be called from user code, and is only
        exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param connections: The number of urllib3 connection pools to cache.
        :param maxsize: The maximum number of connections to save in the pool.
        :param block: Block when no free connections are available.
        :param pool_kwargs: Extra keyword arguments used to initialize the Pool Manager.
        
Return urllib3 ProxyManager for the given proxy.

        This method should not be called from user code, and is only
        exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param proxy: The proxy to return a urllib3 ProxyManager for.
        :param proxy_kwargs: Extra keyword arguments used to configure the Proxy Manager.
        :returns: ProxyManager
        :rtype: urllib3.ProxyManager
        
Verify a SSL certificate. This method should not be called from user
        code, and is only exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param conn: The urllib3 connection object associated with the cert.
        :param url: The requested URL.
        :param verify: Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use
        :param cert: The SSL certificate to verify.
        
Builds a :class:`Response <requests.Response>` object from a urllib3
        response. This should not be called from user code, and is only exposed
        for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`

        :param req: The :class:`PreparedRequest <PreparedRequest>` used to generate the response.
        :param resp: The urllib3 response object.
        :rtype: requests.Response
        
Build the PoolKey attributes used by urllib3 to return a connection.

        This looks at the PreparedRequest, the user-specified verify value,
        and the value of the cert parameter to determine what PoolKey values
        to use to select a connection from a given urllib3 Connection Pool.

        The SSL related pool key arguments are not consistently set. As of
        this writing, use the following to determine what keys may be in that
        dictionary:

        * If ``verify`` is ``True``, ``"ssl_context"`` will be set and will be the
          default Requests SSL Context
        * If ``verify`` is ``False``, ``"ssl_context"`` will not be set but
          ``"cert_reqs"`` will be set
        * If ``verify`` is a string, (i.e., it is a user-specified trust bundle)
          ``"ca_certs"`` will be set if the string is not a directory recognized
          by :py:func:`os.path.isdir`, otherwise ``"ca_certs_dir"`` will be
          set.
        * If ``"cert"`` is specified, ``"cert_file"`` will always be set. If
          ``"cert"`` is a tuple with a second item, ``"key_file"`` will also
          be present

        To override these settings, one may subclass this class, call this
        method and use the above logic to change parameters as desired. For
        example, if one wishes to use a custom :py:class:`ssl.SSLContext` one
        must both set ``"ssl_context"`` and based on what else they require,
        alter the other keys to ensure the desired behaviour.

        :param request:
            The PreparedReqest being sent over the connection.
        :type request:
            :class:`~requests.models.PreparedRequest`
        :param verify:
            Either a boolean, in which case it controls whether
            we verify the server's TLS certificate, or a string, in which case it
            must be a path to a CA bundle to use.
        :param cert:
            (optional) Any user-provided SSL certificate for client
            authentication (a.k.a., mTLS). This may be a string (i.e., just
            the path to a file which holds both certificate and key) or a
            tuple of length 2 with the certificate file path and key file
            path.
        :returns:
            A tuple of two dictionaries. The first is the "host parameters"
            portion of the Pool Key including scheme, hostname, and port. The
            second is a dictionary of SSLContext related parameters.
        
Returns a urllib3 connection for the given request and TLS settings.
        This should not be called from user code, and is only exposed for use
        when subclassing the :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param request:
            The :class:`PreparedRequest <PreparedRequest>` object to be sent
            over the connection.
        :param verify:
            Either a boolean, in which case it controls whether we verify the
            server's TLS certificate, or a string, in which case it must be a
            path to a CA bundle to use.
        :param proxies:
            (optional) The proxies dictionary to apply to the request.
        :param cert:
            (optional) Any user-provided SSL certificate to be used for client
            authentication (a.k.a., mTLS).
        :rtype:
            urllib3.ConnectionPool
        
DEPRECATED: Users should move to `get_connection_with_tls_context`
        for all subclasses of HTTPAdapter using Requests>=2.32.2.

        Returns a urllib3 connection for the given URL. This should not be
        called from user code, and is only exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param url: The URL to connect to.
        :param proxies: (optional) A Requests-style dictionary of proxies used on this request.
        :rtype: urllib3.ConnectionPool
        
Disposes of any internal state.

        Currently, this closes the PoolManager and any active ProxyManager,
        which closes any pooled connections.
        
Obtain the url to use when making the final request.

        If the message is being sent through a HTTP proxy, the full URL has to
        be used. Otherwise, we should only use the path portion of the URL.

        This should not be called from user code, and is only exposed for use
        when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
        :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs.
        :rtype: str
        
Add any headers needed by the connection. As of v2.0 this does
        nothing by default, but is left for overriding by users that subclass
        the :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        This should not be called from user code, and is only exposed for use
        when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param request: The :class:`PreparedRequest <PreparedRequest>` to add headers to.
        :param kwargs: The keyword arguments from the call to send().
        
Returns a dictionary of the headers to add to any request sent
        through a proxy. This works with urllib3 magic to ensure that they are
        correctly sent to the proxy, rather than in a tunnelled request if
        CONNECT is being used.

        This should not be called from user code, and is only exposed for use
        when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param proxy: The url of the proxy being used for this request.
        :rtype: dict
        
Sends PreparedRequest object. Returns Response object.

        :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
        :param stream: (optional) Whether to stream the request content.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple or urllib3 Timeout object
        :param verify: (optional) Either a boolean, in which case it controls whether
            we verify the server's TLS certificate, or a string, in which case it
            must be a path to a CA bundle to use
        :param cert: (optional) Any user-provided SSL certificate to be trusted.
        :param proxies: (optional) The proxies dictionary to apply to the request.
        :rtype: requests.Response
        

---


requests.cookies
~~~~~~~~~~~~~~~~

Compatibility code to be able to use `http.cookiejar.CookieJar` with requests.

requests.utils imports from here, so be careful with imports.

Wraps a `requests.Request` to mimic a `urllib2.Request`.

    The code in `http.cookiejar.CookieJar` expects this interface in order to correctly
    manage cookie policies, i.e., determine whether a cookie can be set, given the
    domains of the request and the cookie.

    The original request object is read-only. The client is responsible for collecting
    the new headers via `get_new_headers()` and interpreting them appropriately. You
    probably want `get_cookie_header`, defined below.
    
cookiejar has no legitimate use for this method; add it back if you find one.
Wraps a `httplib.HTTPMessage` to mimic a `urllib.addinfourl`.

    ...what? Basically, expose the parsed HTTP headers from the server response
    the way `http.cookiejar` expects to see them.
    
Make a MockResponse for `cookiejar` to read.

        :param headers: a httplib.HTTPMessage or analogous carrying the headers
        
Extract the cookies from the response into a CookieJar.

    :param jar: http.cookiejar.CookieJar (not necessarily a RequestsCookieJar)
    :param request: our own requests.Request object
    :param response: urllib3.HTTPResponse object
    

    Produce an appropriate Cookie header string to be sent with `request`, or None.

    :rtype: str
    
Unsets a cookie by name, by default over all domains and paths.

    Wraps CookieJar.clear(), is O(n).
    
There are two cookies that meet the criteria specified in the cookie jar.
    Use .get and .set and include domain and path args in order to be more specific.
    
Compatibility class; is a http.cookiejar.CookieJar, but exposes a dict
    interface.

    This is the CookieJar we create by default for requests and sessions that
    don't specify one, since some clients may expect response.cookies and
    session.cookies to support dict operations.

    Requests does not use the dict interface internally; it's just for
    compatibility with external client code. All requests code should work
    out of the box with externally provided instances of ``CookieJar``, e.g.
    ``LWPCookieJar`` and ``FileCookieJar``.

    Unlike a regular CookieJar, this class is pickleable.

    .. warning:: dictionary operations that are normally O(1) may be O(n).
    
Dict-like get() that also supports optional domain and path args in
        order to resolve naming collisions from using one cookie jar over
        multiple domains.

        .. warning:: operation is O(n), not O(1).
        
Dict-like set() that also supports optional domain and path args in
        order to resolve naming collisions from using one cookie jar over
        multiple domains.
        
Dict-like iterkeys() that returns an iterator of names of cookies
        from the jar.

        .. seealso:: itervalues() and iteritems().
        
Dict-like keys() that returns a list of names of cookies from the
        jar.

        .. seealso:: values() and items().
        
Dict-like itervalues() that returns an iterator of values of cookies
        from the jar.

        .. seealso:: iterkeys() and iteritems().
        
Dict-like values() that returns a list of values of cookies from the
        jar.

        .. seealso:: keys() and items().
        
Dict-like iteritems() that returns an iterator of name-value tuples
        from the jar.

        .. seealso:: iterkeys() and itervalues().
        
Dict-like items() that returns a list of name-value tuples from the
        jar. Allows client-code to call ``dict(RequestsCookieJar)`` and get a
        vanilla python dict of key value pairs.

        .. seealso:: keys() and values().
        
Utility method to list all the domains in the jar.
Utility method to list all the paths in the jar.
Returns True if there are multiple domains in the jar.
        Returns False otherwise.

        :rtype: bool
        
Takes as an argument an optional domain and path and returns a plain
        old Python dict of name-value pairs of cookies that meet the
        requirements.

        :rtype: dict
        
Dict-like __getitem__() for compatibility with client code. Throws
        exception if there are more than one cookie with name. In that case,
        use the more explicit get() method instead.

        .. warning:: operation is O(n), not O(1).
        
Dict-like __setitem__ for compatibility with client code. Throws
        exception if there is already a cookie of that name in the jar. In that
        case, use the more explicit set() method instead.
        
Deletes a cookie given a name. Wraps ``http.cookiejar.CookieJar``'s
        ``remove_cookie_by_name()``.
        
Updates this jar with cookies from another CookieJar or dict-like
Requests uses this method internally to get cookie values.

        If there are conflicting cookies, _find arbitrarily chooses one.
        See _find_no_duplicates if you want an exception thrown if there are
        conflicting cookies.

        :param name: a string containing name of cookie
        :param domain: (optional) string containing domain of cookie
        :param path: (optional) string containing path of cookie
        :return: cookie.value
        
Both ``__get_item__`` and ``get`` call this function: it's never
        used elsewhere in Requests.

        :param name: a string containing name of cookie
        :param domain: (optional) string containing domain of cookie
        :param path: (optional) string containing path of cookie
        :raises KeyError: if cookie is not found
        :raises CookieConflictError: if there are multiple cookies
            that match name and optionally domain and path
        :return: cookie.value
        
Unlike a normal CookieJar, this class is pickleable.
Unlike a normal CookieJar, this class is pickleable.
Return a copy of this RequestsCookieJar.
Return the CookiePolicy instance used.
Make a cookie from underspecified parameters.

    By default, the pair of `name` and `value` will be set for the domain ''
    and sent on every request (this is sometimes called a "supercookie").
    
Convert a Morsel object into a Cookie containing the one k/v pair.
Returns a CookieJar from a key/value dictionary.

    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :param cookiejar: (optional) A cookiejar to add the cookies to.
    :param overwrite: (optional) If False, will not replace cookies
        already in the jar with new ones.
    :rtype: CookieJar
    
Add cookies to cookiejar and returns a merged CookieJar.

    :param cookiejar: CookieJar object to add the cookies to.
    :param cookies: Dictionary or CookieJar object to be added.
    :rtype: CookieJar
    

---



---


requests.models
~~~~~~~~~~~~~~~

This module contains the primary objects that power Requests.

Build the path URL to use.
Encode parameters in a piece of data.

        Will successfully encode parameters when passed as a dict or a list of
        2-tuples. Order is retained if data is a list of 2-tuples but arbitrary
        if parameters are supplied as a dict.
        
Build the body for a multipart/form-data request.

        Will successfully encode files when passed as a dict or a list of
        tuples. Order is retained if data is a list of tuples but arbitrary
        if parameters are supplied as a dict.
        The tuples may be 2-tuples (filename, fileobj), 3-tuples (filename, fileobj, contentype)
        or 4-tuples (filename, fileobj, contentype, custom_headers).
        
Properly register a hook.
Deregister a previously registered hook.
        Returns True if the hook existed, False if not.
        
A user-created :class:`Request <Request>` object.

    Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.

    :param method: HTTP method to use.
    :param url: URL to send.
    :param headers: dictionary of headers to send.
    :param files: dictionary of {filename: fileobject} files to multipart upload.
    :param data: the body to attach to the request. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param json: json for the body to attach to the request (if files or data is not specified).
    :param params: URL parameters to append to the URL. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param auth: Auth handler or (user, pass) tuple.
    :param cookies: dictionary or CookieJar of cookies to attach to this request.
    :param hooks: dictionary of callback hooks, for internal usage.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> req.prepare()
      <PreparedRequest [GET]>
    
Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it.
The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
    containing the exact bytes that will be sent to the server.

    Instances are generated from a :class:`Request <Request>` object, and
    should not be instantiated manually; doing so may produce undesirable
    effects.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> r = req.prepare()
      >>> r
      <PreparedRequest [GET]>

      >>> s = requests.Session()
      >>> s.send(r)
      <Response [200]>
    
Prepares the entire request with the given parameters.
Prepares the given HTTP method.
Prepares the given HTTP URL.
Prepares the given HTTP headers.
Prepares the given HTTP body data.
Prepare Content-Length header based on request method and body
Prepares the given HTTP auth data.
Prepares the given HTTP cookie data.

        This function eventually generates a ``Cookie`` header from the
        given cookies using cookielib. Due to cookielib's design, the header
        will not be regenerated if it already exists, meaning this function
        can only be called once for the life of the
        :class:`PreparedRequest <PreparedRequest>` object. Any subsequent calls
        to ``prepare_cookies`` will have no actual effect, unless the "Cookie"
        header is removed beforehand.
        
Prepares the given hooks.
The :class:`Response <Response>` object, which contains a
    server's response to an HTTP request.
    
Returns True if :attr:`status_code` is less than 400.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        
Returns True if :attr:`status_code` is less than 400.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        
Allows you to use a response as an iterator.
Returns True if :attr:`status_code` is less than 400, False if not.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        
True if this Response is a well-formed HTTP redirect that could have
        been processed automatically (by :meth:`Session.resolve_redirects`).
        
True if this Response one of the permanent versions of redirect.
Returns a PreparedRequest for the next request in a redirect chain, if there is one.
The apparent encoding, provided by the charset_normalizer or chardet libraries.
Iterates over the response data.  When stream=True is set on the
        request, this avoids reading the content at once into memory for
        large responses.  The chunk size is the number of bytes it should
        read into memory.  This is not necessarily the length of each item
        returned as decoding can take place.

        chunk_size must be of type int or None. A value of None will
        function differently depending on the value of `stream`.
        stream=True will read data as it arrives in whatever size the
        chunks are received. If stream=False, data is returned as
        a single chunk.

        If decode_unicode is True, content will be decoded using the best
        available encoding based on the response.
        
Iterates over the response data, one line at a time.  When
        stream=True is set on the request, this avoids reading the
        content at once into memory for large responses.

        .. note:: This method is not reentrant safe.
        
Content of the response, in bytes.
Content of the response, in unicode.

        If Response.encoding is None, encoding will be guessed using
        ``charset_normalizer`` or ``chardet``.

        The encoding of the response content is determined based solely on HTTP
        headers, following RFC 2616 to the letter. If you can take advantage of
        non-HTTP knowledge to make a better guess at the encoding, you should
        set ``r.encoding`` appropriately before accessing this property.
        
Returns the json-encoded content of a response, if any.

        :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
        :raises requests.exceptions.JSONDecodeError: If the response body does not
            contain valid json.
        
Returns the parsed header links of the response, if any.
Raises :class:`HTTPError`, if one occurred.
Releases the connection back to the pool. Once this method has been
        called the underlying ``raw`` object must not be accessed again.

        *Note: Should not normally need to be called explicitly.*
        

---


requests.hooks
~~~~~~~~~~~~~~

This module provides the capabilities for the Requests hooks system.

Available hooks:

``response``:
    The response generated from a Request.

Dispatches a hook dictionary on a given piece of data.

---


requests._internal_utils
~~~~~~~~~~~~~~

Provides utility functions that are consumed internally by Requests
which depend on extremely few external helpers (such as compat)

Given a string object, regardless of type, returns a representation of
    that string in the native string type, encoding and decoding where
    necessary. This assumes ASCII unless told otherwise.
    
Determine if unicode string only contains ASCII characters.

    :param str u_string: unicode string to check. Must be unicode
        and not Python 2 `str`.
    :rtype: bool
    

---


requests.sessions
~~~~~~~~~~~~~~~~~

This module provides a Session object to manage and persist settings across
requests (cookies, auth, proxies).

Determines appropriate setting for a given request, taking into account
    the explicit setting on that request, and the setting in the session. If a
    setting is a dictionary, they will be merged together using `dict_class`
    
Properly merges both requests and session hooks.

    This is necessary because when request_hooks == {'response': []}, the
    merge breaks Session hooks entirely.
    
Receives a Response. Returns a redirect URI or ``None``
Decide whether Authorization header should be removed when redirecting
Receives a Response. Returns a generator of Responses or Requests.
When being redirected we may want to strip authentication from the
        request to avoid leaking credentials. This method intelligently removes
        and reapplies authentication where possible to avoid credential loss.
        
This method re-evaluates the proxy configuration by considering the
        environment variables. If we are redirected to a URL covered by
        NO_PROXY, we strip the proxy configuration. Otherwise, we set missing
        proxy keys for this URL (in case they were stripped by a previous
        redirect).

        This method also replaces the Proxy-Authorization header where
        necessary.

        :rtype: dict
        
When being redirected we may want to change the method of the request
        based on certain specs or browser behavior.
        
A Requests session.

    Provides cookie persistence, connection-pooling, and configuration.

    Basic Usage::

      >>> import requests
      >>> s = requests.Session()
      >>> s.get('https://httpbin.org/get')
      <Response [200]>

    Or as a context manager::

      >>> with requests.Session() as s:
      ...     s.get('https://httpbin.org/get')
      <Response [200]>
    
Constructs a :class:`PreparedRequest <PreparedRequest>` for
        transmission and returns it. The :class:`PreparedRequest` has settings
        merged from the :class:`Request <Request>` instance and those of the
        :class:`Session`.

        :param request: :class:`Request` instance to prepare with this
            session's settings.
        :rtype: requests.PreparedRequest
        
Constructs a :class:`Request <Request>`, prepares it and sends it.
        Returns :class:`Response <Response>` object.

        :param method: method for the new :class:`Request` object.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query
            string for the :class:`Request`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the
            :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the
            :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the
            :class:`Request`.
        :param files: (optional) Dictionary of ``'filename': file-like-objects``
            for multipart encoding upload.
        :param auth: (optional) Auth tuple or callable to enable
            Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Set to True by default.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol or protocol and
            hostname to the URL of the proxy.
        :param hooks: (optional) Dictionary mapping hook name to one event or
            list of events, event must be callable.
        :param stream: (optional) whether to immediately download the response
            content. Defaults to ``False``.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``. When set to
            ``False``, requests will accept any TLS certificate presented by
            the server, and will ignore hostname mismatches and/or expired
            certificates, which will make your application vulnerable to
            man-in-the-middle (MitM) attacks. Setting verify to ``False``
            may be useful during local development or testing.
        :param cert: (optional) if String, path to ssl client cert file (.pem).
            If Tuple, ('cert', 'key') pair.
        :rtype: requests.Response
        
Sends a GET request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Sends a OPTIONS request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Sends a HEAD request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Sends a POST request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Sends a PUT request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Sends a PATCH request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Sends a DELETE request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Send a given PreparedRequest.

        :rtype: requests.Response
        

        Check the environment and merge it with some settings.

        :rtype: dict
        

        Returns the appropriate connection adapter for the given URL.

        :rtype: requests.adapters.BaseAdapter
        
Closes all adapters and as such the session
Registers a connection adapter to a prefix.

        Adapters are sorted in descending order by prefix length.
        

    Returns a :class:`Session` for context-management.

    .. deprecated:: 1.0.0

        This method has been deprecated since version 1.0.0 and is only kept for
        backwards compatibility. New code should use :class:`~requests.sessions.Session`
        to create a session. This may be removed at a future date.

    :rtype: Session
    

---


Requests HTTP Library
~~~~~~~~~~~~~~~~~~~~~

Requests is an HTTP library, written in Python, for human beings.
Basic GET usage:

   >>> import requests
   >>> r = requests.get('https://www.python.org')
   >>> r.status_code
   200
   >>> b'Python is a programming language' in r.content
   True

... or POST:

   >>> payload = dict(key1='value1', key2='value2')
   >>> r = requests.post('https://httpbin.org/post', data=payload)
   >>> print(r.text)
   {
     ...
     "form": {
       "key1": "value1",
       "key2": "value2"
     },
     ...
   }

The other HTTP methods are supported - see `requests.api`. Full documentation
is at <https://requests.readthedocs.io>.

:copyright: (c) 2017 by Kenneth Reitz.
:license: Apache 2.0, see LICENSE for more details.


---


The ``codes`` object defines a mapping from common names for HTTP statuses
to their numerical codes, accessible either as attributes or as dictionary
items.

Example::

    >>> import requests
    >>> requests.codes['temporary_redirect']
    307
    >>> requests.codes.teapot
    418
    >>> requests.codes['\o/']
    200

Some codes have multiple names, and both upper- and lower-case versions of
the names are allowed. For example, ``codes.ok``, ``codes.OK``, and
``codes.okay`` all correspond to the HTTP status code 200.


---


requests.certs
~~~~~~~~~~~~~~

This module returns the preferred default CA certificate bundle. There is
only one — the one from the certifi package.

If you are packaging Requests, e.g., for a Linux distribution or a managed
environment, you can change the definition of where() to return a separately
packaged CA bundle.


---


requests.compat
~~~~~~~~~~~~~~~

This module previously handled import compatibility issues
between Python 2 and Python 3. It remains for backwards
compatibility until the next major version.

Find supported character detection libraries.

---


requests.structures
~~~~~~~~~~~~~~~~~~~

Data structures that power Requests.

A case-insensitive ``dict``-like object.

    Implements all methods and operations of
    ``MutableMapping`` as well as dict's ``copy``. Also
    provides ``lower_items``.

    All keys are expected to be strings. The structure remembers the
    case of the last key to be set, and ``iter(instance)``,
    ``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
    will contain case-sensitive keys. However, querying and contains
    testing is case insensitive::

        cid = CaseInsensitiveDict()
        cid['Accept'] = 'application/json'
        cid['aCCEPT'] == 'application/json'  # True
        list(cid) == ['Accept']  # True

    For example, ``headers['content-encoding']`` will return the
    value of a ``'Content-Encoding'`` response header, regardless
    of how the header name was originally stored.

    If the constructor, ``.update``, or equality comparison
    operations are given keys that have equal ``.lower()``s, the
    behavior is undefined.
    
Like iteritems(), but with all lowercase keys.
Dictionary lookup object.

---

Module containing bug report helper(s).
Return a dict with the Python implementation and version.

    Provide both the name and the version of the Python implementation
    currently running. For example, on CPython 3.10.3 it will return
    {'name': 'CPython', 'version': '3.10.3'}.

    This function works best on CPython and PyPy: in particular, it probably
    doesn't work for Jython or IronPython. Future investigation should be done
    to work out the correct shape of the code for those platforms.
    
Generate information for a bug report.
Pretty-print the bug information as JSON.

---



---


requests.utils
~~~~~~~~~~~~~~

This module provides utility functions that are used within Requests
that are also useful for external consumption.

Return True, if the host should be bypassed.

        Checks proxy settings gathered from the environment, if specified,
        or the registry.
        
Returns an internal sequence dictionary update.
Returns the Requests tuple auth for a given url from netrc.
Tries to guess the filename of the given object.
Replace nonexistent paths that look like they refer to a member of a zip
    archive with the location of an extracted copy of the target, or else
    just return the provided path unchanged.
    
Write a file to the disk in an atomic fashion
Take an object and test to see if it can be represented as a
    dictionary. Unless it can not be represented as such, return an
    OrderedDict, e.g.,

    ::

        >>> from_key_val_list([('key', 'val')])
        OrderedDict([('key', 'val')])
        >>> from_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples
        >>> from_key_val_list({'key': 'val'})
        OrderedDict([('key', 'val')])

    :rtype: OrderedDict
    
Take an object and test to see if it can be represented as a
    dictionary. If it can be, return a list of tuples, e.g.,

    ::

        >>> to_key_val_list([('key', 'val')])
        [('key', 'val')]
        >>> to_key_val_list({'key': 'val'})
        [('key', 'val')]
        >>> to_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples

    :rtype: list
    
Parse lists as described by RFC 2068 Section 2.

    In particular, parse comma-separated lists where the elements of
    the list may include quoted-strings.  A quoted-string could
    contain a comma.  A non-quoted string could have quotes in the
    middle.  Quotes are removed automatically after parsing.

    It basically works like :func:`parse_set_header` just that items
    may appear multiple times and case sensitivity is preserved.

    The return value is a standard :class:`list`:

    >>> parse_list_header('token, "quoted value"')
    ['token', 'quoted value']

    To create a header from the :class:`list` again, use the
    :func:`dump_header` function.

    :param value: a string with a list header.
    :return: :class:`list`
    :rtype: list
    
Parse lists of key, value pairs as described by RFC 2068 Section 2 and
    convert them into a python dict:

    >>> d = parse_dict_header('foo="is a fish", bar="as well"')
    >>> type(d) is dict
    True
    >>> sorted(d.items())
    [('bar', 'as well'), ('foo', 'is a fish')]

    If there is no value for a key it will be `None`:

    >>> parse_dict_header('key_without_value')
    {'key_without_value': None}

    To create a header from the :class:`dict` again, use the
    :func:`dump_header` function.

    :param value: a string with a dict header.
    :return: :class:`dict`
    :rtype: dict
    
Unquotes a header value.  (Reversal of :func:`quote_header_value`).
    This does not use the real unquoting but what browsers are actually
    using for quoting.

    :param value: the header value to unquote.
    :rtype: str
    
Returns a key/value dictionary from a CookieJar.

    :param cj: CookieJar object to extract cookies from.
    :rtype: dict
    
Returns a CookieJar from a key/value dictionary.

    :param cj: CookieJar to insert cookies into.
    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :rtype: CookieJar
    
Returns encodings from given content string.

    :param content: bytestring to extract encodings from.
    
Returns content type and parameters from given header

    :param header: string
    :return: tuple containing content type and dictionary of
         parameters
    
Returns encodings from given HTTP Header Dict.

    :param headers: dictionary to extract encoding from.
    :rtype: str
    
Stream decodes an iterator.
Iterate over slices of a string.
Returns the requested content back in unicode.

    :param r: Response object to get unicode content from.

    Tried:

    1. charset from content-type
    2. fall back and replace all unicode characters

    :rtype: str
    
Un-escape any percent-escape sequences in a URI that are unreserved
    characters. This leaves all reserved, illegal and non-ASCII bytes encoded.

    :rtype: str
    
Re-quote the given URI.

    This function passes the given URI through an unquote/quote cycle to
    ensure that it is fully and consistently quoted.

    :rtype: str
    
This function allows you to check if an IP belongs to a network subnet

    Example: returns True if ip = 192.168.1.1 and net = 192.168.1.0/24
             returns False if ip = 192.168.1.1 and net = 192.168.100.0/24

    :rtype: bool
    
Converts mask from /xx format to xxx.xxx.xxx.xxx

    Example: if mask is 24 function returns 255.255.255.0

    :rtype: str
    

    :rtype: bool
    

    Very simple check of the cidr format in no_proxy variable.

    :rtype: bool
    
Set the environment variable 'env_name' to 'value'

    Save previous value, yield, and then restore the previous value stored in
    the environment variable 'env_name'.

    If 'value' is None, do nothing

    Returns whether we should bypass proxies or not.

    :rtype: bool
    

    Return a dict of environment proxies.

    :rtype: dict
    
Select a proxy for the url, if applicable.

    :param url: The url being for the request
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    
This method takes proxy information from a request and configuration
    input to resolve a mapping of target proxies. This will consider settings
    such as NO_PROXY to strip proxy configurations.

    :param request: Request or PreparedRequest
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    :param trust_env: Boolean declaring whether to trust environment configs

    :rtype: dict
    

    Return a string representing the default user agent.

    :rtype: str
    

    :rtype: requests.structures.CaseInsensitiveDict
    
Return a list of parsed link headers proxies.

    i.e. Link: <http:/.../front.jpeg>; rel=front; type="image/jpeg",<http://.../back.jpeg>; rel=back;type="image/jpeg"

    :rtype: list
    

    :rtype: str
    
Given a URL that may or may not have a scheme, prepend the given scheme.
    Does not replace a present scheme with the one provided as an argument.

    :rtype: str
    
Given a url with authentication components, extract them into a tuple of
    username,password.

    :rtype: (str,str)
    
Verifies that header parts don't contain leading whitespace
    reserved characters, or return characters.

    :param header: tuple, in the format (name, value).
    

    Given a url remove the fragment and the authentication part.

    :rtype: str
    
Move file pointer back to its recorded starting position
    so it can be read again on redirect.
    

---

Base exception for all IDNA-encoding related problems
Exception when bidirectional requirements are not satisfied
Exception when a disallowed or unallocated codepoint is used
Exception when the codepoint is not valid in the context it is used
Re-map the characters in the string according to UTS46 processing.

---



---



---



---


Given a list of integers, made up of (hopefully) a small number of long runs
of consecutive integers, compute a representation of the form
((start1, end1), (start2, end2) ...). Then answer the question "was x present
in the original list?" in time O(log(# runs)).

Represent a list of integers as a sequence of ranges:
    ((start_0, end_0), (start_1, end_1), ...), such that the original
    integers are exactly those x such that start_i <= x < end_i for some i.

    Ranges are encoded as single integers (start << 32 | end), not as tuples.
    
Determine if `int_` falls into one of the ranges in `ranges`.

---

IDNA Mapping Table from UTS46.

---



---



---

Loads a CDLL by name, falling back to known path on 10.16+

    Raises an error if the OSStatus value is non-zero.
    
CoreFoundation constants

    Given a Python binary data, create a CFString.
    The string must be CFReleased by the caller.
    

    Creates a Unicode string from a CFString object. Used entirely for error
    reporting.
    Yes, it annoys me quite a lot that this function is this complex.
    
Builds a CFArray of SecCertificateRefs from a list of DER-encoded certificates.
    Responsibility of the caller to call CoreFoundation.CFRelease on the CFArray.
    
Verify using 'SecTrustEvaluate' API for macOS 10.13 and earlier.
    macOS 10.14 added the 'SecTrustEvaluateWithError' API.
    
Verify using 'SecTrustEvaluateWithError' API for macOS 10.14+.

---



---

Verify the cert_chain from the server using Windows APIs.

---

Injects the :class:`truststore.SSLContext` into the ``ssl``
    module by replacing :class:`ssl.SSLContext`.
    
Restores the :class:`ssl.SSLContext` class to its original state
SSLContext API that uses system certificates on all platforms

    Verifies the peer certificates from an SSLSocket or SSLObject
    against the certificates in the OS trust store.
    

---

Check whether capath exists and contains certs in the expected format.

---

Verify certificates using native system trust stores

---


certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem or its contents.


---



---



---


    An invalid marker was found, users should refer to PEP 508.
    

    An invalid operation was attempted on a value that doesn't support it.
    

    A name was attempted to be used that does not exist inside of the
    environment.
    
The implementation's identifier, e.g. ``'cpython'``.

    The implementation's version, e.g. ``'3.13.0a2'`` for CPython 3.13.0a2, or
    ``'7.3.13'`` for PyPy3.10 v7.3.13.
    

    The value of :py:data:`os.name`. The name of the operating system dependent module
    imported, e.g. ``'posix'``.
    

    Returns the machine type, e.g. ``'i386'``.

    An empty string if the value cannot be determined.
    

    The system's release, e.g. ``'2.2.0'`` or ``'NT'``.

    An empty string if the value cannot be determined.
    

    The system/OS name, e.g. ``'Linux'``, ``'Windows'`` or ``'Java'``.

    An empty string if the value cannot be determined.
    

    The system's release version, e.g. ``'#3 on degas'``.

    An empty string if the value cannot be determined.
    

    The Python version as string ``'major.minor.patchlevel'``.

    Note that unlike the Python :py:data:`sys.version`, this value will always include
    the patchlevel (it defaults to 0).
    

    A string identifying the Python implementation, e.g. ``'CPython'``.
    
The Python version as string ``'major.minor'``.

    This string contains a platform identifier that can be used to append
    platform-specific components to :py:data:`sys.path`, for instance.

    For Unix systems, except on Linux and AIX, this is the lowercased OS name as
    returned by ``uname -s`` with the first part of the version as returned by
    ``uname -r`` appended, e.g. ``'sunos5'`` or ``'freebsd8'``, at the time when Python
    was built.
    

    Normalize extra values.
    
Evaluate a marker.

        Return the boolean from evaluating the given marker against the
        environment. environment is an optional argument to override all or
        part of the determined environment. The *context* parameter specifies what
        context the markers are being evaluated for, which influences what markers
        are considered valid. Acceptable values are "metadata" (for core metadata;
        default), "lock_file", and "requirement" (i.e. all other situations).

        The environment is determined from the current Python process.
        

    Work around platform.python_version() returning something that is not PEP 440
    compliant for non-tagged Python builds.
    

---

Handwritten parser of dependency specifiers.

The docstring for each __parse_* function contains EBNF-inspired grammar representing
the implementation.


    requirement = WS? IDENTIFIER WS? extras WS? requirement_details
    

    requirement_details = AT URL (WS requirement_marker?)?
                        | specifier WS? (requirement_marker)?
    

    requirement_marker = SEMICOLON marker WS?
    

    extras = (LEFT_BRACKET wsp* extras_list? wsp* RIGHT_BRACKET)?
    

    extras_list = identifier (wsp* ',' wsp* identifier)*
    

    specifier = LEFT_PARENTHESIS WS? version_many WS? RIGHT_PARENTHESIS
              | WS? version_many WS?
    

    version_many = (SPECIFIER (WS? COMMA WS? SPECIFIER)*)?
    

    marker = marker_atom (BOOLOP marker_atom)+
    

    marker_atom = WS? LEFT_PARENTHESIS WS? marker WS? RIGHT_PARENTHESIS WS?
                | WS? marker_item WS?
    

    marker_item = WS? marker_var WS? marker_op WS? marker_var WS?
    

    marker_var = VARIABLE | QUOTED_STRING
    

    marker_op = IN | NOT IN | OP
    

---


.. testsetup::

    from pip._vendor.packaging.version import parse, Version

Parse the given version string.

    >>> parse('1.0.dev1')
    <Version('1.0.dev1')>

    :param version: The version string to parse.
    :raises InvalidVersion: When the version string is not a valid version.
    
Raised when a version string is not a valid version.

    >>> Version("invalid")
    Traceback (most recent call last):
        ...
    packaging.version.InvalidVersion: Invalid version: 'invalid'
    

    v?
    (?:
        (?:(?P<epoch>[0-9]+)!)?                           # epoch
        (?P<release>[0-9]+(?:\.[0-9]+)*)                  # release segment
        (?P<pre>                                          # pre-release
            [-_\.]?
            (?P<pre_l>alpha|a|beta|b|preview|pre|c|rc)
            [-_\.]?
            (?P<pre_n>[0-9]+)?
        )?
        (?P<post>                                         # post release
            (?:-(?P<post_n1>[0-9]+))
            |
            (?:
                [-_\.]?
                (?P<post_l>post|rev|r)
                [-_\.]?
                (?P<post_n2>[0-9]+)?
            )
        )?
        (?P<dev>                                          # dev release
            [-_\.]?
            (?P<dev_l>dev)
            [-_\.]?
            (?P<dev_n>[0-9]+)?
        )?
    )
    (?:\+(?P<local>[a-z0-9]+(?:[-_\.][a-z0-9]+)*))?       # local version


A string containing the regular expression used to match a valid version.

The pattern is not anchored at either end, and is intended for embedding in larger
expressions (for example, matching a version number as part of a file name). The
regular expression should be compiled with the ``re.VERBOSE`` and ``re.IGNORECASE``
flags set.

:meta hide-value:

This class abstracts handling of a project's versions.

    A :class:`Version` instance is comparison aware and can be compared and
    sorted using the standard Python interfaces.

    >>> v1 = Version("1.0a5")
    >>> v2 = Version("1.0")
    >>> v1
    <Version('1.0a5')>
    >>> v2
    <Version('1.0')>
    >>> v1 < v2
    True
    >>> v1 == v2
    False
    >>> v1 > v2
    False
    >>> v1 >= v2
    False
    >>> v1 <= v2
    True
    
Initialize a Version object.

        :param version:
            The string representation of a version which will be parsed and normalized
            before use.
        :raises InvalidVersion:
            If the ``version`` does not conform to PEP 440 in any way then this
            exception will be raised.
        
A representation of the Version that shows all internal state.

        >>> Version('1.0.0')
        <Version('1.0.0')>
        
A string representation of the version that can be round-tripped.

        >>> str(Version("1.0a5"))
        '1.0a5'
        
The epoch of the version.

        >>> Version("2.0.0").epoch
        0
        >>> Version("1!2.0.0").epoch
        1
        
The components of the "release" segment of the version.

        >>> Version("1.2.3").release
        (1, 2, 3)
        >>> Version("2.0.0").release
        (2, 0, 0)
        >>> Version("1!2.0.0.post0").release
        (2, 0, 0)

        Includes trailing zeroes but not the epoch or any pre-release / development /
        post-release suffixes.
        
The pre-release segment of the version.

        >>> print(Version("1.2.3").pre)
        None
        >>> Version("1.2.3a1").pre
        ('a', 1)
        >>> Version("1.2.3b1").pre
        ('b', 1)
        >>> Version("1.2.3rc1").pre
        ('rc', 1)
        
The post-release number of the version.

        >>> print(Version("1.2.3").post)
        None
        >>> Version("1.2.3.post1").post
        1
        
The development number of the version.

        >>> print(Version("1.2.3").dev)
        None
        >>> Version("1.2.3.dev1").dev
        1
        
The local version segment of the version.

        >>> print(Version("1.2.3").local)
        None
        >>> Version("1.2.3+abc").local
        'abc'
        
The public portion of the version.

        >>> Version("1.2.3").public
        '1.2.3'
        >>> Version("1.2.3+abc").public
        '1.2.3'
        >>> Version("1!1.2.3dev1+abc").public
        '1!1.2.3.dev1'
        
The "base version" of the version.

        >>> Version("1.2.3").base_version
        '1.2.3'
        >>> Version("1.2.3+abc").base_version
        '1.2.3'
        >>> Version("1!1.2.3dev1+abc").base_version
        '1!1.2.3'

        The "base version" is the public version of the project without any pre or post
        release markers.
        
Whether this version is a pre-release.

        >>> Version("1.2.3").is_prerelease
        False
        >>> Version("1.2.3a1").is_prerelease
        True
        >>> Version("1.2.3b1").is_prerelease
        True
        >>> Version("1.2.3rc1").is_prerelease
        True
        >>> Version("1.2.3dev1").is_prerelease
        True
        
Whether this version is a post-release.

        >>> Version("1.2.3").is_postrelease
        False
        >>> Version("1.2.3.post1").is_postrelease
        True
        
Whether this version is a development release.

        >>> Version("1.2.3").is_devrelease
        False
        >>> Version("1.2.3.dev1").is_devrelease
        True
        
The first item of :attr:`release` or ``0`` if unavailable.

        >>> Version("1.2.3").major
        1
        
The second item of :attr:`release` or ``0`` if unavailable.

        >>> Version("1.2.3").minor
        2
        >>> Version("1").minor
        0
        
The third item of :attr:`release` or ``0`` if unavailable.

        >>> Version("1.2.3").micro
        3
        >>> Version("1").micro
        0
        

        Release segment without any trailing zeros.

        >>> _TrimmedRelease('1.0.0').release
        (1,)
        >>> _TrimmedRelease('0.0').release
        (0,)
        

    Takes a string like abc.1.twelve and turns it into ("abc", 1, "twelve").
    

---



---


    An invalid requirement was found, users should refer to PEP 508.
    
Parse a requirement.

    Parse a given requirement string into its parts, such as name, specifier,
    URL, and extras. Raises InvalidRequirement on a badly-formed requirement
    string.
    

---


ELF file parser.

This provides a class ``ELFFile`` that parses an ELF executable in a similar
interface to ``ZipFile``. Only the read interface is implemented.

Based on: https://gist.github.com/lyssdod/f51579ae8d93c8657a5564aefc2ffbca
ELF header: https://refspecs.linuxfoundation.org/elf/gabi4+/ch4.eheader.html


    Representation of an ELF executable.
    

        The path recorded in the ``PT_INTERP`` section header.
        

---

A minimal implementation of :external:exc:`ExceptionGroup` from Python 3.11.

        If :external:exc:`ExceptionGroup` is already defined by Python itself,
        that version is used instead.
        
A metadata field contains invalid data.
The name of the field that contains invalid data.
A dictionary of raw core metadata.

    Each field in core metadata maps to a key of this dictionary (when data is
    provided). The key is lower-case and underscores are used instead of dashes
    compared to the equivalent core metadata field. Any core metadata field that
    can be specified multiple times or can hold multiple values in a single
    field have a key with a plural name. See :class:`Metadata` whose attributes
    match the keys of this dictionary.

    Core metadata fields that can be specified multiple times are stored as a
    list or dict depending on which is appropriate for the field. Any fields
    which hold multiple values in a single field are stored as a list.

    
Split a string of comma-separated keywords into a list of keywords.
Parse a list of label/URL string pairings separated by a comma.
Get the body of the message.
Parse a distribution's metadata stored as email headers (e.g. from ``METADATA``).

    This function returns a two-item tuple of dicts. The first dict is of
    recognized fields from the core metadata specification. Fields that can be
    parsed and translated into Python's built-in types are converted
    appropriately. All other fields are left as-is. Fields that are allowed to
    appear multiple times are stored as lists.

    The second dict contains all other fields from the metadata. This includes
    any unrecognized fields. It also includes any fields which are expected to
    be parsed into a built-in type but were not formatted appropriately. Finally,
    any fields that are expected to appear only once but are repeated are
    included in this dict.

    
Validate a metadata field.

    All _process_*() methods correspond to a core metadata field. The method is
    called with the field's raw value. If the raw value is valid it is returned
    in its "enriched" form (e.g. ``version.Version`` for the ``Version`` field).
    If the raw value is invalid, :exc:`InvalidMetadata` is raised (with a cause
    as appropriate).
    
Check the field contains no newlines.
Representation of distribution metadata.

    Compared to :class:`RawMetadata`, this class provides objects representing
    metadata fields instead of only using built-in types. Any invalid metadata
    will cause :exc:`InvalidMetadata` to be raised (with a
    :py:attr:`~BaseException.__cause__` attribute as appropriate).
    
Create an instance from :class:`RawMetadata`.

        If *validate* is true, all metadata will be validated. All exceptions
        related to validation will be gathered and raised as an :class:`ExceptionGroup`.
        
Parse metadata from email headers.

        If *validate* is true, the metadata will be validated. All exceptions
        related to validation will be gathered and raised as an :class:`ExceptionGroup`.
        
:external:ref:`core-metadata-metadata-version`
    (required; validated to be a valid metadata version)
:external:ref:`core-metadata-name`
    (required; validated using :func:`~packaging.utils.canonicalize_name` and its
    *validate* parameter)
:external:ref:`core-metadata-version` (required)
:external:ref:`core-metadata-dynamic`
    (validated against core metadata field names and lowercased)
:external:ref:`core-metadata-platform`
:external:ref:`core-metadata-supported-platform`
:external:ref:`core-metadata-summary` (validated to contain no newlines)
:external:ref:`core-metadata-description`
:external:ref:`core-metadata-description-content-type` (validated)
:external:ref:`core-metadata-keywords`
:external:ref:`core-metadata-home-page`
:external:ref:`core-metadata-download-url`
:external:ref:`core-metadata-author`
:external:ref:`core-metadata-author-email`
:external:ref:`core-metadata-maintainer`
:external:ref:`core-metadata-maintainer-email`
:external:ref:`core-metadata-license`
:external:ref:`core-metadata-license-expression`
:external:ref:`core-metadata-license-file`
:external:ref:`core-metadata-classifier`
:external:ref:`core-metadata-requires-dist`
:external:ref:`core-metadata-requires-python`
:external:ref:`core-metadata-requires-external`
:external:ref:`core-metadata-project-url`
:external:ref:`core-metadata-provides-extra`
:external:ref:`core-metadata-provides-dist`
:external:ref:`core-metadata-obsoletes-dist`
``Requires`` (deprecated)
``Provides`` (deprecated)
``Obsoletes`` (deprecated)

---


    Primary implementation of glibc_version_string using os.confstr.
    

    Fallback implementation of glibc_version_string using ctypes.
    
Returns glibc version string, or None if not using glibc.
Parse glibc version.

    We use a regexp instead of str.split because we want to discard any
    random junk that might come after the minor version -- this might happen
    in patched/forked versions of glibc (e.g. Linaro's version of glibc
    uses version strings like "2.20-2014.11"). See gh-3588.
    
Generate manylinux tags compatible to the current platform.

    :param archs: Sequence of compatible architectures.
        The first one shall be the closest to the actual architecture and be the part of
        platform tag after the ``linux_`` prefix, e.g. ``x86_64``.
        The ``linux_`` prefix is assumed as a prerequisite for the current platform to
        be manylinux-compatible.

    :returns: An iterator of compatible manylinux tags.
    

---

The provided source text could not be parsed correctly.

            (
                ('[^']*')
                |
                ("[^"]*")
            )
        

            \b(
                python_version
                |python_full_version
                |os[._]name
                |sys[._]platform
                |platform_(release|system)
                |platform[._](version|machine|python_implementation)
                |python_implementation
                |implementation_(name|version)
                |extras?
                |dependency_groups
            )\b
        
Context-sensitive token parsing.

    Provides methods to examine the input stream to check whether the next token
    matches.
    
Move beyond provided token name, if at current position.
Check whether the next token has the provided name.

        By default, if the check succeeds, the token *must* be read before
        another check. If `peek` is set to `True`, the token is not loaded and
        would need to be checked again.
        
Expect a certain token name next, failing with a syntax error otherwise.

        The token is *not* read.
        
Consume the next token and return it.
Raise ParserSyntaxError at the given position.

---


.. testsetup::

    from pip._vendor.packaging.specifiers import Specifier, SpecifierSet, InvalidSpecifier
    from pip._vendor.packaging.version import Version


    Raised when attempting to create a :class:`Specifier` with a specifier
    string that is invalid.

    >>> Specifier("lolwat")
    Traceback (most recent call last):
        ...
    packaging.specifiers.InvalidSpecifier: Invalid specifier: 'lolwat'
    

        Returns the str representation of this Specifier-like object. This
        should be representative of the Specifier itself.
        

        Returns a hash value for this Specifier-like object.
        

        Returns a boolean representing whether or not the two Specifier-like
        objects are equal.

        :param other: The other object to check against.
        
Whether or not pre-releases as a whole are allowed.

        This can be set to either ``True`` or ``False`` to explicitly enable or disable
        prereleases or it can be set to ``None`` (the default) to use default semantics.
        
Setter for :attr:`prereleases`.

        :param value: The value to set.
        

        Determines if the given item is contained within this specifier.
        

        Takes an iterable of items and filters them so that only items which
        are contained within this specifier are allowed in it.
        
This class abstracts handling of version specifiers.

    .. tip::

        It is generally not required to instantiate this manually. You should instead
        prefer to work with :class:`SpecifierSet` instead, which can parse
        comma-separated version specifiers (which is what package metadata contains).
    

        (?P<operator>(~=|==|!=|<=|>=|<|>|===))
        

        (?P<version>
            (?:
                # The identity operators allow for an escape hatch that will
                # do an exact string match of the version you wish to install.
                # This will not be parsed by PEP 440 and we cannot determine
                # any semantic meaning from it. This operator is discouraged
                # but included entirely as an escape hatch.
                (?<====)  # Only match for the identity operator
                \s*
                [^\s;)]*  # The arbitrary version can be just about anything,
                          # we match everything except for whitespace, a
                          # semi-colon for marker support, and a closing paren
                          # since versions can be enclosed in them.
            )
            |
            (?:
                # The (non)equality operators allow for wild card and local
                # versions to be specified so we have to define these two
                # operators separately to enable that.
                (?<===|!=)            # Only match for equals and not equals

                \s*
                v?
                (?:[0-9]+!)?          # epoch
                [0-9]+(?:\.[0-9]+)*   # release

                # You cannot use a wild card and a pre-release, post-release, a dev or
                # local version together so group them with a | and make them optional.
                (?:
                    \.\*  # Wild card syntax of .*
                    |
                    (?:                                  # pre release
                        [-_\.]?
                        (alpha|beta|preview|pre|a|b|c|rc)
                        [-_\.]?
                        [0-9]*
                    )?
                    (?:                                  # post release
                        (?:-[0-9]+)|(?:[-_\.]?(post|rev|r)[-_\.]?[0-9]*)
                    )?
                    (?:[-_\.]?dev[-_\.]?[0-9]*)?         # dev release
                    (?:\+[a-z0-9]+(?:[-_\.][a-z0-9]+)*)? # local
                )?
            )
            |
            (?:
                # The compatible operator requires at least two digits in the
                # release segment.
                (?<=~=)               # Only match for the compatible operator

                \s*
                v?
                (?:[0-9]+!)?          # epoch
                [0-9]+(?:\.[0-9]+)+   # release  (We have a + instead of a *)
                (?:                   # pre release
                    [-_\.]?
                    (alpha|beta|preview|pre|a|b|c|rc)
                    [-_\.]?
                    [0-9]*
                )?
                (?:                                   # post release
                    (?:-[0-9]+)|(?:[-_\.]?(post|rev|r)[-_\.]?[0-9]*)
                )?
                (?:[-_\.]?dev[-_\.]?[0-9]*)?          # dev release
            )
            |
            (?:
                # All other operators only allow a sub set of what the
                # (non)equality operators do. Specifically they do not allow
                # local versions to be specified nor do they allow the prefix
                # matching wild cards.
                (?<!==|!=|~=)         # We have special cases for these
                                      # operators so we want to make sure they
                                      # don't match here.

                \s*
                v?
                (?:[0-9]+!)?          # epoch
                [0-9]+(?:\.[0-9]+)*   # release
                (?:                   # pre release
                    [-_\.]?
                    (alpha|beta|preview|pre|a|b|c|rc)
                    [-_\.]?
                    [0-9]*
                )?
                (?:                                   # post release
                    (?:-[0-9]+)|(?:[-_\.]?(post|rev|r)[-_\.]?[0-9]*)
                )?
                (?:[-_\.]?dev[-_\.]?[0-9]*)?          # dev release
            )
        )
        
Initialize a Specifier instance.

        :param spec:
            The string representation of a specifier which will be parsed and
            normalized before use.
        :param prereleases:
            This tells the specifier if it should accept prerelease versions if
            applicable or not. The default of ``None`` will autodetect it from the
            given specifiers.
        :raises InvalidSpecifier:
            If the given specifier is invalid (i.e. bad syntax).
        
The operator of this specifier.

        >>> Specifier("==1.2.3").operator
        '=='
        
The version of this specifier.

        >>> Specifier("==1.2.3").version
        '1.2.3'
        
A representation of the Specifier that shows all internal state.

        >>> Specifier('>=1.0.0')
        <Specifier('>=1.0.0')>
        >>> Specifier('>=1.0.0', prereleases=False)
        <Specifier('>=1.0.0', prereleases=False)>
        >>> Specifier('>=1.0.0', prereleases=True)
        <Specifier('>=1.0.0', prereleases=True)>
        
A string representation of the Specifier that can be round-tripped.

        >>> str(Specifier('>=1.0.0'))
        '>=1.0.0'
        >>> str(Specifier('>=1.0.0', prereleases=False))
        '>=1.0.0'
        
Whether or not the two Specifier-like objects are equal.

        :param other: The other object to check against.

        The value of :attr:`prereleases` is ignored.

        >>> Specifier("==1.2.3") == Specifier("== 1.2.3.0")
        True
        >>> (Specifier("==1.2.3", prereleases=False) ==
        ...  Specifier("==1.2.3", prereleases=True))
        True
        >>> Specifier("==1.2.3") == "==1.2.3"
        True
        >>> Specifier("==1.2.3") == Specifier("==1.2.4")
        False
        >>> Specifier("==1.2.3") == Specifier("~=1.2.3")
        False
        
Return whether or not the item is contained in this specifier.

        :param item: The item to check for.

        This is used for the ``in`` operator and behaves the same as
        :meth:`contains` with no ``prereleases`` argument passed.

        >>> "1.2.3" in Specifier(">=1.2.3")
        True
        >>> Version("1.2.3") in Specifier(">=1.2.3")
        True
        >>> "1.0.0" in Specifier(">=1.2.3")
        False
        >>> "1.3.0a1" in Specifier(">=1.2.3")
        False
        >>> "1.3.0a1" in Specifier(">=1.2.3", prereleases=True)
        True
        
Return whether or not the item is contained in this specifier.

        :param item:
            The item to check for, which can be a version string or a
            :class:`Version` instance.
        :param prereleases:
            Whether or not to match prereleases with this Specifier. If set to
            ``None`` (the default), it uses :attr:`prereleases` to determine
            whether or not prereleases are allowed.

        >>> Specifier(">=1.2.3").contains("1.2.3")
        True
        >>> Specifier(">=1.2.3").contains(Version("1.2.3"))
        True
        >>> Specifier(">=1.2.3").contains("1.0.0")
        False
        >>> Specifier(">=1.2.3").contains("1.3.0a1")
        False
        >>> Specifier(">=1.2.3", prereleases=True).contains("1.3.0a1")
        True
        >>> Specifier(">=1.2.3").contains("1.3.0a1", prereleases=True)
        True
        
Filter items in the given iterable, that match the specifier.

        :param iterable:
            An iterable that can contain version strings and :class:`Version` instances.
            The items in the iterable will be filtered according to the specifier.
        :param prereleases:
            Whether or not to allow prereleases in the returned iterator. If set to
            ``None`` (the default), it will be intelligently decide whether to allow
            prereleases or not (based on the :attr:`prereleases` attribute, and
            whether the only versions matching are prereleases).

        This method is smarter than just ``filter(Specifier().contains, [...])``
        because it implements the rule from :pep:`440` that a prerelease item
        SHOULD be accepted if no other versions match the given specifier.

        >>> list(Specifier(">=1.2.3").filter(["1.2", "1.3", "1.5a1"]))
        ['1.3']
        >>> list(Specifier(">=1.2.3").filter(["1.2", "1.2.3", "1.3", Version("1.4")]))
        ['1.2.3', '1.3', <Version('1.4')>]
        >>> list(Specifier(">=1.2.3").filter(["1.2", "1.5a1"]))
        ['1.5a1']
        >>> list(Specifier(">=1.2.3").filter(["1.3", "1.5a1"], prereleases=True))
        ['1.3', '1.5a1']
        >>> list(Specifier(">=1.2.3", prereleases=True).filter(["1.3", "1.5a1"]))
        ['1.3', '1.5a1']
        
Split version into components.

    The split components are intended for version comparison. The logic does
    not attempt to retain the original version string, so joining the
    components back with :func:`_version_join` may not produce the original
    version string.
    
Join split version components into a version string.

    This function assumes the input came from :func:`_version_split`, where the
    first component must be the epoch (either empty or numeric), and all other
    components numeric.
    
This class abstracts handling of a set of version specifiers.

    It can be passed a single specifier (``>=3.0``), a comma-separated list of
    specifiers (``>=3.0,!=3.1``), or no specifier at all.
    
Initialize a SpecifierSet instance.

        :param specifiers:
            The string representation of a specifier or a comma-separated list of
            specifiers which will be parsed and normalized before use.
            May also be an iterable of ``Specifier`` instances, which will be used
            as is.
        :param prereleases:
            This tells the SpecifierSet if it should accept prerelease versions if
            applicable or not. The default of ``None`` will autodetect it from the
            given specifiers.

        :raises InvalidSpecifier:
            If the given ``specifiers`` are not parseable than this exception will be
            raised.
        
A representation of the specifier set that shows all internal state.

        Note that the ordering of the individual specifiers within the set may not
        match the input string.

        >>> SpecifierSet('>=1.0.0,!=2.0.0')
        <SpecifierSet('!=2.0.0,>=1.0.0')>
        >>> SpecifierSet('>=1.0.0,!=2.0.0', prereleases=False)
        <SpecifierSet('!=2.0.0,>=1.0.0', prereleases=False)>
        >>> SpecifierSet('>=1.0.0,!=2.0.0', prereleases=True)
        <SpecifierSet('!=2.0.0,>=1.0.0', prereleases=True)>
        
A string representation of the specifier set that can be round-tripped.

        Note that the ordering of the individual specifiers within the set may not
        match the input string.

        >>> str(SpecifierSet(">=1.0.0,!=1.0.1"))
        '!=1.0.1,>=1.0.0'
        >>> str(SpecifierSet(">=1.0.0,!=1.0.1", prereleases=False))
        '!=1.0.1,>=1.0.0'
        
Return a SpecifierSet which is a combination of the two sets.

        :param other: The other object to combine with.

        >>> SpecifierSet(">=1.0.0,!=1.0.1") & '<=2.0.0,!=2.0.1'
        <SpecifierSet('!=1.0.1,!=2.0.1,<=2.0.0,>=1.0.0')>
        >>> SpecifierSet(">=1.0.0,!=1.0.1") & SpecifierSet('<=2.0.0,!=2.0.1')
        <SpecifierSet('!=1.0.1,!=2.0.1,<=2.0.0,>=1.0.0')>
        
Whether or not the two SpecifierSet-like objects are equal.

        :param other: The other object to check against.

        The value of :attr:`prereleases` is ignored.

        >>> SpecifierSet(">=1.0.0,!=1.0.1") == SpecifierSet(">=1.0.0,!=1.0.1")
        True
        >>> (SpecifierSet(">=1.0.0,!=1.0.1", prereleases=False) ==
        ...  SpecifierSet(">=1.0.0,!=1.0.1", prereleases=True))
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1") == ">=1.0.0,!=1.0.1"
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1") == SpecifierSet(">=1.0.0")
        False
        >>> SpecifierSet(">=1.0.0,!=1.0.1") == SpecifierSet(">=1.0.0,!=1.0.2")
        False
        
Returns the number of specifiers in this specifier set.

        Returns an iterator over all the underlying :class:`Specifier` instances
        in this specifier set.

        >>> sorted(SpecifierSet(">=1.0.0,!=1.0.1"), key=str)
        [<Specifier('!=1.0.1')>, <Specifier('>=1.0.0')>]
        
Return whether or not the item is contained in this specifier.

        :param item: The item to check for.

        This is used for the ``in`` operator and behaves the same as
        :meth:`contains` with no ``prereleases`` argument passed.

        >>> "1.2.3" in SpecifierSet(">=1.0.0,!=1.0.1")
        True
        >>> Version("1.2.3") in SpecifierSet(">=1.0.0,!=1.0.1")
        True
        >>> "1.0.1" in SpecifierSet(">=1.0.0,!=1.0.1")
        False
        >>> "1.3.0a1" in SpecifierSet(">=1.0.0,!=1.0.1")
        False
        >>> "1.3.0a1" in SpecifierSet(">=1.0.0,!=1.0.1", prereleases=True)
        True
        
Return whether or not the item is contained in this SpecifierSet.

        :param item:
            The item to check for, which can be a version string or a
            :class:`Version` instance.
        :param prereleases:
            Whether or not to match prereleases with this SpecifierSet. If set to
            ``None`` (the default), it uses :attr:`prereleases` to determine
            whether or not prereleases are allowed.

        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains("1.2.3")
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains(Version("1.2.3"))
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains("1.0.1")
        False
        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains("1.3.0a1")
        False
        >>> SpecifierSet(">=1.0.0,!=1.0.1", prereleases=True).contains("1.3.0a1")
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains("1.3.0a1", prereleases=True)
        True
        
Filter items in the given iterable, that match the specifiers in this set.

        :param iterable:
            An iterable that can contain version strings and :class:`Version` instances.
            The items in the iterable will be filtered according to the specifier.
        :param prereleases:
            Whether or not to allow prereleases in the returned iterator. If set to
            ``None`` (the default), it will be intelligently decide whether to allow
            prereleases or not (based on the :attr:`prereleases` attribute, and
            whether the only versions matching are prereleases).

        This method is smarter than just ``filter(SpecifierSet(...).contains, [...])``
        because it implements the rule from :pep:`440` that a prerelease item
        SHOULD be accepted if no other versions match the given specifier.

        >>> list(SpecifierSet(">=1.2.3").filter(["1.2", "1.3", "1.5a1"]))
        ['1.3']
        >>> list(SpecifierSet(">=1.2.3").filter(["1.2", "1.3", Version("1.4")]))
        ['1.3', <Version('1.4')>]
        >>> list(SpecifierSet(">=1.2.3").filter(["1.2", "1.5a1"]))
        []
        >>> list(SpecifierSet(">=1.2.3").filter(["1.3", "1.5a1"], prereleases=True))
        ['1.3', '1.5a1']
        >>> list(SpecifierSet(">=1.2.3", prereleases=True).filter(["1.3", "1.5a1"]))
        ['1.3', '1.5a1']

        An "empty" SpecifierSet will filter items based on the presence of prerelease
        versions in the set.

        >>> list(SpecifierSet("").filter(["1.3", "1.5a1"]))
        ['1.3']
        >>> list(SpecifierSet("").filter(["1.5a1"]))
        ['1.5a1']
        >>> list(SpecifierSet("", prereleases=True).filter(["1.3", "1.5a1"]))
        ['1.3', '1.5a1']
        >>> list(SpecifierSet("").filter(["1.3", "1.5a1"], prereleases=True))
        ['1.3', '1.5a1']
        

---



---

PEP 656 support.

This module implements logic to detect if the currently running Python is
linked against musl, and what musl version is used.

Detect currently-running musl runtime version.

    This is done by checking the specified executable's dynamic linking
    information, and invoking the loader to parse its output for a version
    string. If the loader is musl, the output would be something like::

        musl libc (x86_64)
        Version 1.2.2
        Dynamic Program Loader
    
Generate musllinux tags compatible to the current platform.

    :param archs: Sequence of compatible architectures.
        The first one shall be the closest to the actual architecture and be the part of
        platform tag after the ``linux_`` prefix, e.g. ``x86_64``.
        The ``linux_`` prefix is assumed as a prerequisite for the current platform to
        be musllinux-compatible.

    :returns: An iterator of compatible musllinux tags.
    

---


    A representation of the tag triple for a wheel.

    Instances are considered immutable and thus are hashable. Equality checking
    is also supported.
    

    Parses the provided tag (e.g. `py3-none-any`) into a frozenset of Tag instances.

    Returning a set is required due to the possibility that the tag is a
    compressed tag set.
    

    Determine if the ABI corresponds to a threaded (`--disable-gil`) build.

    The threaded builds are indicated by a "t" in the abiflags.
    

    Determine if the Python version supports abi3.

    PEP 384 was first implemented in Python 3.2. The threaded (`--disable-gil`)
    builds do not support abi3.
    

    Yields the tags for a CPython interpreter.

    The tags consist of:
    - cp<python_version>-<abi>-<platform>
    - cp<python_version>-abi3-<platform>
    - cp<python_version>-none-<platform>
    - cp<less than python_version>-abi3-<platform>  # Older Python versions down to 3.2.

    If python_version only specifies a major version then user-provided ABIs and
    the 'none' ABItag will be used.

    If 'abi3' or 'none' are specified in 'abis' then they will be yielded at
    their normal position and not at the beginning.
    

    Return the ABI tag based on EXT_SUFFIX.
    

    Yields the tags for a generic interpreter.

    The tags consist of:
    - <interpreter>-<abi>-<platform>

    The "none" ABI will be added if it was not explicitly provided.
    

    Yields Python versions in descending order.

    After the latest version, the major-only version will be yielded, and then
    all previous versions of that major version.
    

    Yields the sequence of tags that are compatible with a specific version of Python.

    The tags consist of:
    - py*-none-<platform>
    - <interpreter>-none-any  # ... if `interpreter` is provided.
    - py*-none-any
    

    Yields the platform tags for a macOS system.

    The `version` parameter is a two-item tuple specifying the macOS version to
    generate platform tags for. The `arch` parameter is the CPU architecture to
    generate platform tags for. Both parameters default to the appropriate value
    for the current system.
    

    Yields the platform tags for an iOS system.

    :param version: A two-item tuple specifying the iOS version to generate
        platform tags for. Defaults to the current iOS version.
    :param multiarch: The CPU architecture+ABI to generate platform tags for -
        (the value used by `sys.implementation._multiarch` e.g.,
        `arm64_iphoneos` or `x84_64_iphonesimulator`). Defaults to the current
        multiarch value.
    

    Yields the :attr:`~Tag.platform` tags for Android. If this function is invoked on
    non-Android platforms, the ``api_level`` and ``abi`` arguments are required.

    :param int api_level: The maximum `API level
        <https://developer.android.com/tools/releases/platforms>`__ to return. Defaults
        to the current system's version, as returned by ``platform.android_ver``.
    :param str abi: The `Android ABI <https://developer.android.com/ndk/guides/abis>`__,
        e.g. ``arm64_v8a``. Defaults to the current system's ABI , as returned by
        ``sysconfig.get_platform``. Hyphens and periods will be replaced with
        underscores.
    

    Provides the platform tags for this installation.
    

    Returns the name of the running interpreter.

    Some implementations have a reserved, two-letter abbreviation which will
    be returned when appropriate.
    

    Returns the version of the running interpreter.
    

    Returns the sequence of tag triples for the running interpreter.

    The order of the sequence corresponds to priority order for the
    interpreter, from most to least important.
    

---


    An invalid distribution name; users should refer to the packaging user guide.
    

    An invalid wheel filename was found, users should refer to PEP 427.
    

    An invalid sdist filename was found, users should refer to the packaging user guide.
    

    Return a canonical form of a version as a string.

    >>> canonicalize_version('1.0.1')
    '1.0.1'

    Per PEP 625, versions may have multiple canonical forms, differing
    only by trailing zeros.

    >>> canonicalize_version('1.0.0')
    '1'
    >>> canonicalize_version('1.0.0', strip_trailing_zero=False)
    '1.0.0'

    Invalid versions are returned unaltered.

    >>> canonicalize_version('foo bar baz')
    'foo bar baz'
    

---



---

Raised when a license-expression string is invalid

    >>> canonicalize_license_expression("invalid")
    Traceback (most recent call last):
        ...
    packaging.licenses.InvalidLicenseExpression: Invalid license expression: 'invalid'
    

---



---



---



---



---



---


    An error representing the detection of a cycle.
    

    A resolver for Dependency Group data.

    This class handles caching, name normalization, cycle detection, and other
    parsing requirements. There are only two public methods for exploring the data:
    ``lookup()`` and ``resolve()``.

    :param dependency_groups: A mapping, as provided via pyproject
        ``[dependency-groups]``.
    

        Lookup a group name, returning the parsed dependency data for that group.
        This will not resolve includes.

        :param group: the name of the group to lookup

        :raises ValueError: if the data does not appear to be valid dependency group
            data
        :raises TypeError: if the data is not a string
        :raises LookupError: if group name is absent
        :raises packaging.requirements.InvalidRequirement: if a specifier is not valid
        

        Resolve a dependency group to a list of requirements.

        :param group: the name of the group to resolve

        :raises TypeError: if the inputs appear to be the wrong types
        :raises ValueError: if the data does not appear to be valid dependency group
            data
        :raises LookupError: if group name is absent
        :raises packaging.requirements.InvalidRequirement: if a specifier is not valid
        

        This is a helper for cached resolution to strings.

        :param group: The name of the group to resolve.
        :param requested_group: The group which was used in the original, user-facing
            request.
        

    Resolve a dependency group to a tuple of requirements, as strings.

    :param dependency_groups: the parsed contents of the ``[dependency-groups]`` table
        from ``pyproject.toml``
    :param groups: the name of the group(s) to resolve

    :raises TypeError: if the inputs appear to be the wrong types
    :raises ValueError: if the data does not appear to be valid dependency group data
    :raises LookupError: if group name is absent
    :raises packaging.requirements.InvalidRequirement: if a specifier is not valid
    

---

Base exception used by this module.
Base warning used by this module.
Base exception for errors caused within a pool.
Base exception for PoolErrors that have associated URLs.
Raised when SSL certificate fails in an HTTPS connection.
Raised when the connection to a proxy fails.
Raised when automatic decoding based on Content-Type fails.
Raised when something unexpected happens mid-request/response.
Raised when the maximum number of retries is exceeded.

    :param pool: The connection pool
    :type pool: :class:`~urllib3.connectionpool.HTTPConnectionPool`
    :param string url: The requested Url
    :param exceptions.Exception reason: The underlying error

    
Raised when an existing pool gets a request for a foreign host.
Raised when passing an invalid state to a timeout
Raised when a socket timeout error occurs.

    Catching this error will catch both :exc:`ReadTimeoutErrors
    <ReadTimeoutError>` and :exc:`ConnectTimeoutErrors <ConnectTimeoutError>`.
    
Raised when a socket timeout occurs while receiving data from a server
Raised when a socket timeout occurs while connecting to a server
Raised when we fail to establish a new connection. Usually ECONNREFUSED.
Raised when a pool runs out of connections and no more are allowed.
Raised when a request enters a pool after the pool has been closed.
Raised when there is something wrong with a given URL input.
Raised when get_host or similar fails to parse the URL input.
Raised when a URL input has an unsupported scheme.
Used as a container for an error reason supplied in a MaxRetryError.
Warned when performing security reducing actions
Warned when connecting to a host with a certificate missing a SAN.
Warned when making an unverified HTTPS request.
Warned when system time is suspected to be wrong
Warned when certain TLS/SSL configuration is not available on a platform.
Warned when making a HTTPS request without SNI available.

    Warned when an attempt is made to import a module with missing optional
    dependencies.
    
Response needs to be chunked in order to read it as chunks.

    Body should be :class:`http.client.HTTPResponse` like
    (have an fp attribute which returns raw chunks) for read_chunked().
    

    Response length doesn't match expected Content-Length

    Subclass of :class:`http.client.IncompleteRead` to allow int value
    for ``partial`` to avoid creating large objects on streamed reads.
    
Invalid chunk length in a chunked response.
The header provided was somehow invalid.
ProxyManager does not support the supplied scheme
Fetching HTTPS resources through HTTPS proxies is unsupported
Raised by assert_header_parsing, but we convert it to a log.warning statement.
urllib3 encountered an error when trying to rewind a body

---


    Guess the "Content-Type" of a file.

    :param filename:
        The filename to guess the "Content-Type" of using :mod:`mimetypes`.
    :param default:
        If no "Content-Type" can be guessed, default to `default`.
    

    Helper function to format and quote a single header parameter using the
    strategy defined in RFC 2231.

    Particularly useful for header parameters which might contain
    non-ASCII values, like file names. This follows
    `RFC 2388 Section 4.4 <https://tools.ietf.org/html/rfc2388#section-4.4>`_.

    :param name:
        The name of the parameter, a string expected to be ASCII only.
    :param value:
        The value of the parameter, provided as ``bytes`` or `str``.
    :ret:
        An RFC-2231-formatted unicode string.
    

    Helper function to format and quote a single header parameter using the
    HTML5 strategy.

    Particularly useful for header parameters which might contain
    non-ASCII values, like file names. This follows the `HTML5 Working Draft
    Section 4.10.22.7`_ and matches the behavior of curl and modern browsers.

    .. _HTML5 Working Draft Section 4.10.22.7:
        https://w3c.github.io/html/sec-forms.html#multipart-form-data

    :param name:
        The name of the parameter, a string expected to be ASCII only.
    :param value:
        The value of the parameter, provided as ``bytes`` or `str``.
    :ret:
        A unicode string, stripped of troublesome characters.
    

    A data container for request body parameters.

    :param name:
        The name of this request field. Must be unicode.
    :param data:
        The data/value body.
    :param filename:
        An optional filename of the request field. Must be unicode.
    :param headers:
        An optional dict-like object of headers to initially use for the field.
    :param header_formatter:
        An optional callable that is used to encode and format the headers. By
        default, this is :func:`format_header_param_html5`.
    

        A :class:`~urllib3.fields.RequestField` factory from old-style tuple parameters.

        Supports constructing :class:`~urllib3.fields.RequestField` from
        parameter of key/value strings AND key/filetuple. A filetuple is a
        (filename, data, MIME type) tuple where the MIME type is optional.
        For example::

            'foo': 'bar',
            'fakefile': ('foofile.txt', 'contents of foofile'),
            'realfile': ('barfile.txt', open('realfile').read()),
            'typedfile': ('bazfile.bin', open('bazfile').read(), 'image/jpeg'),
            'nonamefile': 'contents of nonamefile field',

        Field names and filenames must be unicode.
        

        Overridable helper function to format a single header parameter. By
        default, this calls ``self.header_formatter``.

        :param name:
            The name of the parameter, a string expected to be ASCII only.
        :param value:
            The value of the parameter, provided as a unicode string.
        

        Helper function to format and quote a single header.

        Useful for single headers that are composed of multiple items. E.g.,
        'Content-Disposition' fields.

        :param header_parts:
            A sequence of (k, v) tuples or a :class:`dict` of (k, v) to format
            as `k1="v1"; k2="v2"; ...`.
        

        Renders the headers for this request field.
        

        Makes this request field into a multipart request field.

        This method overrides "Content-Disposition", "Content-Type" and
        "Content-Location" headers to the request parameter.

        :param content_type:
            The 'Content-Type' of the request body.
        :param content_location:
            The 'Content-Location' of the request body.

        

---


    Based on :class:`http.client.HTTPConnection` but provides an extra constructor
    backwards-compatibility layer between older and newer Pythons.

    Additional keyword parameters are used to configure attributes of the connection.
    Accepted parameters include:

    - ``strict``: See the documentation on :class:`urllib3.connectionpool.HTTPConnectionPool`
    - ``source_address``: Set the source address for the current connection.
    - ``socket_options``: Set specific options on the underlying socket. If not specified, then
      defaults are loaded from ``HTTPConnection.default_socket_options`` which includes disabling
      Nagle's algorithm (sets TCP_NODELAY to 1) unless the connection is behind a proxy.

      For example, if you wish to enable TCP Keep Alive in addition to the defaults,
      you might pass:

      .. code-block:: python

         HTTPConnection.default_socket_options + [
             (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
         ]

      Or you may want to disable the defaults by passing an empty list (e.g., ``[]``).
    

        Getter method to remove any trailing dots that indicate the hostname is an FQDN.

        In general, SSL certificates don't include the trailing dot indicating a
        fully-qualified domain name, and thus, they don't validate properly when
        checked against a domain name that includes the dot. In addition, some
        servers may not expect to receive the trailing dot when provided.

        However, the hostname with trailing dot is critical to DNS resolution; doing a
        lookup with the trailing dot will properly only resolve the appropriate FQDN,
        whereas a lookup without a trailing dot will search the system's search domain
        list. Thus, it's important to keep the original host around for use only in
        those cases where it's appropriate (i.e., when doing DNS lookup to establish the
        actual TCP connection across which we're going to send HTTP requests).
        

        Setter for the `host` property.

        We assume that only urllib3 uses the _dns_host attribute; httplib itself
        only uses `host`, and it seems reasonable that other libraries follow suit.
        
Establish a socket connection and set nodelay settings on it.

        :return: New socket connection.
        
 
 

        Alternative to the common request method, which sends the
        body with chunked encoding and not as one block
        

    Many of the parameters to this constructor are passed to the underlying SSL
    socket by means of :py:func:`urllib3.util.ssl_wrap_socket`.
    

        This method should only be called once, before the connection is used.
        

        Establish a TLS connection to the proxy using the provided SSL context.
        
Used to detect a failed ConnectionCls import.

---


    Create a pool key out of a request context dictionary.

    According to RFC 3986, both the scheme and host are case-insensitive.
    Therefore, this function normalizes both before constructing the pool
    key for an HTTPS request. If you wish to change this behaviour, provide
    alternate callables to ``key_fn_by_scheme``.

    :param key_class:
        The class to use when constructing the key. This should be a namedtuple
        with the ``scheme`` and ``host`` keys at a minimum.
    :type  key_class: namedtuple
    :param request_context:
        A dictionary-like object that contain the context for a request.
    :type  request_context: dict

    :return: A namedtuple that can be used as a connection pool key.
    :rtype:  PoolKey
    

    Allows for arbitrary requests while transparently keeping track of
    necessary connection pools for you.

    :param num_pools:
        Number of connection pools to cache before discarding the least
        recently used pool.

    :param headers:
        Headers to include with all requests, unless other headers are given
        explicitly.

    :param \\**connection_pool_kw:
        Additional parameters are used to create fresh
        :class:`urllib3.connectionpool.ConnectionPool` instances.

    Example::

        >>> manager = PoolManager(num_pools=2)
        >>> r = manager.request('GET', 'http://google.com/')
        >>> r = manager.request('GET', 'http://google.com/mail')
        >>> r = manager.request('GET', 'http://yahoo.com/')
        >>> len(manager.pools)
        2

    

        Create a new :class:`urllib3.connectionpool.ConnectionPool` based on host, port, scheme, and
        any additional pool keyword arguments.

        If ``request_context`` is provided, it is provided as keyword arguments
        to the pool class used. This method is used to actually create the
        connection pools handed out by :meth:`connection_from_url` and
        companion methods. It is intended to be overridden for customization.
        

        Empty our store of pools and direct them all to close.

        This will not affect in-flight connections, but they will not be
        re-used after completion.
        

        Get a :class:`urllib3.connectionpool.ConnectionPool` based on the host, port, and scheme.

        If ``port`` isn't given, it will be derived from the ``scheme`` using
        ``urllib3.connectionpool.port_by_scheme``. If ``pool_kwargs`` is
        provided, it is merged with the instance's ``connection_pool_kw``
        variable and used to create the new connection pool, if one is
        needed.
        

        Get a :class:`urllib3.connectionpool.ConnectionPool` based on the request context.

        ``request_context`` must at least contain the ``scheme`` key and its
        value must be a key in ``key_fn_by_scheme`` instance variable.
        

        Get a :class:`urllib3.connectionpool.ConnectionPool` based on the provided pool key.

        ``pool_key`` should be a namedtuple that only contains immutable
        objects. At a minimum it must have the ``scheme``, ``host``, and
        ``port`` fields.
        

        Similar to :func:`urllib3.connectionpool.connection_from_url`.

        If ``pool_kwargs`` is not provided and a new pool needs to be
        constructed, ``self.connection_pool_kw`` is used to initialize
        the :class:`urllib3.connectionpool.ConnectionPool`. If ``pool_kwargs``
        is provided, it is used instead. Note that if a new pool does not
        need to be created for the request, the provided ``pool_kwargs`` are
        not used.
        

        Merge a dictionary of override values for self.connection_pool_kw.

        This does not modify self.connection_pool_kw and returns a new dict.
        Any keys in the override dictionary with a value of ``None`` are
        removed from the merged dictionary.
        

        Indicates if the proxy requires the complete destination URL in the
        request.  Normally this is only needed when not using an HTTP CONNECT
        tunnel.
        

        Validates that were not attempting to do TLS in TLS connections on
        Python2 or with unsupported SSL implementations.
        

        Same as :meth:`urllib3.HTTPConnectionPool.urlopen`
        with custom cross-host redirect logic and only sends the request-uri
        portion of the ``url``.

        The given ``url`` parameter must be absolute, such that an appropriate
        :class:`urllib3.connectionpool.ConnectionPool` can be chosen for it.
        

    Behaves just like :class:`PoolManager`, but sends all requests through
    the defined proxy, using the CONNECT method for HTTPS URLs.

    :param proxy_url:
        The URL of the proxy to be used.

    :param proxy_headers:
        A dictionary containing headers that will be sent to the proxy. In case
        of HTTP they are being sent with each request, while in the
        HTTPS/CONNECT case they are sent only once. Could be used for proxy
        authentication.

    :param proxy_ssl_context:
        The proxy SSL context is used to establish the TLS connection to the
        proxy when using HTTPS proxies.

    :param use_forwarding_for_https:
        (Defaults to False) If set to True will forward requests to the HTTPS
        proxy to be made on behalf of the client instead of creating a TLS
        tunnel via the CONNECT method. **Enabling this flag means that request
        and response headers and content will be visible from the HTTPS proxy**
        whereas tunneling keeps request and response headers and content
        private.  IP address, target hostname, SNI, and port are always visible
        to an HTTPS proxy even when this flag is disabled.

    Example:
        >>> proxy = urllib3.ProxyManager('http://localhost:3128/')
        >>> r1 = proxy.request('GET', 'http://google.com/')
        >>> r2 = proxy.request('GET', 'http://httpbin.org/')
        >>> len(proxy.pools)
        1
        >>> r3 = proxy.request('GET', 'https://httpbin.org/')
        >>> r4 = proxy.request('GET', 'https://twitter.com/')
        >>> len(proxy.pools)
        3

    

        Sets headers needed by proxies: specifically, the Accept and Host
        headers. Only sets headers not provided by the user.
        

---


    Our embarrassingly-simple replacement for mimetools.choose_boundary.
    

    Iterate over fields.

    Supports list of (k, v) tuples and dicts, and lists of
    :class:`~urllib3.fields.RequestField`.

    

    .. deprecated:: 1.6

    Iterate over fields.

    The addition of :class:`~urllib3.fields.RequestField` makes this function
    obsolete. Instead, use :func:`iter_field_objects`, which returns
    :class:`~urllib3.fields.RequestField` objects.

    Supports list of (k, v) tuples and dicts.
    

    Encode a dictionary of ``fields`` using the multipart/form-data MIME format.

    :param fields:
        Dictionary of fields or list of (key, :class:`~urllib3.fields.RequestField`).

    :param boundary:
        If not specified, then a random boundary will be generated using
        :func:`urllib3.filepost.choose_boundary`.
    

---


    From RFC7231:
        If one or more encodings have been applied to a representation, the
        sender that applied the encodings MUST generate a Content-Encoding
        header field that lists the content codings in the order in which
        they were applied.
    

    HTTP Response container.

    Backwards-compatible with :class:`http.client.HTTPResponse` but the response ``body`` is
    loaded and decoded on-demand when the ``data`` property is accessed.  This
    class is also compatible with the Python standard library's :mod:`io`
    module, and can hence be treated as a readable object in the context of that
    framework.

    Extra parameters for behaviour not present in :class:`http.client.HTTPResponse`:

    :param preload_content:
        If True, the response's body will be preloaded during construction.

    :param decode_content:
        If True, will attempt to decode the body based on the
        'content-encoding' header.

    :param original_response:
        When this HTTPResponse wrapper is generated from an :class:`http.client.HTTPResponse`
        object, it's convenient to include the original for debug purposes. It's
        otherwise unused.

    :param retries:
        The retries contains the last :class:`~urllib3.util.retry.Retry` that
        was used during the request.

    :param enforce_content_length:
        Enforce content length checking. Body returned by server must match
        value of Content-Length header, if present. Otherwise, raise error.
    

        Should we redirect and where to?

        :returns: Truthy redirect location string if we got a redirect status
            code and valid location. ``None`` if redirect status and no
            location. ``False`` if not a redirect status code.
        

        Read and discard any remaining HTTP response data in the response connection.

        Unread data in the HTTPResponse connection blocks the connection from being released back to the pool.
        

        Obtain the number of bytes pulled over the wire so far. May differ from
        the amount of content returned by :meth:``urllib3.response.HTTPResponse.read``
        if bytes are encoded on the wire (e.g, compressed).
        

        Set initial length value for Response content if available.
        

        Set-up the _decoder attribute if necessary.
        

        Decode the data passed in and potentially flush the decoder.
        

        Flushes the decoder. Should only be called if the decoder is actually
        being used.
        

        Catch low-level python exceptions, instead re-raising urllib3
        variants, so that low-level exceptions are not leaked in the
        high-level api.

        On exit, release the connection back to the pool.
        

        Read a response with the thought that reading the number of bytes
        larger than can fit in a 32-bit int at a time via SSL in some
        known cases leads to an overflow error that has to be prevented
        if `amt` or `self.length_remaining` indicate that a problem may
        happen.

        The known cases:
          * 3.8 <= CPython < 3.9.7 because of a bug
            https://github.com/urllib3/urllib3/issues/2513#issuecomment-1152559900.
          * urllib3 injected with pyOpenSSL-backed SSL-support.
          * CPython < 3.10 only when `amt` does not fit 32-bit int.
        

        Similar to :meth:`http.client.HTTPResponse.read`, but with two additional
        parameters: ``decode_content`` and ``cache_content``.

        :param amt:
            How much of the content to read. If specified, caching is skipped
            because it doesn't make sense to cache partial content as the full
            response.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.

        :param cache_content:
            If True, will save the returned data such that the same result is
            returned despite of the state of the underlying file object. This
            is useful if you want the ``.data`` property to continue working
            after having ``.read()`` the file object. (Overridden if ``amt`` is
            set.)
        

        A generator wrapper for the read() method. A call will block until
        ``amt`` bytes have been read from the connection or until the
        connection is closed.

        :param amt:
            How much of the content to read. The generator will return up to
            much data per iteration, but may return less. This is particularly
            likely when using compressed data. However, the empty string will
            never be returned.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.
        

        Given an :class:`http.client.HTTPResponse` instance ``r``, return a
        corresponding :class:`urllib3.response.HTTPResponse` object.

        Remaining parameters are passed to the HTTPResponse constructor, along
        with ``original_response=r``.
        

        Checks if the underlying file-like object looks like a
        :class:`http.client.HTTPResponse` object. We do this by testing for
        the fp attribute. If it is present we assume it returns raw chunks as
        processed by read_chunked().
        

        Similar to :meth:`HTTPResponse.read`, but with an additional
        parameter: ``decode_content``.

        :param amt:
            How much of the content to read. If specified, caching is skipped
            because it doesn't make sense to cache partial content as the full
            response.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.
        

        Returns the URL that was the source of this response.
        If the request that generated this response redirected, this method
        will return the final redirect location.
        

---



---


    Provides a thread-safe dict-like container which maintains up to
    ``maxsize`` keys while throwing away the least-recently-used keys beyond
    ``maxsize``.

    :param maxsize:
        Maximum number of recent elements to retain.

    :param dispose_func:
        Every time an item is evicted from the container,
        ``dispose_func(value)`` is called.  Callback which will get called
    

    :param headers:
        An iterable of field-value pairs. Must not contain multiple field names
        when compared case-insensitively.

    :param kwargs:
        Additional field-value pairs to pass in to ``dict.update``.

    A ``dict`` like container for storing HTTP Headers.

    Field names are stored and compared case-insensitively in compliance with
    RFC 7230. Iteration provides the first case-sensitive key seen for each
    case-insensitive pair.

    Using ``__setitem__`` syntax overwrites fields that compare equal
    case-insensitively in order to maintain ``dict``'s api. For fields that
    compare equal, instead create a new ``HTTPHeaderDict`` and use ``.add``
    in a loop.

    If multiple fields that are equal case-insensitively are passed to the
    constructor or ``.update``, the behavior is undefined and some will be
    lost.

    >>> headers = HTTPHeaderDict()
    >>> headers.add('Set-Cookie', 'foo=bar')
    >>> headers.add('set-cookie', 'baz=quxx')
    >>> headers['content-length'] = '7'
    >>> headers['SET-cookie']
    'foo=bar, baz=quxx'
    >>> headers['Content-Length']
    '7'
    
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised.
        
Adds a (name, value) pair, doesn't overwrite the value if it already
        exists.

        >>> headers = HTTPHeaderDict(foo='bar')
        >>> headers.add('Foo', 'baz')
        >>> headers['foo']
        'bar, baz'
        
Generic import function for any type of header-like object.
        Adapted version of MutableMapping.update in order to insert items
        with self.add instead of self.__setitem__
        
Returns a list of all the values for the named field. Returns an
        empty list if the key doesn't exist.

        Remove content-specific header fields before changing the request
        method to GET or HEAD according to RFC 9110, Section 15.4.
        
Iterate over all header lines, including duplicate ones.
Iterate over all headers, merging duplicate ones together.
Read headers from a Python 2 httplib message object.

---


Python HTTP library with thread-safe connection pooling, file post support, user friendly, and more


    Helper for quickly adding a StreamHandler to the logger. Useful for
    debugging.

    Returns the handler after adding it.
    

    Helper for quickly disabling all urllib3 warnings.
    

---


    Base class for all connection pools, such as
    :class:`.HTTPConnectionPool` and :class:`.HTTPSConnectionPool`.

    .. note::
       ConnectionPool.urlopen() does not normalize or percent-encode target URIs
       which is useful if your target server doesn't support percent-encoded
       target URIs.
    

        Close all pooled connections and disable the pool.
        

    Thread-safe connection pool for one host.

    :param host:
        Host used for this HTTP Connection (e.g. "localhost"), passed into
        :class:`http.client.HTTPConnection`.

    :param port:
        Port used for this HTTP Connection (None is equivalent to 80), passed
        into :class:`http.client.HTTPConnection`.

    :param strict:
        Causes BadStatusLine to be raised if the status line can't be parsed
        as a valid HTTP/1.0 or 1.1 status line, passed into
        :class:`http.client.HTTPConnection`.

        .. note::
           Only works in Python 2. This parameter is ignored in Python 3.

    :param timeout:
        Socket timeout in seconds for each individual connection. This can
        be a float or integer, which sets the timeout for the HTTP request,
        or an instance of :class:`urllib3.util.Timeout` which gives you more
        fine-grained control over request timeouts. After the constructor has
        been parsed, this is always a `urllib3.util.Timeout` object.

    :param maxsize:
        Number of connections to save that can be reused. More than 1 is useful
        in multithreaded situations. If ``block`` is set to False, more
        connections will be created but they will not be saved once they've
        been used.

    :param block:
        If set to True, no more than ``maxsize`` connections will be used at
        a time. When no free connections are available, the call will block
        until a connection has been released. This is a useful side effect for
        particular multithreaded situations where one does not want to use more
        than maxsize connections per host to prevent flooding.

    :param headers:
        Headers to include with all requests, unless other headers are given
        explicitly.

    :param retries:
        Retry configuration to use by default with requests in this pool.

    :param _proxy:
        Parsed proxy URL, should not be used directly, instead, see
        :class:`urllib3.ProxyManager`

    :param _proxy_headers:
        A dictionary with proxy headers, should not be used directly,
        instead, see :class:`urllib3.ProxyManager`

    :param \\**conn_kw:
        Additional parameters are used to create fresh :class:`urllib3.connection.HTTPConnection`,
        :class:`urllib3.connection.HTTPSConnection` instances.
    

        Return a fresh :class:`HTTPConnection`.
        

        Get a connection. Will return a pooled connection if one is available.

        If no connections are available and :prop:`.block` is ``False``, then a
        fresh connection is returned.

        :param timeout:
            Seconds to wait before giving up and raising
            :class:`urllib3.exceptions.EmptyPoolError` if the pool is empty and
            :prop:`.block` is ``True``.
        

        Put a connection back into the pool.

        :param conn:
            Connection object for the current host and port as returned by
            :meth:`._new_conn` or :meth:`._get_conn`.

        If the pool is already full, the connection is closed and discarded
        because we exceeded maxsize. If connections are discarded frequently,
        then maxsize should be increased.

        If the pool is closed, then the connection will be closed and discarded.
        

        Called right before a request is made, after the socket is created.
        
Helper that always returns a :class:`urllib3.util.Timeout`
Is the error actually a timeout? Will raise a ReadTimeout or pass

        Perform a request on a given urllib connection object taken from our
        pool.

        :param conn:
            a connection from one of our connection pools

        :param timeout:
            Socket timeout in seconds for the request. This can be a
            float or integer, which will set the same timeout value for
            the socket connect and the socket read, or an instance of
            :class:`urllib3.util.Timeout`, which gives you more fine-grained
            control over your timeouts.
        

        Close all pooled connections and disable the pool.
        

        Check if the given ``url`` is a member of the same host as this
        connection pool.
        

        Get a connection from the pool and perform an HTTP request. This is the
        lowest level call for making a request, so you'll need to specify all
        the raw details.

        .. note::

           More commonly, it's appropriate to use a convenience method provided
           by :class:`.RequestMethods`, such as :meth:`request`.

        .. note::

           `release_conn` will only behave as expected if
           `preload_content=False` because we want to make
           `preload_content=False` the default behaviour someday soon without
           breaking backwards compatibility.

        :param method:
            HTTP request method (such as GET, POST, PUT, etc.)

        :param url:
            The URL to perform the request on.

        :param body:
            Data to send in the request body, either :class:`str`, :class:`bytes`,
            an iterable of :class:`str`/:class:`bytes`, or a file-like object.

        :param headers:
            Dictionary of custom headers to send, such as User-Agent,
            If-None-Match, etc. If None, pool headers are used. If provided,
            these headers completely replace any pool-specific headers.

        :param retries:
            Configure the number of retries to allow before raising a
            :class:`~urllib3.exceptions.MaxRetryError` exception.

            Pass ``None`` to retry until you receive a response. Pass a
            :class:`~urllib3.util.retry.Retry` object for fine-grained control
            over different types of retries.
            Pass an integer number to retry connection errors that many times,
            but no other types of errors. Pass zero to never retry.

            If ``False``, then retries are disabled and any exception is raised
            immediately. Also, instead of raising a MaxRetryError on redirects,
            the redirect response will be returned.

        :type retries: :class:`~urllib3.util.retry.Retry`, False, or an int.

        :param redirect:
            If True, automatically handle redirects (status codes 301, 302,
            303, 307, 308). Each redirect counts as a retry. Disabling retries
            will disable redirect, too.

        :param assert_same_host:
            If ``True``, will make sure that the host of the pool requests is
            consistent else will raise HostChangedError. When ``False``, you can
            use the pool on an HTTP proxy and request foreign hosts.

        :param timeout:
            If specified, overrides the default timeout for this one
            request. It may be a float (in seconds) or an instance of
            :class:`urllib3.util.Timeout`.

        :param pool_timeout:
            If set and the pool is set to block=True, then this method will
            block for ``pool_timeout`` seconds and raise EmptyPoolError if no
            connection is available within the time period.

        :param release_conn:
            If False, then the urlopen call will not release the connection
            back into the pool once a response is received (but will release if
            you read the entire contents of the response such as when
            `preload_content=True`). This is useful if you're not preloading
            the response's content immediately. You will need to call
            ``r.release_conn()`` on the response ``r`` to return the connection
            back into the pool. If None, it takes the value of
            ``response_kw.get('preload_content', True)``.

        :param chunked:
            If True, urllib3 will send the body using chunked transfer
            encoding. Otherwise, urllib3 will send the body using the standard
            content-length form. Defaults to False.

        :param int body_pos:
            Position to seek to in file-like body in the event of a retry or
            redirect. Typically this won't need to be set because urllib3 will
            auto-populate the value when needed.

        :param \\**response_kw:
            Additional parameters are passed to
            :meth:`urllib3.response.HTTPResponse.from_httplib`
        

    Same as :class:`.HTTPConnectionPool`, but HTTPS.

    :class:`.HTTPSConnection` uses one of ``assert_fingerprint``,
    ``assert_hostname`` and ``host`` in this order to verify connections.
    If ``assert_hostname`` is False, no verification is done.

    The ``key_file``, ``cert_file``, ``cert_reqs``, ``ca_certs``,
    ``ca_cert_dir``, ``ssl_version``, ``key_password`` are only used if :mod:`ssl`
    is available and are fed into :meth:`urllib3.util.ssl_wrap_socket` to upgrade
    the connection socket into an SSL socket.
    

        Prepare the ``connection`` for :meth:`urllib3.util.ssl_wrap_socket`
        and establish the tunnel if proxy is used.
        

        Establishes a tunnel connection through HTTP CONNECT.

        Tunnel connection is established early because otherwise httplib would
        improperly set Host: header to proxy's IP:port.
        

        Return a fresh :class:`http.client.HTTPSConnection`.
        

        Called right before a request is made, after the socket is created.
        

    Given a url, return an :class:`.ConnectionPool` instance of its host.

    This is a shortcut for not having to parse out the scheme, host, and port
    of the url before creating an :class:`.ConnectionPool` instance.

    :param url:
        Absolute URL string that must include the scheme. Port is optional.

    :param \\**kw:
        Passes additional parameters to the constructor of the appropriate
        :class:`.ConnectionPool`. Useful for specifying things like
        timeout, maxsize, headers, etc.

    Example::

        >>> conn = connection_from_url('http://google.com/')
        >>> r = conn.request('GET', '/')
    

    Normalize hosts for comparisons and use with sockets.
    
Drains a queue of connections and closes each one.

---


    Convenience mixin for classes who implement a :meth:`urlopen` method, such
    as :class:`urllib3.HTTPConnectionPool` and
    :class:`urllib3.PoolManager`.

    Provides behavior for making common types of HTTP request methods and
    decides which type of request field encoding to use.

    Specifically,

    :meth:`.request_encode_url` is for sending requests whose fields are
    encoded in the URL (such as GET, HEAD, DELETE).

    :meth:`.request_encode_body` is for sending requests whose fields are
    encoded in the *body* of the request using multipart or www-form-urlencoded
    (such as for POST, PUT, PATCH).

    :meth:`.request` is for making any kind of request, it will look up the
    appropriate encoding format and use one of the above two methods to make
    the request.

    Initializer parameters:

    :param headers:
        Headers to include with all requests, unless other headers are given
        explicitly.
    

        Make a request using :meth:`urlopen` with the appropriate encoding of
        ``fields`` based on the ``method`` used.

        This is a convenience method that requires the least amount of manual
        effort. It can be used in most situations, while still having the
        option to drop down to more specific methods when necessary, such as
        :meth:`request_encode_url`, :meth:`request_encode_body`,
        or even the lowest level :meth:`urlopen`.
        

        Make a request using :meth:`urlopen` with the ``fields`` encoded in
        the url. This is useful for request methods like GET, HEAD, DELETE, etc.
        

        Make a request using :meth:`urlopen` with the ``fields`` encoded in
        the body. This is useful for request methods like POST, PUT, PATCH, etc.

        When ``encode_multipart=True`` (default), then
        :func:`urllib3.encode_multipart_formdata` is used to encode
        the payload with the appropriate content type. Otherwise
        :func:`urllib.parse.urlencode` is used with the
        'application/x-www-form-urlencoded' content type.

        Multipart encoding must be used when posting files, and it's reasonably
        safe to use it in other times too. However, it may break request
        signing, such as with OAuth.

        Supports an optional ``fields`` parameter of key/value strings AND
        key/filetuple. A filetuple is a (filename, data, MIME type) tuple where
        the MIME type is optional. For example::

            fields = {
                'foo': 'bar',
                'fakefile': ('foofile.txt', 'contents of foofile'),
                'realfile': ('barfile.txt', open('realfile').read()),
                'typedfile': ('bazfile.bin', open('bazfile').read(),
                              'image/jpeg'),
                'nonamefile': 'contents of nonamefile field',
            }

        When uploading a file, providing a filename (the first parameter of the
        tuple) is optional but recommended to best mimic behavior of browsers.

        Note that if ``headers`` are supplied, the 'Content-Type' header will
        be overwritten because it depends on the dynamic random boundary string
        which is used to compose the body of the request. The random boundary
        string can be explicitly set with the ``multipart_boundary`` parameter.
        

            If user tries to call this module directly urllib3 v2.x style raise an error to the user
            suggesting they may need urllib3 v2
            

---


TLS with SNI_-support for Python 2. Follow these instructions if you would
like to verify TLS certificates in Python 2. Note, the default libraries do
*not* do certificate checking; you need to do additional work to validate
certificates yourself.

This needs the following packages installed:

* `pyOpenSSL`_ (tested with 16.0.0)
* `cryptography`_ (minimum 1.3.4, from pyopenssl)
* `idna`_ (minimum 2.0, from cryptography)

However, pyopenssl depends on cryptography, which depends on idna, so while we
use all three directly here we end up having relatively few packages required.

You can install them with the following command:

.. code-block:: bash

    $ python -m pip install pyopenssl cryptography idna

To activate certificate checking, call
:func:`~urllib3.contrib.pyopenssl.inject_into_urllib3` from your Python code
before you begin making HTTP requests. This can be done in a ``sitecustomize``
module, or at any other time before your application begins using ``urllib3``,
like this:

.. code-block:: python

    try:
        import pip._vendor.urllib3.contrib.pyopenssl as pyopenssl
        pyopenssl.inject_into_urllib3()
    except ImportError:
        pass

Now you can use :mod:`urllib3` as you normally would, and it will support SNI
when the required modules are installed.

Activating this module also has the positive side effect of disabling SSL/TLS
compression in Python 2 (see `CRIME attack`_).

.. _sni: https://en.wikipedia.org/wiki/Server_Name_Indication
.. _crime attack: https://en.wikipedia.org/wiki/CRIME_(security_exploit)
.. _pyopenssl: https://www.pyopenssl.org
.. _cryptography: https://cryptography.io
.. _idna: https://github.com/kjd/idna


    Verifies that PyOpenSSL's package-level dependencies have been met.
    Throws `ImportError` if they are not met.
    

    Converts a dNSName SubjectAlternativeName field to the form used by the
    standard library on the given Python version.

    Cryptography produces a dNSName as a unicode string that was idna-decoded
    from ASCII bytes. We need to idna-encode that string to get it back, and
    then on Python 3 we also need to convert to unicode via UTF-8 (the stdlib
    uses PyUnicode_FromStringAndSize on it, which decodes via UTF-8).

    If the name cannot be idna-encoded then we return None signalling that
    the name given should be skipped.
    

        Borrowed wholesale from the Python Cryptography Project. It turns out
        that we can't just safely call `idna.encode`: it can explode for
        wildcard names. This avoids that problem.
        

    Given an PyOpenSSL certificate, provides all the subject alternative names.
    
API-compatibility wrapper for Python OpenSSL's Connection-class.

    Note: _makefile_refs, _drop() and _reuse() are needed for the garbage
    collector of pypy.
    

    I am a wrapper class for the PyOpenSSL ``Context`` object. I am responsible
    for translating the interface of the standard library ``SSLContext`` object
    to calls into PyOpenSSL.
    

---


NTLM authenticating pool, contributed by erikcederstran

Issue #10, see: http://code.google.com/p/urllib3/issues/detail?id=10


    Implements an NTLM authentication version of an urllib3 connection pool
    

        authurl is a random URL on the server that is protected by NTLM.
        user is the Windows user, probably in the DOMAIN\\username format.
        pw is the password for the user.
        

---


This module contains provisional support for SOCKS proxies from within
urllib3. This module supports SOCKS4, SOCKS4A (an extension of SOCKS4), and
SOCKS5. To enable its functionality, either install PySocks or install this
module with the ``socks`` extra.

The SOCKS implementation supports the full range of urllib3 features. It also
supports the following SOCKS features:

- SOCKS4A (``proxy_url='socks4a://...``)
- SOCKS4 (``proxy_url='socks4://...``)
- SOCKS5 with remote DNS (``proxy_url='socks5h://...``)
- SOCKS5 with local DNS (``proxy_url='socks5://...``)
- Usernames and passwords for the SOCKS proxy

.. note::
   It is recommended to use ``socks5h://`` or ``socks4a://`` schemes in
   your ``proxy_url`` to ensure that DNS resolution is done from the remote
   server instead of client-side when connecting to a domain name.

SOCKS4 supports IPv4 and domain names with the SOCKS4A extension. SOCKS5
supports IPv4, IPv6, and domain names.

When connecting to a SOCKS4 proxy the ``username`` portion of the ``proxy_url``
will be sent as the ``userid`` section of the SOCKS request:

.. code-block:: python

    proxy_url="socks4a://<userid>@proxy-host"

When connecting to a SOCKS5 proxy the ``username`` and ``password`` portion
of the ``proxy_url`` will be sent as the username/password to authenticate
with the proxy:

.. code-block:: python

    proxy_url="socks5h://<username>:<password>@proxy-host"



    A plain-text HTTP connection that connects via a SOCKS proxy.
    

        Establish a new connection via the SOCKS proxy.
        

    A version of the urllib3 ProxyManager that routes connections via the
    defined SOCKS proxy.
    

---


This module provides a pool manager that uses Google App Engine's
`URLFetch Service <https://cloud.google.com/appengine/docs/python/urlfetch>`_.

Example usage::

    from pip._vendor.urllib3 import PoolManager
    from pip._vendor.urllib3.contrib.appengine import AppEngineManager, is_appengine_sandbox

    if is_appengine_sandbox():
        # AppEngineManager uses AppEngine's URLFetch API behind the scenes
        http = AppEngineManager()
    else:
        # PoolManager uses a socket-level API behind the scenes
        http = PoolManager()

    r = http.request('GET', 'https://google.com/')

There are `limitations <https://cloud.google.com/appengine/docs/python/\
urlfetch/#Python_Quotas_and_limits>`_ to the URLFetch service and it may not be
the best choice for your application. There are three options for using
urllib3 on Google App Engine:

1. You can use :class:`AppEngineManager` with URLFetch. URLFetch is
   cost-effective in many circumstances as long as your usage is within the
   limitations.
2. You can use a normal :class:`~urllib3.PoolManager` by enabling sockets.
   Sockets also have `limitations and restrictions
   <https://cloud.google.com/appengine/docs/python/sockets/\
   #limitations-and-restrictions>`_ and have a lower free quota than URLFetch.
   To use sockets, be sure to specify the following in your ``app.yaml``::

        env_variables:
            GAE_USE_SOCKETS_HTTPLIB : 'true'

3. If you are using `App Engine Flexible
<https://cloud.google.com/appengine/docs/flexible/>`_, you can use the standard
:class:`PoolManager` without any configuration or special environment variables.


    Connection manager for Google App Engine sandbox applications.

    This manager uses the URLFetch service directly instead of using the
    emulated httplib, and is subject to URLFetch limitations as described in
    the App Engine documentation `here
    <https://cloud.google.com/appengine/docs/python/urlfetch>`_.

    Notably it will raise an :class:`AppEnginePlatformError` if:
        * URLFetch is not available.
        * If you attempt to use this on App Engine Flexible, as full socket
          support is available.
        * If a request size is more than 10 megabytes.
        * If a response size is more than 32 megabytes.
        * If you use an unsupported request method such as OPTIONS.

    Beyond those cases, it will raise normal urllib3 errors.
    

---


SecureTranport support for urllib3 via ctypes.

This makes platform-native TLS available to urllib3 users on macOS without the
use of a compiler. This is an important feature because the Python Package
Index is moving to become a TLSv1.2-or-higher server, and the default OpenSSL
that ships with macOS is not capable of doing TLSv1.2. The only way to resolve
this is to give macOS users an alternative solution to the problem, and that
solution is to use SecureTransport.

We use ctypes here because this solution must not require a compiler. That's
because pip is not allowed to require a compiler either.

This is not intended to be a seriously long-term solution to this problem.
The hope is that PEP 543 will eventually solve this issue for us, at which
point we can retire this contrib module. But in the short term, we need to
solve the impending tire fire that is Python on Mac without this kind of
contrib module. So...here we are.

To use this module, simply import and inject it::

    import pip._vendor.urllib3.contrib.securetransport as securetransport
    securetransport.inject_into_urllib3()

Happy TLSing!

This code is a bastardised version of the code found in Will Bond's oscrypto
library. An enormous debt is owed to him for blazing this trail for us. For
that reason, this code should be considered to be covered both by urllib3's
license and by oscrypto's:

.. code-block::

    Copyright (c) 2015-2016 Will Bond <will@wbond.net>

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.


    Monkey-patch urllib3 with SecureTransport-backed SSL-support.
    

    Undo monkey-patching by :func:`inject_into_urllib3`.
    

    SecureTransport read callback. This is called by ST to request that data
    be returned from the socket.
    

    SecureTransport write callback. This is called by ST to request that data
    actually be sent on the network.
    

    API-compatibility wrapper for Python's OpenSSL wrapped socket object.

    Note: _makefile_refs, _drop(), and _reuse() are needed for the garbage
    collector of PyPy.
    

        A context manager that can be used to wrap calls that do I/O from
        SecureTransport. If any of the I/O callbacks hit an exception, this
        context manager will correctly propagate the exception after the fact.
        This avoids silently swallowing those exceptions.

        It also correctly forces the socket closed.
        

        Sets up the allowed ciphers. By default this matches the set in
        util.ssl_.DEFAULT_CIPHERS, at least as supported by macOS. This is done
        custom and doesn't allow changing at this time, mostly because parsing
        OpenSSL cipher strings is going to be a freaking nightmare.
        

        Sets up the ALPN protocols on the context.
        

        Called when we have set custom validation. We do this in two cases:
        first, when cert validation is entirely disabled; and second, when
        using a custom trust DB.
        Raises an SSLError if the connection is not trusted.
        

        Actually performs the TLS handshake. This is run automatically by
        wrapped socket, and shouldn't be needed in user code.
        

    I am a wrapper class for the SecureTransport library, to translate the
    interface of the standard library ``SSLContext`` object to calls into
    SecureTransport.
    

        SecureTransport cannot have its hostname checking disabled. For more,
        see the comment on getpeercert() in this file.
        

        SecureTransport cannot have its hostname checking disabled. For more,
        see the comment on getpeercert() in this file.
        

        Sets the ALPN protocols that will later be set on the context.

        Raises a NotImplementedError if ALPN is not supported.
        

---



---


This module provides means to detect the App Engine environment.

Reports if the app is running in the first generation sandbox.

    The second generation runtimes are technically still in a sandbox, but it
    is much less restrictive, so generally you shouldn't need to check for it.
    see https://cloud.google.com/appengine/docs/standard/runtimes
    
Deprecated.

---


Low-level helpers for the SecureTransport bindings.

These are Python functions that are not directly related to the high-level APIs
but are necessary to get them to work. They include a whole bunch of low-level
CoreFoundation messing about and memory management. The concerns in this module
are almost entirely about trying to avoid memory leaks and providing
appropriate and useful assistance to the higher-level code.


    Given a bytestring, create a CFData object from it. This CFData object must
    be CFReleased by the caller.
    

    Given a list of Python tuples, create an associated CFDictionary.
    

    Given a Python binary data, create a CFString.
    The string must be CFReleased by the caller.
    

    Given a list of Python binary data, create an associated CFMutableArray.
    The array must be CFReleased by the caller.

    Raises an ssl.SSLError on failure.
    

    Creates a Unicode string from a CFString object. Used entirely for error
    reporting.

    Yes, it annoys me quite a lot that this function is this complex.
    

    Checks the return code and throws an exception if there is an error to
    report
    

    Given a bundle of certs in PEM format, turns them into a CFArray of certs
    that can be used to validate a cert chain.
    

    Returns True if a given CFTypeRef is a certificate.
    

    Returns True if a given CFTypeRef is an identity.
    

    This function creates a temporary Mac keychain that we can use to work with
    credentials. This keychain uses a one-time password and a temporary file to
    store the data. We expect to have one keychain per socket. The returned
    SecKeychainRef must be freed by the caller, including calling
    SecKeychainDelete.

    Returns a tuple of the SecKeychainRef and the path to the temporary
    directory that contains it.
    

    Given a single file, loads all the trust objects from it into arrays and
    the keychain.
    Returns a tuple of lists: the first list is a list of identities, the
    second a list of certs.
    

    Load certificates and maybe keys from a number of files. Has the end goal
    of returning a CFArray containing one SecIdentityRef, and then zero or more
    SecCertificateRef objects, suitable for use as a client certificate trust
    chain.
    

    Builds a TLS alert record for an unknown CA.
    

---



---


This module uses ctypes to bind a whole bunch of functions and constants from
SecureTransport. The goal here is to provide the low-level API to
SecureTransport. These are essentially the C-level functions and constants, and
they're pretty gross to work with.

This code is a bastardised version of the code found in Will Bond's oscrypto
library. An enormous debt is owed to him for blazing this trail for us. For
that reason, this code should be considered to be covered both by urllib3's
license and by oscrypto's:

    Copyright (c) 2015-2016 Will Bond <will@wbond.net>

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.

Loads a CDLL by name, falling back to known path on 10.16+

    A class object that acts as essentially a namespace for CoreFoundation
    constants.
    

    A class object that acts as essentially a namespace for Security constants.
    

---



---

Utilities for writing code that runs on Python 2 and 3
Add documentation to a function.
Import module, returning the module after the last dot.

    A meta path importer to import six.moves and its submodules.

    This class implements a PEP302 finder and loader. It should be compatible
    with Python 2.5 and all existing versions of Python3
    

        Return true, if the named module is a package.

        We need this method to get correct spec objects with
        Python 3.4 (see PEP451)
        
Return None

        Required, if is_package is implemented
Lazy loading of moved objects
Lazy loading of moved objects in six.moves.urllib_parse
Lazy loading of moved objects in six.moves.urllib_error
Lazy loading of moved objects in six.moves.urllib_request
Lazy loading of moved objects in six.moves.urllib_response
Lazy loading of moved objects in six.moves.urllib_robotparser
Create a six.moves.urllib namespace that resembles the Python 3 namespace
Add an item to six.moves.
Remove item from six.moves.
Get the function out of a possibly unbound function
Byte literal
Text literal
Execute code in a namespace.
exec _code_ in _globs_, _locs_
def reraise(tp, value, tb=None):
    try:
        raise tp, value, tb
    finally:
        tb = None

def raise_from(value, from_value):
    try:
        raise value from from_value
    finally:
        value = None

The new-style print function for Python 2.4 and 2.5.
Reraise an exception.
Create a base class with a metaclass.
Class decorator for creating a class with a metaclass.
Coerce **s** to six.binary_type.

    For Python 2:
      - `unicode` -> encoded to `str`
      - `str` -> `str`

    For Python 3:
      - `str` -> encoded to `bytes`
      - `bytes` -> `bytes`
    
Coerce *s* to `str`.

    For Python 2:
      - `unicode` -> encoded to `str`
      - `str` -> `str`

    For Python 3:
      - `str` -> `str`
      - `bytes` -> decoded to `str`
    
Coerce *s* to six.text_type.

    For Python 2:
      - `unicode` -> `unicode`
      - `str` -> `unicode`

    For Python 3:
      - `str` -> `str`
      - `bytes` -> decoded to `str`
    

    A class decorator that defines __unicode__ and __str__ methods under Python 2.
    Under Python 3 it does nothing.

    To support Python 2 and 3 with a single code base, define a __str__ method
    returning text and apply this decorator to the class.
    

---


backports.weakref_finalize
~~~~~~~~~~~~~~~~~~

Backports the Python 3 ``weakref.finalize`` method.

Class for finalization of weakrefable objects
    finalize(obj, func, *args, **kwargs) returns a callable finalizer
    object which will be called when obj is garbage collected. The
    first time the finalizer is called it evaluates func(*arg, **kwargs)
    and returns the result. After this the finalizer is dead, and
    calling it just returns None.
    When the program exits any remaining finalizers for which the
    atexit attribute is true will be run in reverse order of creation.
    By default atexit is true.
    
If alive then mark as dead and return func(*args, **kwargs);
        otherwise return None
If alive then mark as dead and return (obj, func, args, kwargs);
        otherwise return None
If alive then return (obj, func, args, kwargs);
        otherwise return None
Whether finalizer is alive
Whether finalizer should be called at exit

---



---


backports.makefile
~~~~~~~~~~~~~~~~~~

Backports the Python 3 ``socket.makefile`` method for use with anything that
wants to create a "fake" socket object.


    Backport of ``socket.makefile`` from Python 3.5.
    

---

The match_hostname() function from Python 3.3.3, essential when using SSL.
Matching according to RFC 6125, section 6.4.3

    http://tools.ietf.org/html/rfc6125#section-6.4.3
    
Exact matching of IP addresses.

    RFC 6125 explicitly doesn't define an algorithm for this
    (section 1.7.2 - "Out of Scope").
    
Verify that *cert* (in decoded format as returned by
    SSLSocket.getpeercert()) matches the *hostname*.  RFC 2818 and RFC 6125
    rules are followed, but IP addresses are not accepted for *hostname*.

    CertificateError is raised on failure. On success, the function
    returns nothing.
    

---


    Returns True if the connection is dropped and should be closed.

    :param conn:
        :class:`http.client.HTTPConnection` object.

    Note: For platforms like AppEngine, this will always return ``False`` to
    let the platform handle connection recycling transparently for us.
    
Connect to *address* and return the socket object.

    Convenience function.  Connect to *address* (a 2-tuple ``(host,
    port)``) and return the socket object.  Passing the optional
    *timeout* parameter will set the timeout on the socket instance
    before attempting to connect.  If no *timeout* is supplied, the
    global default timeout setting returned by :func:`socket.getdefaulttimeout`
    is used.  If *source_address* is set it must be a tuple of (host, port)
    for the socket to bind as a source address before making the connection.
    An host of '' or port 0 tells the OS to use the default.
    
This function is designed to work in the context of
    getaddrinfo, where family=socket.AF_UNSPEC is the default and
    will perform a DNS search for both IPv6 and IPv4 records.
Returns True if the system can bind an IPv6 address.

---

Timeout configuration.

    Timeouts can be defined as a default for a pool:

    .. code-block:: python

       timeout = Timeout(connect=2.0, read=7.0)
       http = PoolManager(timeout=timeout)
       response = http.request('GET', 'http://example.com/')

    Or per-request (which overrides the default for the pool):

    .. code-block:: python

       response = http.request('GET', 'http://example.com/', timeout=Timeout(10))

    Timeouts can be disabled by setting all the parameters to ``None``:

    .. code-block:: python

       no_timeout = Timeout(connect=None, read=None)
       response = http.request('GET', 'http://example.com/, timeout=no_timeout)


    :param total:
        This combines the connect and read timeouts into one; the read timeout
        will be set to the time leftover from the connect attempt. In the
        event that both a connect timeout and a total are specified, or a read
        timeout and a total are specified, the shorter timeout will be applied.

        Defaults to None.

    :type total: int, float, or None

    :param connect:
        The maximum amount of time (in seconds) to wait for a connection
        attempt to a server to succeed. Omitting the parameter will default the
        connect timeout to the system default, probably `the global default
        timeout in socket.py
        <http://hg.python.org/cpython/file/603b4d593758/Lib/socket.py#l535>`_.
        None will set an infinite timeout for connection attempts.

    :type connect: int, float, or None

    :param read:
        The maximum amount of time (in seconds) to wait between consecutive
        read operations for a response from the server. Omitting the parameter
        will default the read timeout to the system default, probably `the
        global default timeout in socket.py
        <http://hg.python.org/cpython/file/603b4d593758/Lib/socket.py#l535>`_.
        None will set an infinite timeout.

    :type read: int, float, or None

    .. note::

        Many factors can affect the total amount of time for urllib3 to return
        an HTTP response.

        For example, Python's DNS resolver does not obey the timeout specified
        on the socket. Other factors that can affect total request time include
        high CPU load, high swap, the program running at a low priority level,
        or other behaviors.

        In addition, the read and total timeouts only measure the time between
        read operations on the socket connecting the client and the server,
        not the total amount of time for the request to return a complete
        response. For most requests, the timeout is raised because the server
        has not sent the first byte in the specified time. This is not always
        the case; if a server streams one byte every fifteen seconds, a timeout
        of 20 seconds will not trigger, even though the request will take
        several minutes to complete.

        If your goal is to cut off any request after a set amount of wall clock
        time, consider having a second "watcher" thread to cut off a slow
        request.
    
Check that a timeout attribute is valid.

        :param value: The timeout value to validate
        :param name: The name of the timeout attribute to validate. This is
            used to specify in error messages.
        :return: The validated and casted version of the given value.
        :raises ValueError: If it is a numeric value less than or equal to
            zero, or the type is not an integer, float, or None.
        
Create a new Timeout from a legacy timeout value.

        The timeout value used by httplib.py sets the same timeout on the
        connect(), and recv() socket requests. This creates a :class:`Timeout`
        object that sets the individual timeouts to the ``timeout`` value
        passed to this function.

        :param timeout: The legacy timeout value.
        :type timeout: integer, float, sentinel default object, or None
        :return: Timeout object
        :rtype: :class:`Timeout`
        
Create a copy of the timeout object

        Timeout properties are stored per-pool but each request needs a fresh
        Timeout object to ensure each one has its own start/stop configured.

        :return: a copy of the timeout object
        :rtype: :class:`Timeout`
        
Start the timeout clock, used during a connect() attempt

        :raises urllib3.exceptions.TimeoutStateError: if you attempt
            to start a timer that has been started already.
        
Gets the time elapsed since the call to :meth:`start_connect`.

        :return: Elapsed time in seconds.
        :rtype: float
        :raises urllib3.exceptions.TimeoutStateError: if you attempt
            to get duration for a timer that hasn't been started.
        
Get the value to use when setting a connection timeout.

        This will be a positive float or integer, the value None
        (never timeout), or the default system timeout.

        :return: Connect timeout.
        :rtype: int, float, :attr:`Timeout.DEFAULT_TIMEOUT` or None
        
Get the value for the read timeout.

        This assumes some time has elapsed in the connection timeout and
        computes the read timeout appropriately.

        If self.total is set, the read timeout is dependent on the amount of
        time taken by the connect timeout. If the connection time has not been
        established, a :exc:`~urllib3.exceptions.TimeoutStateError` will be
        raised.

        :return: Value to use for the read timeout.
        :rtype: int, float, :attr:`Timeout.DEFAULT_TIMEOUT` or None
        :raises urllib3.exceptions.TimeoutStateError: If :meth:`start_connect`
            has not yet been called on this object.
        

---


    Checks whether a given file-like object is closed.

    :param obj:
        The file-like object to check.
    

    Asserts whether all headers have been successfully parsed.
    Extracts encountered errors from the result of parsing headers.

    Only works on Python 3.

    :param http.client.HTTPMessage headers: Headers to verify.

    :raises urllib3.exceptions.HeaderParsingError:
        If parsing errors are found.
    

    Checks whether the request of a response has been a HEAD-request.
    Handles the quirks of AppEngine.

    :param http.client.HTTPResponse response:
        Response to check if the originating request
        used 'HEAD' as a method.
    

---


    Returns True if the connection requires an HTTP CONNECT through the proxy.

    :param URL proxy_url:
        URL of the proxy.
    :param ProxyConfig proxy_config:
        Proxy configuration from poolmanager.py
    :param str destination_scheme:
        The scheme of the destination. (i.e https, http, etc)
    

    Generates a default proxy ssl context if one hasn't been provided by the
    user.
    

---


    Data structure for representing an HTTP URL. Used as a return value for
    :func:`parse_url`. Both the scheme and host are normalized as they are
    both case-insensitive according to RFC 3986.
    
For backwards-compatibility with urlparse. We're nice like that.
Absolute path including the query string.
Network location including host and port

        Convert self into a url

        This function should more or less round-trip with :func:`.parse_url`. The
        returned url may not be exactly the same as the url inputted to
        :func:`.parse_url`, but it should be equivalent by the RFC (e.g., urls
        with a blank port will have : removed).

        Example: ::

            >>> U = parse_url('http://google.com/mail/')
            >>> U.url
            'http://google.com/mail/'
            >>> Url('http', 'username:password', 'host.com', 80,
            ... '/path', 'query', 'fragment').url
            'http://username:password@host.com:80/path?query#fragment'
        

    .. deprecated:: 1.25

    Given a string and an iterable of delimiters, split on the first found
    delimiter. Return two split parts and the matched delimiter.

    If not found, then the first part is the full input string.

    Example::

        >>> split_first('foo/bar?baz', '?/=')
        ('foo', 'bar?baz', '/')
        >>> split_first('foo/bar?baz', '123')
        ('foo/bar?baz', '', None)

    Scales linearly with number of delims. Not ideal for large number of delims.
    
Percent-encodes a URI component without reapplying
    onto an already percent-encoded component.
    
Percent-encodes a request target so that there are no invalid characters

    Given a url, return a parsed :class:`.Url` namedtuple. Best-effort is
    performed to parse incomplete urls. Fields not provided will be None.
    This parser is RFC 3986 and RFC 6874 compliant.

    The parser logic and helper functions are based heavily on
    work done in the ``rfc3986`` module.

    :param str url: URL to parse into a :class:`.Url` namedtuple.

    Partly backwards-compatible with :mod:`urlparse`.

    Example::

        >>> parse_url('http://google.com/mail/')
        Url(scheme='http', host='google.com', port=None, path='/mail/', ...)
        >>> parse_url('google.com:80')
        Url(scheme=None, host='google.com', port=80, path=None, ...)
        >>> parse_url('/foo?bar')
        Url(scheme=None, host=None, port=None, path='/foo', query='bar', ...)
    

    Deprecated. Use :func:`parse_url` instead.
    

---


    The SSLTransport wraps an existing socket and establishes an SSL connection.

    Contrary to Python's implementation of SSLSocket, it allows you to chain
    multiple TLS connections together. It's particularly useful if you need to
    implement TLS within TLS.

    The class supports most of the socket API operations.
    

        Raises a ProxySchemeUnsupported if the provided ssl_context can't be used
        for TLS in TLS.

        The only requirement is that the ssl_context provides the 'wrap_bio'
        methods.
        

        Create an SSLTransport around socket using the provided ssl_context.
        

        Python's httpclient uses makefile and buffered io when reading HTTP
        messages and we need to support it.

        This is unfortunately a copy and paste of socket.py makefile with small
        changes to point to the socket directly.
        
Performs an I/O loop between incoming/outgoing and the socket.

---

Waits for reading to be available on a given socket.
    Returns True if the socket is readable, or False if the timeout expired.
    
Waits for writing to be available on a given socket.
    Returns True if the socket is readable, or False if the timeout expired.
    

---



---

Retry configuration.

    Each retry attempt will create a new Retry object with updated values, so
    they can be safely reused.

    Retries can be defined as a default for a pool::

        retries = Retry(connect=5, read=2, redirect=5)
        http = PoolManager(retries=retries)
        response = http.request('GET', 'http://example.com/')

    Or per-request (which overrides the default for the pool)::

        response = http.request('GET', 'http://example.com/', retries=Retry(10))

    Retries can be disabled by passing ``False``::

        response = http.request('GET', 'http://example.com/', retries=False)

    Errors will be wrapped in :class:`~urllib3.exceptions.MaxRetryError` unless
    retries are disabled, in which case the causing exception will be raised.

    :param int total:
        Total number of retries to allow. Takes precedence over other counts.

        Set to ``None`` to remove this constraint and fall back on other
        counts.

        Set to ``0`` to fail on the first retry.

        Set to ``False`` to disable and imply ``raise_on_redirect=False``.

    :param int connect:
        How many connection-related errors to retry on.

        These are errors raised before the request is sent to the remote server,
        which we assume has not triggered the server to process the request.

        Set to ``0`` to fail on the first retry of this type.

    :param int read:
        How many times to retry on read errors.

        These errors are raised after the request was sent to the server, so the
        request may have side-effects.

        Set to ``0`` to fail on the first retry of this type.

    :param int redirect:
        How many redirects to perform. Limit this to avoid infinite redirect
        loops.

        A redirect is a HTTP response with a status code 301, 302, 303, 307 or
        308.

        Set to ``0`` to fail on the first retry of this type.

        Set to ``False`` to disable and imply ``raise_on_redirect=False``.

    :param int status:
        How many times to retry on bad status codes.

        These are retries made on responses, where status code matches
        ``status_forcelist``.

        Set to ``0`` to fail on the first retry of this type.

    :param int other:
        How many times to retry on other errors.

        Other errors are errors that are not connect, read, redirect or status errors.
        These errors might be raised after the request was sent to the server, so the
        request might have side-effects.

        Set to ``0`` to fail on the first retry of this type.

        If ``total`` is not set, it's a good idea to set this to 0 to account
        for unexpected edge cases and avoid infinite retry loops.

    :param iterable allowed_methods:
        Set of uppercased HTTP method verbs that we should retry on.

        By default, we only retry on methods which are considered to be
        idempotent (multiple requests with the same parameters end with the
        same state). See :attr:`Retry.DEFAULT_ALLOWED_METHODS`.

        Set to a ``False`` value to retry on any verb.

        .. warning::

            Previously this parameter was named ``method_whitelist``, that
            usage is deprecated in v1.26.0 and will be removed in v2.0.

    :param iterable status_forcelist:
        A set of integer HTTP status codes that we should force a retry on.
        A retry is initiated if the request method is in ``allowed_methods``
        and the response status code is in ``status_forcelist``.

        By default, this is disabled with ``None``.

    :param float backoff_factor:
        A backoff factor to apply between attempts after the second try
        (most errors are resolved immediately by a second try without a
        delay). urllib3 will sleep for::

            {backoff factor} * (2 ** ({number of total retries} - 1))

        seconds. If the backoff_factor is 0.1, then :func:`.sleep` will sleep
        for [0.0s, 0.2s, 0.4s, ...] between retries. It will never be longer
        than :attr:`Retry.DEFAULT_BACKOFF_MAX`.

        By default, backoff is disabled (set to 0).

    :param bool raise_on_redirect: Whether, if the number of redirects is
        exhausted, to raise a MaxRetryError, or to return a response with a
        response code in the 3xx range.

    :param bool raise_on_status: Similar meaning to ``raise_on_redirect``:
        whether we should raise an exception, or return a response,
        if status falls in ``status_forcelist`` range and retries have
        been exhausted.

    :param tuple history: The history of the request encountered during
        each call to :meth:`~Retry.increment`. The list is in the order
        the requests occurred. Each list item is of class :class:`RequestHistory`.

    :param bool respect_retry_after_header:
        Whether to respect Retry-After header on status codes defined as
        :attr:`Retry.RETRY_AFTER_STATUS_CODES` or not.

    :param iterable remove_headers_on_redirect:
        Sequence of headers to remove from the request when a response
        indicating a redirect is returned before firing off the redirected
        request.
    
Backwards-compatibility for the old retries format.
Formula for computing the current backoff

        :rtype: float
        
Get the value of Retry-After in seconds.
Sleep between retry attempts.

        This method will respect a server's ``Retry-After`` response header
        and sleep the duration of the time requested. If that is not present, it
        will use an exponential backoff. By default, the backoff factor is 0 and
        this method will return immediately.
        
Errors when we're fairly sure that the server did not receive the
        request, so it should be safe to retry.
        
Errors that occur after the request has been started, so we should
        assume that the server began processing it.
        
Checks if a given HTTP method should be retried upon, depending if
        it is included in the allowed_methods
        
Is this method/status code retryable? (Based on allowlists and control
        variables such as the number of total retries to allow, whether to
        respect the Retry-After header, whether this header is present, and
        whether the returned status code is on the list of status codes to
        be retried upon on the presence of the aforementioned header)
        
Are we out of retries?
Return a new Retry object with incremented retry counters.

        :param response: A response object, or None, if the server did not
            return a response.
        :type response: :class:`~urllib3.response.HTTPResponse`
        :param Exception error: An error encountered during the request, or
            None if the response was received successfully.

        :return: A new ``Retry`` object.
        

---



---


    Shortcuts for generating request headers.

    :param keep_alive:
        If ``True``, adds 'connection: keep-alive' header.

    :param accept_encoding:
        Can be a boolean, list, or string.
        ``True`` translates to 'gzip,deflate'.
        List will get joined by comma.
        String will be used as provided.

    :param user_agent:
        String representing the user-agent you want, such as
        "python-urllib3/0.6"

    :param basic_auth:
        Colon-separated username:password string for 'authorization: basic ...'
        auth header.

    :param proxy_basic_auth:
        Colon-separated username:password string for 'proxy-authorization: basic ...'
        auth header.

    :param disable_cache:
        If ``True``, adds 'cache-control: no-cache' header.

    Example::

        >>> make_headers(keep_alive=True, user_agent="Batman/1.0")
        {'connection': 'keep-alive', 'user-agent': 'Batman/1.0'}
        >>> make_headers(accept_encoding=True)
        {'accept-encoding': 'gzip,deflate'}
    

    If a position is provided, move file to that point.
    Otherwise, we'll attempt to record a position for future use.
    

    Attempt to rewind body to a certain position.
    Primarily used for request redirects and retries.

    :param body:
        File-like object that supports seek.

    :param int pos:
        Position to seek to in file.
    

---


    Compare two digests of equal length in constant time.

    The digests must be of type str/bytes.
    Returns True if the digests match, and False otherwise.
    

    Checks if given fingerprint matches the supplied certificate.

    :param cert:
        Certificate as bytes object.
    :param fingerprint:
        Fingerprint as string of hexdigits, can be interspersed by colons.
    

    Resolves the argument to a numeric constant, which can be passed to
    the wrap_socket function/method from the ssl module.
    Defaults to :data:`ssl.CERT_REQUIRED`.
    If given a string it is assumed to be the name of the constant in the
    :mod:`ssl` module or its abbreviation.
    (So you can specify `REQUIRED` instead of `CERT_REQUIRED`.
    If it's neither `None` nor a string we assume it is already the numeric
    constant which can directly be passed to wrap_socket.
    

    like resolve_cert_reqs
    
All arguments have the same meaning as ``ssl_wrap_socket``.

    By default, this function does a lot of the same work that
    ``ssl.create_default_context`` does on Python 3.4+. It:

    - Disables SSLv2, SSLv3, and compression
    - Sets a restricted set of server ciphers

    If you wish to enable SSLv3, you can do::

        from pip._vendor.urllib3.util import ssl_
        context = ssl_.create_urllib3_context()
        context.options &= ~ssl_.OP_NO_SSLv3

    You can do the same to enable compression (substituting ``COMPRESSION``
    for ``SSLv3`` in the last line above).

    :param ssl_version:
        The desired protocol version to use. This will default to
        PROTOCOL_SSLv23 which will negotiate the highest protocol that both
        the server and your installation of OpenSSL support.
    :param cert_reqs:
        Whether to require the certificate verification. This defaults to
        ``ssl.CERT_REQUIRED``.
    :param options:
        Specific OpenSSL options. These default to ``ssl.OP_NO_SSLv2``,
        ``ssl.OP_NO_SSLv3``, ``ssl.OP_NO_COMPRESSION``, and ``ssl.OP_NO_TICKET``.
    :param ciphers:
        Which cipher suites to allow the server to select.
    :returns:
        Constructed SSLContext object with specified options
    :rtype: SSLContext
    

    All arguments except for server_hostname, ssl_context, and ca_cert_dir have
    the same meaning as they do when using :func:`ssl.wrap_socket`.

    :param server_hostname:
        When SNI is supported, the expected hostname of the certificate
    :param ssl_context:
        A pre-made :class:`SSLContext` object. If none is provided, one will
        be created using :func:`create_urllib3_context`.
    :param ciphers:
        A string of ciphers we wish the client to support.
    :param ca_cert_dir:
        A directory containing CA certificates in multiple separate files, as
        supported by OpenSSL's -CApath flag or the capath argument to
        SSLContext.load_verify_locations().
    :param key_password:
        Optional password if the keyfile is encrypted.
    :param ca_cert_data:
        Optional string containing CA certificates in PEM format suitable for
        passing as the cadata parameter to SSLContext.load_verify_locations()
    :param tls_in_tls:
        Use SSLTransport to wrap the existing socket.
    
Detects whether the hostname given is an IPv4 or IPv6 address.
    Also detects IPv6 addresses with Zone IDs.

    :param str hostname: Hostname to examine.
    :return: True if the hostname is an IP address, False otherwise.
    
Detects if a key file is encrypted or not.

---


0
(?:
    x[0-9A-Fa-f](?:_?[0-9A-Fa-f])*   # hex
    |
    b[01](?:_?[01])*                 # bin
    |
    o[0-7](?:_?[0-7])*               # oct
)
|
[+-]?(?:0|[1-9](?:_?[0-9])*)         # dec, integer part
(?P<floatpart>
    (?:\.[0-9](?:_?[0-9])*)?         # optional fractional part
    (?:[eE][+-]?[0-9](?:_?[0-9])*)?  # optional exponent part
)


([0-9]{{4}})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])  # date, e.g. 1988-10-27
(?:
    [Tt ]
    {_TIME_RE_STR}
    (?:([Zz])|([+-])([01][0-9]|2[0-3]):([0-5][0-9]))?  # optional time offset
)?

Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    

---

Sentinel to be used as default arg during deprecation
    period of TOMLDecodeError's free-form arguments.
An error raised if a document is not valid TOML.

    Adds the following attributes to ValueError:
    msg: The unformatted error message
    doc: The TOML document being parsed
    pos: The index of doc where parsing failed
    lineno: The line corresponding to pos
    colno: The column corresponding to pos
    
Parse TOML from a binary file object.
Parse TOML from a string.
Flags that map to parsed keys/namespaces.
', pos):
                return pos + 3, result + src[start_pos:pos]
            pos += 1
            continue
        if char == "\\":
            result += src[start_pos:pos]
            pos, parsed_escape = parse_escapes(src, pos)
            result += parsed_escape
            start_pos = pos
            continue
        if char in error_on:
            raise TOMLDecodeError(f"Illegal character {char!r}", src, pos)
        pos += 1


def parse_value(  # noqa: C901
    src: str, pos: Pos, parse_float: ParseFloat, nest_lvl: int
) -> tuple[Pos, Any]:
    if nest_lvl > MAX_INLINE_NESTING:
        # Pure Python should have raised RecursionError already.
        # This ensures mypyc binaries eventually do the same.
        raise RecursionError(  # pragma: no cover
            "TOML inline arrays/tables are nested more than the allowed"
            f" {MAX_INLINE_NESTING} levels"
        )

    try:
        char: str | None = src[pos]
    except IndexError:
        char = None

    # IMPORTANT: order conditions based on speed of checking and likelihood

    # Basic strings
    if char == '"':
        if src.startswith('
A decorator to make `parse_float` safe.

    `parse_float` must not return dicts or lists, because these types
    would be mixed with parsed TOML tables and arrays, thus confusing
    the parser. The returned decorated callable raises `ValueError`
    instead of returning illegal types.
    

---



---



---

Exceptions used throughout package.

This module MUST NOT try to import from anything within `pip._internal` to
operate. This is expected to be importable from any/all files within the
subpackage and, thus, should not depend on them.

The base pip error.
An error, that presents diagnostic information to the user.

    This contains a bunch of logic, to enable pretty presentation of our error
    messages. Each error gets a unique reference. Each error can also include
    additional context, a hint and/or a note -- which are presented with the
    main error message in a consistent style.

    This is adapted from the error output styling in `sphinx-theme-builder`.
    
General exception in configuration
General exception during installation
Raised when pyproject.toml has `build-system`, but no `build-system.requires`.
Raised when pyproject.toml an invalid `build-system.requires`.
Raised when accessing a Distribution's "METADATA" or "PKG-INFO".

    This signifies an inconsistency, when the Distribution claims to have
    the metadata file (if not, raise ``FileNotFoundError`` instead), but is
    not actually able to produce its content. This may be due to permission
    errors.
    

        :param dist: A Distribution object.
        :param metadata_name: The name of the metadata being accessed
            (can be "METADATA" or "PKG-INFO").
        
A --user install is requested on an environment without user site.
Raised when a distribution cannot be found to satisfy a requirement
Raised when a general error occurs parsing a requirements file line.
Raised when the most up-to-date version of a package is already
    installed.
Raised when virtualenv or a command is not found
Raised when there is an error in command-line arguments
Raised when there's a previous conflicting build directory
HTTP connection error

        Initialize NetworkConnectionError with  `request` and `response`
        objects.
        
Invalid wheel filename.
Unsupported wheel.
Invalid (e.g. corrupt) wheel.
Built metadata contains inconsistent information.

    This is raised when the metadata contains values (e.g. name and version)
    that do not match the information previously obtained from sdist filename,
    user-supplied ``#egg=`` value, or an install requirement name.
    
Metadata is invalid.
A subprocess call failed.
Multiple HashError instances rolled into one for reporting

    A failure to verify a package against known-good hashes

    :cvar order: An int sorting hash exception classes by difficulty of
        recovery (lower being harder), so the user doesn't bother fretting
        about unpinned packages when he has deeper issues, like VCS
        dependencies, to deal with. Also keeps error reports in a
        deterministic order.
    :cvar head: A section heading for display above potentially many
        exceptions of this kind
    :ivar req: The InstallRequirement that triggered this error. This is
        pasted on after the exception is instantiated, because it's not
        typically available earlier.

    
Return a summary of me for display under the heading.

        This default implementation simply prints a description of the
        triggering requirement.

        :param req: The InstallRequirement that provoked this error, with
            its link already populated by the resolver's _populate_link().

        
Return a description of the requirement that triggered me.

        This default implementation returns long description of the req, with
        line numbers

        
A hash was provided for a version-control-system-based requirement, but
    we don't have a method for hashing those.
A hash was provided for a version-control-system-based requirement, but
    we don't have a method for hashing those.
A hash was needed for a requirement but is absent.

        :param gotten_hash: The hash of the (possibly malicious) archive we
            just downloaded
        
A requirement had a hash specified but was not pinned to a specific
    version.

    Distribution file hash values don't match.

    :ivar package_name: The name of the package that triggered the hash
        mismatch. Feel free to write to this after the exception is raise to
        improve its error message.

    

        :param allowed: A dict of algorithm names pointing to lists of allowed
            hex digests
        :param gots: A dict of algorithm names pointing to hashes we
            actually got from the files under suspicion
        

        Return a comparison of actual and expected hash values.

        Example::

               Expected sha256 abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde
                            or 123451234512345123451234512345123451234512345
                    Got        bcdefbcdefbcdefbcdefbcdefbcdefbcdefbcdefbcdef

        
Unsupported python version according to Requires-Python package
    metadata.
When there are errors while loading a configuration file
\
The Python environment under {sys.prefix} is managed externally, and may not be
manipulated by the user. Please use specific tooling from the distributor of
the Python installation to interact with this environment instead.

The current environment is externally managed.

    This is raised when the current environment is externally managed, as
    defined by `PEP 668`_. The ``EXTERNALLY-MANAGED`` configuration is checked
    and displayed when the error is bubbled up to the user.

    :param error: The error message read from ``EXTERNALLY-MANAGED``.
    
Raised when the downloader receives fewer bytes than advertised
    in the Content-Length header.
Raised when the dependency resolver exceeds the maximum recursion depth.

---

This is preserved for old console scripts that may still be referencing
    it.

    For additional details, see https://github.com/pypa/pip/issues/7498.
    

---

Orchestrator for building wheels from InstallRequirements.
Determine whether the string looks like an egg_info.

    :param s: The string to parse. E.g. foo-2.1
    
Return whether an InstallRequirement should be built into a wheel.

    Return whether a built InstallRequirement can be stored in the persistent
    wheel cache, assuming the wheel cache is available, and _should_build()
    has determined a wheel needs to be built.
    
Return the persistent or temporary cache directory where the built
    wheel need to be stored.
    
Build one wheel.

    :return: The filename of the built wheel, or None if the build failed.
    
Build wheels.

    :return: The list of InstallRequirement that succeeded to build and
        the list of InstallRequirement that failed to build.
    

---

Load the pyproject.toml file.

    Parameters:
        use_pep517 - Has the user requested PEP 517 processing? None
                     means the user hasn't explicitly specified.
        pyproject_toml - Location of the project's pyproject.toml file
        setup_py - Location of the project's setup.py file
        req_name - The name of the requirement we're processing (for
                   error reporting)

    Returns:
        None if we should use the legacy code path, otherwise a tuple
        (
            requirements from pyproject.toml,
            name of PEP 517 backend,
            requirements we should check are installed after setting
                up the build environment
            directory paths to import the backend from (backend-path),
                relative to the project root.
        )
    

---

Convert an ISO format string to a date.

    Handles the format 2020-01-22T14:24:01Z (trailing Z)
    which is not supported by older versions of fromisoformat.
    
Check if we have a not-outdated version loaded already.
Checks whether pkg was installed by pip

    This is used not to display the upgrade message when pip is in fact
    installed by system package manager, such as dnf on Fedora.
    
Check for an update for pip.

    Limit the frequency of checks to once per week. State is stored either in
    the active virtualenv or in the user's USER_CACHE_DIR keyed off the prefix
    of the pip script path.
    

---

Cache Management
Return a stable sha224 of a dictionary.
An abstract class - provides cache directories for data from links

    :param cache_dir: The root of the cache.
    
Get parts of part that must be os.path.joined with cache_dir
Return a directory to store cached items in for link.
Returns a link to a cached item if it exists, otherwise returns the
        passed link.
        
A cache of wheels for future installs.
Return a directory to store cached wheels for link

        Because there are M wheels for any one sdist, we provide a directory
        to cache them in, and then consult that directory when looking up
        cache hits.

        We only insert things into the cache if they have plausible version
        numbers, so that we don't contaminate the cache with things that were
        not unique. E.g. ./package might have dozens of installs done for it
        and build a version of 0.0...and if we built and cached a wheel, we'd
        end up using the same wheel even if the source has been edited.

        :param link: The link of the sdist for which this will cache wheels.
        
A SimpleWheelCache that creates it's own temporary cache directory
Wraps EphemWheelCache and SimpleWheelCache into a single Cache

    This Cache allows for gracefully degradation, using the ephem wheel cache
    when a certain link is not found in the simple wheel cache first.
    
Returns a CacheEntry with a link to a cached item if it exists or
        None. The cache entry indicates if the item was found in the persistent
        or ephemeral cache.
        

---

This is preserved for old console scripts that may still be referencing
    it.

    For additional details, see https://github.com/pypa/pip/issues/7498.
    

---

Configuration management setup

Some terminology:
- name
  As written in config files.
- value
  Value associated with a name
- key
  Name combined with it's section (section.name)
- variant
  A single word describing where the configuration key-value pair came from

Make a name consistent regardless of source (environment or file)
Handles management of configuration.

    Provides an interface to accessing and managing configuration files.

    This class converts provides an API that takes "section.key-name" style
    keys and stores the value associated with it as "key-name" under the
    section "section".

    This allows for a clean interface wherein the both the section and the
    key-name are preserved in an easy to manage form in the configuration files
    and the data stored is also nice.
    
Loads configuration from configuration files and environment
Returns the file with highest priority in configuration
Returns key-value pairs like dict.items() representing the loaded
        configuration
        
Get a value from the configuration.
Modify a value in the configuration.
Unset a value in the configuration.
Save the current in-memory state.
A dictionary representing the loaded configuration.
Loads configuration from configuration files
Loads configuration from environment variables
Normalizes items to construct a dictionary with normalized keys.

        This routine is where the names become keys and are made the same
        regardless of source - configuration files or environment.
        
Returns a generator with all environmental vars with prefix PIP_
Yields variant and configuration files associated with it.

        This should be treated like items of a dictionary. The order
        here doesn't affect what gets overridden. That is controlled
        by OVERRIDE_ORDER. However this does control the order they are
        displayed to the user. It's probably most ergonomic to display
        things in the same order as OVERRIDE_ORDER
        
Get values present in a config file

---

Build Environment used for isolation during sdist building
Get a file to pass to a Python executable, to run the currently-running pip.

    This is used to run a pip subprocess, for installing requirements into the build
    environment.
    
Get system site packages

    Usually from site.getsitepackages,
    but fallback on `get_purelib()/get_platlib()` if unavailable
    (e.g. in a virtualenv created by virtualenv<20)

    Returns normalized set of strings.
    
Creates and manages an isolated environment to install build deps

                import os, site, sys

                # First, drop system-sites related paths.
                original_sys_path = sys.path[:]
                known_paths = set()
                for path in {system_sites!r}:
                    site.addsitedir(path, known_paths=known_paths)
                system_paths = set(
                    os.path.normcase(path)
                    for path in sys.path[len(original_sys_path):]
                )
                original_sys_path = [
                    path for path in original_sys_path
                    if os.path.normcase(path) not in system_paths
                ]
                sys.path = original_sys_path

                # Second, add lib directories.
                # ensuring .pth file are processed.
                for path in {lib_dirs!r}:
                    assert not path in sys.path
                    site.addsitedir(path)
                
Return 2 sets:
        - conflicting requirements: set of (installed, wanted) reqs tuples
        - missing requirements: set of reqs
        
A no-op drop-in replacement for BuildEnvironment

---


    Show information about one or more installed packages.

    The output is in RFC-compliant mail header format.
    

      %prog [options] <package> ...

    Gather details from installed distributions. Print distribution name,
    version, location, and installed files. Installed files requires a
    pip generated 'installed-files.txt' in the distributions '.egg-info'
    directory.
    

    Print the information from installed distributions found.
    

---

Verify installed packages have compatible dependencies.

      %prog [options]

---


    Inspect the content of a Python environment and produce a report in JSON format.
    

      %prog [options]

---


    Download packages from:

    - PyPI (and other indexes) using requirement specifiers.
    - VCS project urls.
    - Local project directories.
    - Local or remote source archives.

    pip also supports downloading from "requirements files", which provide
    an easy way to specify a whole environment to be downloaded.
    

      %prog [options] <requirement specifier> [package-index-options] ...
      %prog [options] -r <requirements file> [package-index-options] ...
      %prog [options] <vcs project url> ...
      %prog [options] <local project path> ...
      %prog [options] <archive url/path> ...

---


    Uninstall packages.

    pip is able to uninstall most installed packages. Known exceptions are:

    - Pure distutils packages installed with ``python setup.py install``, which
      leave behind no metadata to determine what files were installed.
    - Script wrappers installed by ``python setup.py develop``.
    

      %prog [options] <package> ...
      %prog [options] -r <requirements file> ...

---

Give the distribution object a couple of extra fields.

        These will be populated during ``get_outdated()``. This is dirty but
        makes the rest of the code much cleaner.
        

    List installed packages, including editables.

    Packages are listed in a case-insensitive sorted order.
    

      %prog [options]

        Create a package finder appropriate to this list command.
        

    Convert the package data into something usable
    by output_package_listing_columns.
    

---


    Inspect information available from package indexes.
    

        %prog versions <package>
    

        Create a package finder appropriate to the index command.
        

---


# pip {shell} completion start{script}# pip {shell} completion end


        _pip_completion()
        {{
            COMPREPLY=( $( COMP_WORDS="${{COMP_WORDS[*]}}" \\
                           COMP_CWORD=$COMP_CWORD \\
                           PIP_AUTO_COMPLETE=1 $1 2>/dev/null ) )
        }}
        complete -o default -F _pip_completion {prog}
    

        #compdef -P pip[0-9.]#
        __pip() {{
          compadd $( COMP_WORDS="$words[*]" \\
                     COMP_CWORD=$((CURRENT-1)) \\
                     PIP_AUTO_COMPLETE=1 $words[1] 2>/dev/null )
        }}
        if [[ $zsh_eval_context[-1] == loadautofunc ]]; then
          # autoload from fpath, call function directly
          __pip "$@"
        else
          # eval/source/. command, register function for later
          compdef __pip -P 'pip[0-9.]#'
        fi
    

        function __fish_complete_pip
            set -lx COMP_WORDS \\
                (commandline --current-process --tokenize --cut-at-cursor) \\
                (commandline --current-token --cut-at-cursor)
            set -lx COMP_CWORD (math (count $COMP_WORDS) - 1)
            set -lx PIP_AUTO_COMPLETE 1
            set -l completions
            if string match -q '2.*' $version
                set completions (eval $COMP_WORDS[1])
            else
                set completions ($COMP_WORDS[1])
            end
            string split \\  -- $completions
        end
        complete -fa "(__fish_complete_pip)" -c {prog}
    

        if ((Test-Path Function:\\TabExpansion) -and -not `
            (Test-Path Function:\\_pip_completeBackup)) {{
            Rename-Item Function:\\TabExpansion _pip_completeBackup
        }}
        function TabExpansion($line, $lastWord) {{
            $lastBlock = [regex]::Split($line, '[|;]')[-1].TrimStart()
            if ($lastBlock.StartsWith("{prog} ")) {{
                $Env:COMP_WORDS=$lastBlock
                $Env:COMP_CWORD=$lastBlock.Split().Length - 1
                $Env:PIP_AUTO_COMPLETE=1
                (& {prog}).Split()
                Remove-Item Env:COMP_WORDS
                Remove-Item Env:COMP_CWORD
                Remove-Item Env:PIP_AUTO_COMPLETE
            }}
            elseif (Test-Path Function:\\_pip_completeBackup) {{
                # Fall back on existing tab expansion
                _pip_completeBackup $line $lastWord
            }}
        }}
    
A helper command to be used for command completion.
Prints the completion code of the given shell

---

Log the actual version and print extra info if there is
    a conflict or if the actual version could not be imported.
    

    Display debug information.
    

      %prog <options>

---

Search for PyPI packages whose name or summary contains <query>.

      %prog [options] <query>

    The list from pypi is really a list of versions. We want a list of
    packages with the list of versions stored inline. This converts the
    list from pypi into one we can use.
    

---


    Build Wheel archives for your requirements and dependencies.

    Wheel is a built-package format, and offers the advantage of not
    recompiling your software during every install. For more details, see the
    wheel docs: https://wheel.readthedocs.io/en/latest/

    'pip wheel' uses the build system interface as described here:
    https://pip.pypa.io/en/stable/reference/build-system/

    

      %prog [options] <requirement specifier> ...
      %prog [options] -r <requirements file> ...
      %prog [options] [-e] <vcs project url> ...
      %prog [options] [-e] <local project path> ...
      %prog [options] <archive url/path> ...

---


    Inspect and manage pip's wheel cache.

    Subcommands:

    - dir: Show the cache directory.
    - info: Show information about the cache.
    - list: List filenames of packages stored in the cache.
    - remove: Remove one or more package from the cache.
    - purge: Remove all items from the cache.

    ``<pattern>`` can be a glob expression or a package name.
    

        %prog dir
        %prog info
        %prog list [<pattern>] [--format=[human, abspath]]
        %prog remove <pattern>
        %prog purge
    

                    Package index page cache location (pip v23.3+): {http_cache_location}
                    Package index page cache location (older pips): {old_http_cache_location}
                    Package index page cache size: {http_cache_size}
                    Number of HTTP files: {num_http_files}
                    Locally built wheels location: {wheels_cache_location}
                    Locally built wheels size: {wheels_cache_size}
                    Number of locally built wheels: {package_count}
                

---


Package containing all pip commands


    Create an instance of the Command class with the given name.
    
Command name auto-correct.

---


    Manage local and global configuration.

    Subcommands:

    - list: List the active configuration (or from the file specified)
    - edit: Edit the configuration file in an editor
    - get: Get the value associated with command.option
    - set: Set the command.option=value
    - unset: Unset the value associated with command.option
    - debug: List the configuration files and values defined under them

    Configuration keys should be dot separated command and option name,
    with the special prefix "global" affecting any command. For example,
    "pip config set global.index-url https://example.org/" would configure
    the index url for all commands, but "pip config set download.timeout 10"
    would configure a 10 second timeout only for "pip download" commands.

    If none of --user, --global and --site are passed, a virtual
    environment configuration file is used if one is active and the file
    exists. Otherwise, all modifications happen to the user file by
    default.
    

        %prog [<file-option>] list
        %prog [<file-option>] [--editor <editor-path>] edit

        %prog [<file-option>] get command.option
        %prog [<file-option>] set command.option value
        %prog [<file-option>] unset command.option
        %prog [<file-option>] debug
    
List config key-value pairs across different config files
Get key-value pairs from the file of a variant
Get key-values pairs present as environment variables
Helper to make sure the command got the right number of arguments

---


    Install packages from:

    - PyPI (and other indexes) using requirement specifiers.
    - VCS project urls.
    - Local project directories.
    - Local or remote source archives.

    pip also supports installing from "requirements files", which provide
    an easy way to specify a whole environment to be installed.
    

      %prog [options] <requirement specifier> [package-index-options] ...
      %prog [options] -r <requirements file> [package-index-options] ...
      %prog [options] [-e] <vcs project url> ...
      %prog [options] [-e] <local project path> ...
      %prog [options] <archive url/path> ...
Determine whether to do a user install based on the input options.

    If use_user_site is False, no additional checks are done.
    If use_user_site is True, it is checked for compatibility with other
    options.
    If use_user_site is None, the default behaviour depends on the environment,
    which is provided by the other arguments.
    
Format an error message for an OSError

    It may occur anytime during the execution of the install command.
    

---

Show help for commands

      %prog <command>

---


    Compute a hash of a local package archive.

    These can be used with --hash in a requirements file to do repeatable
    installs.
    
Return the hash digest of a file.

---


    Output installed packages in requirements format.

    packages are listed in a case-insensitive sorted order.
    

      %prog [options]

---


    EXPERIMENTAL - Lock packages and their dependencies from:

    - PyPI (and other indexes) using requirement specifiers.
    - VCS project urls.
    - Local project directories.
    - Local or remote source archives.

    pip also supports locking from "requirements files", which provide an easy
    way to specify a whole environment to be installed.

    The generated lock file is only guaranteed to be valid for the current
    python version and platform.
    

      %prog [options] [-e] <local project path> ...
      %prog [options] <requirement specifier> [package-index-options] ...
      %prog [options] -r <requirements file> [package-index-options] ...
      %prog [options] <archive url/path> ...

---

A single place for constructing and exposing the main parser
Creates and returns the main parser for pip's CLI

---

Base Command class, and related routines

        This is a no-op so that commands by default do not do the pip version
        check.
        

---

Get an object that can be used to render the download progress.

    Returns a callable, that takes an iterable to "wrap".
    
Get an object that can be used to render the install progress.
    Returns a callable, that takes an iterable to "wrap".
    

---

Primary application entrypoint.

---

Base option parser setup
A prettier/less verbose help formatter for optparse.

        Return a comma-separated list of option strings and metavars.

        :param option:  tuple of (short opt, long opt), e.g: ('-f', '--format')
        :param mvarfmt: metavar format string
        :param optsep:  separator
        

        Ensure there is only one newline between usage and the first heading
        if there is no description.
        
Custom help formatter for use in ConfigOptionParser.

    This is updates the defaults before expanding them, allowing
    them to show up correctly in the help listing.

    Also redact auth from url type options
    
Insert an OptionGroup at a given position.
Get a list of all options, including those in option groups.
Custom option parser which updates its defaults by checking the
    configuration files and environmental variables
Updates the given defaults with values from the config files and
        the environ. Does a little special handling for certain types of
        options (lists).
Overriding to make updating the defaults after instantiation of
        the option parser possible, _update_defaults() does the dirty work.

---



---

Logic that powers autocompletion installed by ``pip completion``.
Entry Point for completion of main and subcommand options.
Get the type of path completion (``file``, ``dir``, ``path`` or None)

    :param cwords: same as the environmental variable ``COMP_WORDS``
    :param cword: same as the environmental variable ``COMP_CWORD``
    :param opts: The available options to check
    :return: path completion type (``file``, ``dir``, ``path`` or None)
    
If ``completion_type`` is ``file`` or ``path``, list all regular files
    and directories starting with ``current``; otherwise only list directories
    starting with ``current``.

    :param current: The word to be completed
    :param completion_type: path completion type(``file``, ``path`` or ``dir``)
    :return: A generator of regular files and/or directories
    

---


Contains command classes which may interact with an index / the network.

Unlike its sister module, req_command, this module still uses lazy imports
so commands which don't always hit the network (e.g. list w/o --outdated or
--uptodate) don't need waste time importing PipSession and friends.


    A class mixin for command classes needing _build_session().
    
Return a list of index urls from user-provided options.
Get a default-managed session.

    Abstract base class for commands with the index_group options.

    This also corresponds to the commands that permit the pip version check.
    

        Do the pip version check if not disabled.

        This overrides the default behavior of not doing the check.
        

---

Contains the RequirementCommand base class.

This class is in a separate module so the commands that do not always
need PackageFinder capability don't unnecessarily import the
PackageFinder machinery and all its vendored dependencies, etc.

Decorator for common logic related to managing temporary
    directories.
    
Determines which resolver should be used, based on the given options.

        Create a RequirementPreparer instance for the given parameters.
        

        Create a Resolver instance for the given parameters.
        

        Parse command-line arguments into the corresponding requirements.
        

        Trace basic information about the provided objects.
        

        Create a package finder appropriate to this requirement command.

        :param ignore_requires_python: Whether to ignore incompatible
            "Requires-Python" values in links. Defaults to False.
        

---

Subpackage containing all of pip's command line interface related code

---



---


shared options and groups

The principle here is to define options once, but *not* instantiate them
globally. One reason being that options with action='append' can carry state
between parses. pip parses general options twice internally, and shouldn't
pass on state. To be consistent, all options will follow this design.


    Raise an option parsing error using parser.error().

    Args:
      parser: an OptionParser instance.
      option: an Option instance.
      msg: the error text.
    

    Return an OptionGroup object
    group  -- assumed to be dict with 'name' and 'options' keys
    parser -- an optparse Parser
    
Function for determining if custom platform options are allowed.

    :param options: The OptionParser options.
    :param check_target: Whether or not to check if --target is being used.
    
Get a format_control object.

    Convert a version string like "3", "37", or "3.7.3" into a tuple of ints.

    :return: A 2-tuple (version_info, error_msg), where `error_msg` is
        non-None if and only if there was a parsing error.
    

    Handle a provided --python-version value.
    
\
    The Python interpreter version to use for wheel and "Requires-Python"
    compatibility checks. Defaults to a version derived from the running
    interpreter. The version can be specified using up to three dot-separated
    integers (e.g. "3" for 3.0.0, "3.7" for 3.7.0, or "3.7.3"). A major-minor
    version can also be given as a string without dots (e.g. "37" for 3.7.0).
    

    Process a value provided for the --no-cache-dir option.

    This is an optparse.Option callback for the --no-cache-dir option.
    

    Process a value provided for the --group option.

    Splits on the rightmost ":", and validates that the path (if present) ends
    in `pyproject.toml`. Defaults the path to `pyproject.toml` when one is not given.

    `:` cannot appear in dependency group names, so this is a safe and simple parse.

    This is an optparse.Option callback for the dependency_groups option.
    

    Process a value provided for the --no-use-pep517 option.

    This is an optparse.Option callback for the no_use_pep517 option.
    
A value was passed for --no-use-pep517,
        probably using either the PIP_NO_USE_PEP517 environment variable
        or the "no-use-pep517" config file option. Use an appropriate value
        of the PIP_USE_PEP517 environment variable or the "use-pep517"
        config file option instead.
        
Given a value spelled "algo:digest", append the digest to a list
    pointed to in a dict by the algo name.

---



---



---



---

Get item from a package name lookup mapping with a resolver identifier.

    This extra logic is needed when the target mapping is keyed by package
    name, which cannot be directly looked up with an identifier (which may
    contain requested extras). Additional logic is added to also look up a value
    by "cleaning up" the extras from the identifier.
    
Pip's provider implementation for resolvelib.

    :params constraints: A mapping of constraints specified by the user. Keys
        are canonicalized project names.
    :params ignore_dependencies: Whether the user specified ``--no-deps``.
    :params upgrade_strategy: The user-specified upgrade strategy.
    :params user_requested: A set of canonicalized package names that the user
        supplied for pip to install/upgrade.
    
Produce a subset of identifiers that should be considered before others.

        Currently pip narrows the following selection:
            * Requires-Python, if present is always returned by itself
            * Backtrack causes are considered next because they can be identified
              in linear time here, whereas because get_preference() is called
              for each identifier, it would be quadratic to check for them there.
              Further, the current backtrack causes likely need to be resolved
              before other requirements as a resolution can't be found while
              there is a conflict.
        
Produce a sort key for given requirement based on preference.

        The lower the return value is, the more preferred this group of
        arguments is.

        Currently pip considers the following in order:

        * Any requirement that is "direct", e.g., points to an explicit URL.
        * Any requirement that is "pinned", i.e., contains the operator ``===``
          or ``==`` without a wildcard.
        * Any requirement that imposes an upper version limit, i.e., contains the
          operator ``<``, ``<=``, ``~=``, or ``==`` with a wildcard. Because
          pip prioritizes the latest version, preferring explicit upper bounds
          can rule out infeasible candidates sooner. This does not imply that
          upper bounds are good practice; they can make dependency management
          and resolution harder.
        * Order user-specified requirements as they are specified, placing
          other requirements afterward.
        * Any "non-free" requirement, i.e., one that contains at least one
          operator, such as ``>=`` or ``!=``.
        * Alphabetical order for consistency (aids debuggability).
        
Are upgrades allowed for this project?

            This checks the upgrade strategy, and whether the project was one
            that the user specified in the command line, in order to decide
            whether we should upgrade if there's a newer version available.

            (Note that we don't need access to the `--upgrade` flag, because
            an upgrade strategy of "to-satisfy-only" means that `--upgrade`
            was not specified).
            

---

The "project name" of a requirement.

        This is different from ``name`` if this requirement contains extras,
        in which case ``name`` would contain the ``[...]`` part, while this
        refers to the name of the project.
        
The name identifying this requirement in the resolver.

        This is different from ``project_name`` if this requirement contains
        extras, where ``project_name`` would not contain the ``[...]`` part.
        
The "project name" of the candidate.

        This is different from ``name`` if this candidate contains extras,
        in which case ``name`` would contain the ``[...]`` part, while this
        refers to the name of the project.
        
The name identifying this candidate in the resolver.

        This is different from ``project_name`` if this candidate contains
        extras, where ``project_name`` would not contain the ``[...]`` part.
        

---

A reporter that does an info log for every event it sees.

---

Get order for installation of requirements in RequirementSet.

        The returned list contains a requirement before another that depends on
        it. This helps ensure that the environment is kept consistent as they
        get installed one-by-one.

        The current implementation creates a topological ordering of the
        dependency graph, giving more weight to packages with less
        or no dependencies, while breaking any cycles in the graph at
        arbitrary points. We make no guarantees about where the cycle
        would be broken, other than it *would* be broken.
        
Assign weights to each node based on how "deep" they are.

    This implementation may change at any point in the future without prior
    notice.

    We first simplify the dependency graph by pruning any leaves and giving them
    the highest weight: a package without any dependencies should be installed
    first. This is done again and again in the same way, giving ever less weight
    to the newly found leaves. The loop stops when no leaves are left: all
    remaining packages have at least one dependency left in the graph.

    Then we continue with the remaining graph, by taking the length for the
    longest path to any node from root, ignoring any paths that contain a single
    node twice (i.e. cycles). This is done through a depth-first search through
    the graph, while keeping track of the path to the node.

    Cycles in the graph result would result in node being revisited while also
    being on its own path. In this case, take no action. This helps ensure we
    don't get stuck in a cycle.

    When assigning weight, the longer path (i.e. larger length) is preferred.

    We are only interested in the weights of packages that are in the
    requirement_keys.
    
Key function used to sort install requirements for installation.

    Based on the "weight" mapping calculated in ``get_installation_order()``.
    The canonical package name is returned as the second member as a tie-
    breaker to ensure the result is predictable, which is useful in tests.
    

---

The runtime version of BaseCandidate.
A candidate backed by an ``InstallRequirement``.

    This represents a package request with the target not being already
    in the environment, and needs to be fetched and installed. The backing
    ``InstallRequirement`` is responsible for most of the leg work; this
    class exposes appropriate information to the resolver.

    :param link: The link passed to the ``InstallRequirement``. The backing
        ``InstallRequirement`` will use this link to fetch the distribution.
    :param source_link: The link this candidate "originates" from. This is
        different from ``link`` when the link is found in the wheel cache.
        ``link`` would point to the wheel cache, while this points to the
        found remote link (e.g. from pypi.org).
    
The normalised name of the project the candidate refers to
Check for consistency of project name and version of dist.
A candidate that has 'extras', indicating additional dependencies.

    Requirements can be for a project with dependencies, something like
    foo[extra].  The extras don't affect the project/version being installed
    directly, but indicate that we need additional dependencies. We model that
    by having an artificial ExtrasCandidate that wraps the "base" candidate.

    The ExtrasCandidate differs from the base in the following ways:

    1. It has a unique name, of the form foo[extra]. This causes the resolver
       to treat it as a separate node in the dependency graph.
    2. When we're getting the candidate's dependencies,
       a) We specify that we want the extra dependencies as well.
       b) We add a dependency on the base candidate.
          See below for why this is needed.
    3. We return None for the underlying InstallRequirement, as the base
       candidate will provide it, and we don't want to end up with duplicates.

    The dependency on the base candidate is needed so that the resolver can't
    decide that it should recommend foo[extra1] version 1.0 and foo[extra2]
    version 2.0. Having those candidates depend on foo=1.0 and foo=2.0
    respectively forces the resolver to recognise that this is a conflict.
    

        :param comes_from: the InstallRequirement that led to this candidate if it
            differs from the base's InstallRequirement. This will often be the
            case in the sense that this candidate's requirement has the extras
            while the base's does not. Unlike the InstallRequirement backed
            candidates, this requirement is used solely for reporting purposes,
            it does not do any leg work.
        
The normalised name of the project the candidate refers to

---

Utilities to lazily create and visit candidates found.

Creating and visiting a candidate is a *very* costly operation. It involves
fetching, extracting, potentially building modules from source, and verifying
distribution metadata. It is therefore crucial for performance to keep
everything here lazy all the way down, so we only touch candidates that we
absolutely need, and not "download the world" when we only need one version of
something.

Iterator for ``FoundCandidates``.

    This iterator is used when the package is not already installed. Candidates
    from index come later in their normal ordering.
    
Iterator for ``FoundCandidates``.

    This iterator is used when the resolver prefers the already-installed
    candidate and NOT to upgrade. The installed candidate is therefore
    always yielded first, and candidates from index come later in their
    normal ordering, except skipped when the version is already installed.
    
Iterator for ``FoundCandidates``.

    This iterator is used when the resolver prefers to upgrade an
    already-installed package. Candidates from index are returned in their
    normal ordering, except replaced when the version is already installed.

    The implementation iterates through and yields other candidates, inserting
    the installed candidate exactly once before we start yielding older or
    equivalent candidates, or after all other candidates if they are all newer.
    
A lazy sequence to provide candidates to the resolver.

    The intended usage is to return this from `find_matches()` so the resolver
    can iterate through the sequence multiple times, but only access the index
    page when remote packages are actually needed. This improve performances
    when suitable candidates are already installed on disk.
    

---


    Requirement backed by an install requirement on a base package.
    Trims extras from its install requirement if there are any.
    
A requirement representing Requires-Python metadata.
A requirement that cannot be satisfied.

---



---

Get the candidate for the currently-installed version.
Produce explicit candidates from the base given an extra-ed package.

        :param base_requirements: Requirements known to the resolver. The
            requirements are guaranteed to not have extras.
        :param extras: The extras to inject into the explicit requirements'
            candidates.
        
Produce explicit candidates from constraints.

        This creates "fake" InstallRequirement objects that are basically clones
        of what "should" be the template, but with original_link set to link.
        

        Returns requirement objects associated with the given InstallRequirement. In
        most cases this will be a single object but the following special cases exist:
            - the InstallRequirement has markers that do not apply -> result is empty
            - the InstallRequirement has both a constraint (or link) and extras
                -> result is split in two requirement objects: one with the constraint
                (or link) and one with the extra. This allows centralized constraint
                handling for the base, resulting in fewer candidate rejections.
        

        Returns requirement objects associated with the given specifier. In most cases
        this will be a single object but the following special cases exist:
            - the specifier has markers that do not apply -> result is empty
            - the specifier has both a constraint and extras -> result is split
                in two requirement objects: one with the constraint and one with the
                extra. This allows centralized constraint handling for the base,
                resulting in fewer candidate rejections.
        
Look up the link in the wheel cache.

        If ``preparer.require_hashes`` is True, don't use the wheel cache,
        because cached wheels, always built locally, have different hashes
        than the files downloaded from the index server and thus throw false
        hash mismatches. Furthermore, cached wheels at present have
        nondeterministic contents due to file modification times.
        

---

Dependency Resolution

The dependency resolution in pip is performed as follows:

for top-level requirements:
    a. only one spec allowed per project, regardless of conflicts or not.
       otherwise a "double requirement" exception is raised
    b. they override sub-dependency requirements.
for sub-dependencies
    a. "first found, wins" (where the order is breadth first)


    Check whether the given Python version is compatible with a distribution's
    "Requires-Python" value.

    :param version_info: A 3-tuple of ints representing the Python
        major-minor-micro version to check.
    :param ignore_requires_python: Whether to ignore the "Requires-Python"
        value if the given Python version isn't compatible.

    :raises UnsupportedPythonVersion: When the given Python version isn't
        compatible.
    
Resolves which packages need to be installed/uninstalled to perform \
    the requested operation without breaking the requirements of any package.
    
Resolve what operations need to be done

        As a side-effect of this method, the packages (and their dependencies)
        are downloaded, unpacked and prepared for installation. This
        preparation is done by ``pip.operations.prepare``.

        Once PyPI has static dependency metadata available, it would be
        possible to move the preparation to become a step separated from
        dependency resolution.
        
Add install_req as a requirement to install.

        :param parent_req_name: The name of the requirement that needed this
            added. The name is used because when multiple unnamed requirements
            resolve to the same name, we could otherwise end up with dependency
            links that point outside the Requirements set. parent_req must
            already be added. Note that None implies that this is a user
            supplied requirement, vs an inferred one.
        :param extras_requested: an iterable of extras used to evaluate the
            environment markers.
        :return: Additional requirements to scan. That is either [] if
            the requirement is not applicable, or [install_req] if the
            requirement is applicable and has just been added.
        

        Set a requirement to be installed.
        
Check if req_to_install should be skipped.

        This will check if the req is installed, and whether we should upgrade
        or reinstall it, taking into account all the relevant user options.

        After calling this req_to_install will only have satisfied_by set to
        None if the req_to_install is to be upgraded/reinstalled etc. Any
        other value will be a dist recording the current thing installed that
        satisfies the requirement.

        Note that for vcs urls and the like we can't assess skipping in this
        routine - we simply identify that we need to pull the thing down,
        then later on it is pulled down and introspected to assess upgrade/
        reinstalls etc.

        :return: A text reason for why it was skipped, or None.
        
Ensure that if a link can be found for this, that it is found.

        Note that req.link may still be None - if the requirement is already
        installed and not needed to be upgraded based on the return value of
        _is_upgrade_allowed().

        If preparer.require_hashes is True, don't use the wheel cache, because
        cached wheels, always built locally, have different hashes than the
        files downloaded from the index server and thus throw false hash
        mismatches. Furthermore, cached wheels at present have undeterministic
        contents due to file modification times.
        
Takes a InstallRequirement and returns a single AbstractDist \
        representing a prepared variant of the same.
        
Prepare a single requirements file.

        :return: A list of additional InstallRequirements to also install.
        
Create the installation order.

        The installation order is topological - requirements are installed
        before the requiring thing. We break cycles at an arbitrary point,
        and make no other guarantees.
        

---



---

Handles all VCS (version control) support

    Return true if the name looks like a URL.
    

    Return the URL for a VCS requirement.

    Args:
      repo_url: the remote VCS url, with any needed VCS prefix (e.g. "git+").
      project_name: the (unescaped) project name.
    

    Find the the Python project's root by searching up the filesystem from
    `location`. Return the path to project root relative to `repo_root`.
    Return None if the project root is `repo_root`, or cannot be found.
    

    Encapsulates a VCS-specific revision to install, along with any VCS
    install options.

    Args:
        vc_class: a VersionControl subclass.
        rev: the name of the revision to install.
        extra_args: a list of extra options.
    

        Return the VCS-specific command arguments.
        

        Make a copy of the current instance, but with a new rev.

        Args:
          rev: the name of the revision for the new object.
        

        Return a VersionControl object if a repository of that type is found
        at the given directory.
        

        Return a VersionControl object or None.
        

        Return a VersionControl object or None.
        

        Return whether the vcs prefix (e.g. "git+") should be added to a
        repository's remote url when used in a requirement.
        

        Return the path to Python project root, relative to the repo root.
        Return None if the project root is in the repo root.
        

        Return the revision string that should be used in a requirement.
        

        Return the requirement string to use to redownload the files
        currently at the given repository directory.

        Args:
          project_name: the (unescaped) project name.

        The return value has a form similar to the following:

            {repository_url}@{revision}#egg={project_name}
        

        Return the base revision arguments for a vcs command.

        Args:
          rev: the name of a revision to install.  Cannot be None.
        

        Return true if the commit hash checked out at dest matches
        the revision in url.

        Always return False, if the VCS does not support immutable commit
        hashes.

        This method does not check if there are local uncommitted changes
        in dest after checkout, as pip currently has no use case for that.
        

        Return a RevOptions object.

        Args:
          rev: the name of a revision to install.
          extra_args: a list of extra options.
        

        posix absolute paths start with os.path.sep,
        win32 ones start with drive (like c:\\folder)
        

        Parse the repository URL's netloc, and return the new netloc to use
        along with auth information.

        Args:
          netloc: the original repository URL netloc.
          scheme: the repository URL's scheme without the vcs prefix.

        This is mainly for the Subversion class to override, so that auth
        information can be provided via the --username and --password options
        instead of through the URL.  For other subclasses like Git without
        such an option, auth information must stay in the URL.

        Returns: (netloc, (username, password)).
        

        Parse the repository URL to use, and return the URL, revision,
        and auth info to use.

        Returns: (url, rev, (username, password)).
        

        Return the RevOptions "extra arguments" to use in obtain().
        

        Return the URL and RevOptions object to use in obtain(),
        as a tuple (url, rev_options).
        

        Normalize a URL for comparison by unquoting it and removing any
        trailing slash.
        

        Compare two repo URLs for identity, ignoring incidental differences.
        

        Fetch a revision from a repository, in the case that this is the
        first fetch from the repository.

        Args:
          dest: the directory to fetch the repository to.
          rev_options: a RevOptions object.
          verbosity: verbosity level.
        

        Switch the repo at ``dest`` to point to ``URL``.

        Args:
          rev_options: a RevOptions object.
        

        Update an already-existing repo to the given ``rev_options``.

        Args:
          rev_options: a RevOptions object.
        

        Return whether the id of the current commit equals the given name.

        Args:
          dest: the repository directory.
          name: a string name.
        

        Install or update in editable mode the package represented by this
        VersionControl object.

        :param dest: the repository directory in which to install or update.
        :param url: the repository URL starting with a vcs prefix.
        :param verbosity: verbosity level.
        

        Clean up current location and download the url repository
        (and vcs infos) into location

        :param url: the repository URL starting with a vcs prefix.
        :param verbosity: verbosity level.
        

        Return the url used at location

        Raises RemoteNotFoundError if the repository does not have a remote
        url configured.
        

        Return the current commit id of the files at the given location.
        

        Run a VCS subcommand
        This is simply a wrapper around call_subprocess that adds the VCS
        command name, and checks that the VCS is available
        

        Return whether a directory path is a repository directory.
        

        Return the "root" (top-level) directory controlled by the vcs,
        or `None` if the directory is not in any.

        It is meant to be overridden to implement smarter detection
        mechanisms for specific vcs.

        This can do more than is_repository_directory() alone. For
        example, the Git override checks that Git is actually available.
        

---


        Return the repository-local changeset revision number, as an integer.
        

        Return the changeset identification hash, as a 40-character
        hexadecimal string
        
Always assume the versions don't match

        Return the path to Python project root, relative to the repo root.
        Return None if the project root is in the repo root.
        

---


        Return the maximum revision for all files under a given location
        

        This override allows the auth information to be passed to svn via the
        --username and --password options instead of via the URL.
        
Always assume the versions don't match
Query the version of the currently installed Subversion client.

        :return: A tuple containing the parts of the version information or
            ``()`` if the version returned from ``svn`` could not be parsed.
        :raises: BadCommand: If ``svn`` is not installed.
        
Return the version of the currently installed Subversion client.

        If the version of the Subversion client has already been queried,
        a cached value will be used.

        :return: A tuple containing the parts of the version information or
            ``()`` if the version returned from ``svn`` could not be parsed.
        :raises: BadCommand: If ``svn`` is not installed.
        
Return options to be used on calls to Subversion that contact the server.

        These options are applicable for the following ``svn`` subcommands used
        in this class.

            - checkout
            - switch
            - update

        :return: A list of command line arguments to pass to ``svn``.
        

---

^
    # Optional user, e.g. 'git@'
    (\w+@)?
    # Server, e.g. 'github.com'.
    ([^/:]+):
    # The server-side path. e.g. 'user/project.git'. Must start with an
    # alphanumeric character so as not to be confusable with a Windows paths
    # like 'C:/foo/bar' or 'C:\foo\bar'.
    (\w[^:]*)
    $

        Return the current branch, or None if HEAD isn't at a branch
        (e.g. detached HEAD).
        

        Return (sha_or_none, is_branch), where sha_or_none is a commit hash
        if the revision names a remote branch or tag, otherwise None.

        Args:
          dest: the repository directory.
          rev: the revision name.
        

        Return true if rev is a ref or is a commit that we don't have locally.

        Branches and tags are not considered in this method because they are
        assumed to be always available locally (which is a normal outcome of
        ``git clone`` and ``git fetch --tags``).
        

        Resolve a revision to a new RevOptions object with the SHA1 of the
        branch, tag, or ref if found.

        Args:
          rev_options: a RevOptions object.
        

        Return whether the current commit hash equals the given name.

        Args:
          dest: the repository directory.
          name: a string name.
        

        Return URL of the first remote encountered.

        Raises RemoteNotFoundError if the repository does not have a remote
        url configured.
        

        Convert a remote url from what git uses to what pip accepts.

        There are 3 legal forms **url** may take:

            1. A fully qualified url: ssh://git@example.com/foo/bar.git
            2. A local project.git folder: /path/to/bare/repository.git
            3. SCP shorthand for form 1: git@example.com:foo/bar.git

        Form 1 is output as-is. Form 2 must be converted to URI and form 3 must
        be converted to form 1.

        See the corresponding test test_git_remote_url_to_pip() for examples of
        sample inputs/outputs.
        

        Check if rev is a commit that is available in the local repository.
        

        Return the path to Python project root, relative to the repo root.
        Return None if the project root is in the repo root.
        

        Prefixes stub URLs like 'user@hostname:user/repo.git' with 'ssh://'.
        That's required because although they use SSH they sometimes don't
        work with a ssh:// scheme (e.g. GitHub). But we need a scheme for
        parsing. Hence we remove it again afterwards and return it as a stub.
        
In either https or ssh form, requirements must be prefixed with git+.

---

Always assume the versions don't match

---



---


    Encapsulates the candidate selection preferences for downloading
    and installing files.
    
Create a SelectionPreferences object.

        :param allow_yanked: Whether files marked as yanked (in the sense
            of PEP 592) are permitted to be candidates for install.
        :param format_control: A FormatControl object or None. Used to control
            the selection of source packages / binary packages when consulting
            the index and links.
        :param prefer_binary: Whether to prefer an old, but valid, binary
            dist over a new source dist.
        :param ignore_requires_python: Whether to ignore incompatible
            "Requires-Python" values in links. Defaults to False.
        

---

Links to content may have embedded hash values. This class parses those.

    `name` must be any member of `_SUPPORTED_HASHES`.

    This class can be converted to and from `ArchiveInfo`. While ArchiveInfo intends to
    be JSON-serializable to conform to PEP 610, this class contains the logic for
    parsing a hash name and value for correctness, and then checking whether that hash
    conforms to a schema with `.is_hash_allowed()`.
Search a string for a checksum algorithm name and encoded output value.
Return a Hashes instance which checks only for the current hash.

        Return True if the current hash is allowed by `hashes`.
        
Information about a core metadata file associated with a distribution.

    Clean a "part" of a URL path (i.e. after splitting on "@" characters).
    

    Clean the first part of a URL path that corresponds to a local
    filesystem path (i.e. the first part after splitting on "@" characters).
    

    Clean the path portion of a URL.
    

    Make sure a link is fully quoted.
    For example, if ' ' occurs in the URL, it will be replaced with "%20",
    and without double-quoting other characters.
    

    A faster implementation of urllib.parse.urljoin with a shortcut
    for absolute http/https URLs.
    
Represents a parsed link from a Package Index's simple URL

        :param url: url of the resource pointed to (href of the link)
        :param comes_from: instance of IndexContent where the link was found,
            or string.
        :param requires_python: String containing the `Requires-Python`
            metadata field, specified in PEP 345. This may be specified by
            a data-requires-python attribute in the HTML link tag, as
            described in PEP 503.
        :param yanked_reason: the reason the file has been yanked, if the
            file has been yanked, or None if the file hasn't been yanked.
            This is the value of the "data-yanked" attribute, if present, in
            a simple repository HTML link. If the file has been yanked but
            no reason was provided, this should be the empty string. See
            PEP 592 for more information and the specification.
        :param metadata_file_data: the metadata attached to the file, or None if
            no such metadata is provided. This argument, if not None, indicates
            that a separate metadata file exists, and also optionally supplies
            hashes for that file.
        :param cache_link_parsing: A flag that is used elsewhere to determine
            whether resources retrieved from this link should be cached. PyPI
            URLs should generally have this set to False, for example.
        :param hashes: A mapping of hash names to digests to allow us to
            determine the validity of a download.
        

        Convert an pypi json document from a simple repository page into a Link.
        

        Convert an anchor element's attributes in a simple repository page to a Link.
        

        This can contain auth information.
        
Return a link to the associated core metadata file (if any).

        Return True if the link has a hash and it is allowed by `hashes`.
        
Convert link for equivalency check.

    This is used in the resolver to check whether two URL-specified requirements
    likely point to the same distribution and can be considered equivalent. This
    equivalency logic avoids comparing URLs literally, which can be too strict
    (e.g. "a=1&b=2" vs "b=2&a=1") and produce conflicts unexpecting to users.

    Currently this does three things:

    1. Drop the basic auth part. This is technically wrong since a server can
       serve different content based on auth, but if it does that, it is even
       impossible to guarantee two URLs without auth are equivalent, since
       the user can input different auth information when prompted. So the
       practical solution is to assume the auth doesn't affect the response.
    2. Parse the query to avoid the ordering issue. Note that ordering under the
       same key in the query are NOT cleaned; i.e. "a=1&a=2" and "a=2&a=1" are
       still considered different.
    3. Explicitly drop most of the fragment part, except ``subdirectory=`` and
       hash values, since it should have no impact the downloaded content. Note
       that this drops the "egg=" part historically used to denote the requested
       project (and extras), which is wrong in the strictest sense, but too many
       people are supplying it inconsistently to cause superfluous resolution
       conflicts, so we choose to also ignore them.
    

---

PEP 610
Get value from dictionary and verify expected type.
Make dict excluding None values.
url with user:password part removed unless it is formed with
        environment variables as specified in PEP 610, or it is ``git``
        in the case of a git URL.
        

---



---

Represents a Package Index and provides easier access to endpoints

---

Helper for managing formats from which a package can be installed.

---


For types associated with installation schemes.

For a general overview of available schemes and their context, see
https://docs.python.org/3/install/index.html#alternate-installation.

A Scheme holds paths which are used as the base directories for
    artifacts associated with a Python package.
    

---

Represents a wheel file and provides access to the various parts of the
name that have meaning.

A wheel file
^(?P<namever>(?P<name>[^\s-]+?)-(?P<ver>[^\s-]*?))
        ((-(?P<build>\d[^-]*?))?-(?P<pyver>[^\s-]+?)-(?P<abi>[^\s-]+?)-(?P<plat>[^\s-]+?)
        \.whl|\.dist-info)$
Return the wheel's tags as a sorted list of strings.
Return the lowest index that one of the wheel's file_tag combinations
        achieves in the given list of supported tags.

        For example, if there are 8 supported tags and one of the file tags
        is first in the list, then return 0.

        :param tags: the PEP 425 tags to check the wheel against, in order
            with most preferred first.

        :raises ValueError: If none of the wheel's file tags match one of
            the supported tags.
        
Return the priority of the most preferred tag that one of the wheel's file
        tag combinations achieves in the given list of supported tags using the given
        tag_to_priority mapping, where lower priorities are more-preferred.

        This is used in place of support_index_min in some cases in order to avoid
        an expensive linear scan of a large list of tags.

        :param tags: the PEP 425 tags to check the wheel against.
        :param tag_to_priority: a mapping from tag to priority of that tag, where
            lower is more preferred.

        :raises ValueError: If none of the wheel's file tags match one of
            the supported tags.
        
Return whether the wheel is compatible with one of the given tags.

        :param tags: the PEP 425 tags to check the wheel against.
        

---

A package that contains models that represent entities.

---


    Encapsulates the locations that pip is configured to search.
    

        Create a SearchScope object after normalizing the `find_links`.
        
Returns the locations found via self.index_urls

        Checks the url_name on the main (first in the list) index and
        use this url_name to produce all locations
        

---



---


    Encapsulates the properties of a Python interpreter one is targeting
    for a package install, download, etc.
    

        :param platforms: A list of strings or None. If None, searches for
            packages that are supported by the current system. Otherwise, will
            find packages that can be built on the platforms passed in. These
            packages will only be downloaded for distribution: they will
            not be built locally.
        :param py_version_info: An optional tuple of ints representing the
            Python version information to use (e.g. `sys.version_info[:3]`).
            This can have length 1, 2, or 3 when provided.
        :param abis: A list of strings or None. This is passed to
            compatibility_tags.py's get_supported() function as is.
        :param implementation: A string or None. This is passed to
            compatibility_tags.py's get_supported() function as is.
        

        Format the given, non-None attributes for display.
        

        Return the supported PEP 425 tags to check wheel candidates against.

        The tags are returned in order of preference (most preferred first).
        
Exactly the same as get_sorted_tags, but returns a set.

        This is important for performance.
        

---

Represents a potential "candidate" for installation.

---

Represents a source distribution.

    The preparation step for these needs metadata for the packages to be
    generated, either using PEP 517 or using the legacy `setup.py egg_info`.
    
Identify this requirement uniquely by its link.

---

A base class for handling installable artifacts.

    The requirements for anything installable are as follows:

     - we must be able to determine the requirement name
       (or we can't correctly handle the non-upgrade case).

     - for packages with setup requirements, we must also be able
       to determine their requirements without installing additional
       packages (for the same reason as run-time dependencies)

     - we must be able to create a Distribution object exposing the
       above metadata.

     - if we need to do work in the build tracker, we must be able to generate a unique
       string to identify the requirement in the build tracker.
    
A string that uniquely identifies this requirement to the build tracker.

        If None, then this dist has no work to do in the build tracker, and
        ``.prepare_distribution_metadata()`` will not be called.

---

Represents a wheel distribution.

    This does not need any preparation as wheels can be directly unpacked.
    
Loads the metadata from the wheel file into memory and returns a
        Distribution that uses it, not relying on the wheel file or
        requirement.
        

---

Returns a Distribution for the given InstallRequirement

---

Represents an installed package.

    This does not need any preparation as the required information has already
    been computed.
    

---


    Parse dependency groups data as provided via the CLI, in a `[path:]group` syntax.

    Raises InstallationErrors if anything goes wrong.
    

    Run all resolution, converting any error from `DependencyGroupResolver` into
    an InstallationError.
    

    This helper loads a pyproject.toml as TOML.

    It raises an InstallationError if the operation fails.
    

---

Create the fully qualified name of the files created by
    {console,gui}_scripts for the given ``dist``.
    Returns the list of file names
    

    Yield all the uninstallation paths for dist based on RECORD-without-.py[co]

    Yield paths to all the files in RECORD. For each .py file in RECORD, add
    the .pyc and .pyo in the same directory.

    UninstallPathSet.add() takes care of the __pycache__ .py[co].

    If RECORD is not found, raises an error,
    with possible information from the INSTALLER file.

    https://packaging.python.org/specifications/recording-installed-packages/
    
Compact a path set to contain the minimal number of paths
    necessary to contain all paths in the set. If /a/path/ and
    /a/path/to/a/file.txt are both in the set, leave only the
    shorter path.
Returns a set containing the paths that need to be renamed.

    This set may include directories when the original sequence of paths
    included every file on disk.
    
Returns a tuple of 2 sets of which paths to display to user

    The first set contains paths that would be deleted. Files of a package
    are not added and the top-level directory of the package has a '*' added
    at the end - to signify that all it's contents are removed.

    The second set contains files that would have been skipped in the above
    folders.
    
A set of file rename operations to stash files while
    tentatively uninstalling them.
Stashes a directory.

        Directories are stashed adjacent to their original location if
        possible, or else moved/copied into the user's temp dir.
Stashes a file.

        If no root has been provided, one will be created for the directory
        in the user's temp directory.
Stashes the directory or file and returns its new location.
        Handle symlinks as files to avoid modifying the symlink targets.
        
Commits the uninstall by removing stashed files.
Undoes the uninstall by moving stashed files back.
A set of file paths to be removed in the uninstallation of a
    requirement.

        Return True if the given path is one we are permitted to
        remove/modify, False otherwise.

        
Remove paths in ``self._paths`` with confirmation (unless
        ``auto_confirm`` is True).
Display which files would be deleted and prompt for confirmation
Rollback the changes previously made by remove().
Remove temporary save dir: rollback will no longer be possible.

---

Backing implementation for InstallRequirement's various constructors

The idea here is that these formed a major chunk of InstallRequirement's size
so, moving them and support code dedicated to them outside of that class
helps creates for better understandability for the rest of the code.

These are meant to be used elsewhere within pip to create instances of
InstallRequirement.


    Returns a new requirement based on the given one, with the supplied extras. If the
    given requirement already has extras those are replaced (or dropped if no new extras
    are given).
    
Parses an editable requirement into:
        - a requirement name
        - an URL
        - extras
        - editable options
    Accepted requirements:
        svn+http://blahblah@rev#egg=Foobar[baz]&subdirectory=version_subdir
        .[some_extra]
    
Check if file is parsable as a requirements file.

    This is heavily based on ``pkg_resources.parse_requirements``, but
    simplified to just check the first meaningful line.

    :raises InvalidRequirement: If the first meaningful line cannot be parsed
        as an requirement.
    
Returns helpful msg in case requirements file does not exist,
    or cannot be parsed.

    :params req: Requirements file path
    
Checks whether the string "looks like" a path on the filesystem.

    This does not check whether the target actually exists, only judge from the
    appearance.

    Returns true if any of the following conditions is true:
    * a path separator is found (either os.path.sep or os.path.altsep);
    * a dot is found (which represents the current directory).
    

    First, it checks whether a provided path is an installable directory. If it
    is, returns the path.

    If false, check if the path is an archive file (such as a .whl).
    The function checks if the path is a file. If false, if the path has
    an @, it will treat it as a PEP 440 URL requirement and return the path.
    
Creates an InstallRequirement from a name, which might be a
    requirement, directory containing 'setup.py', filename, or URL.

    :param line_source: An optional string describing where the line is from,
        for logging purposes in case of an error.
    

    Creates a new InstallationRequirement using the given template but without
    any extras. Sets the original requirement as the new one's parent
    (comes_from).
    

    Returns a copy of an installation requirement with some additional extras.
    Makes a shallow copy of the ireq object.
    

---

Create a RequirementSet.
Return the list of requirements that need to be installed.

        TODO remove this property together with the legacy resolver, since the new
             resolver only returns requirements that need to be installed.
        

---


    Represents something that may be installed later on, may have information
    about where to fetch the relevant requirement and also contains logic for
    installing the said requirement.
    
An un-tested helper for getting state, for debugging.
Whether this requirement was specified as a direct URL.
Return whether I am pinned to an exact version.

        For example, some-package==1.2 is pinned; some-package>1.2 is not.
        
Return whether any known-good hashes are specified as options.

        These activate --require-hashes mode; hashes specified as part of a
        URL do not.

        
Return a hash-comparer that considers my option- and URL-based
        hashes to be known-good.

        Hashes in URLs--ones embedded in the requirements file, not ones
        downloaded from an index server--are almost peers with ones from
        flags. They satisfy --require-hashes (whether it was implicitly or
        explicitly activated) but do not activate it. md5 and sha224 are not
        allowed in flags, which should nudge people toward good algos. We
        always OR all hashes together, even ones from URLs.

        :param trust_internet: Whether to trust URL-based (#md5=...) hashes
            downloaded from the internet, as by populate_link()

        
Format a nice indicator to show where this "comes from" 
Set requirement after generating metadata.
Find an installed distribution that satisfies or conflicts
        with this requirement, and set self.satisfied_by or
        self.should_reinstall appropriately.
        
Load the pyproject.toml file.

        After calling this routine, all of the attributes related to PEP 517
        processing for this requirement have been set. In particular, the
        use_pep517 attribute can be used to determine whether we should
        follow the PEP 517 or legacy (setup.py) code path.
        
Check that an editable requirement if valid for use with PEP 517/518.

        This verifies that an editable that has a pyproject.toml either supports PEP 660
        or as a setup.py or a setup.cfg
        
Ensure that project metadata is available.

        Under PEP 517 and PEP 660, call the backend hook to prepare the metadata.
        Under legacy processing, call setup.py egg-info.
        
Ensure that a source_dir is set.

        This will create a temporary build dir if the name of the requirement
        isn't known yet.

        :param parent_dir: The ideal pip parent_dir for the source_dir.
            Generally src_dir for editables and build_dir for sdists.
        :return: self.source_dir
        
Ensure the source directory has not yet been built in.

        Uninstall the distribution currently satisfying this requirement.

        Prompts before removing or modifying files unless
        ``auto_confirm`` is True.

        Refuses to delete or modify files outside of ``sys.prefix`` -
        thus uninstallation within a virtual environment can only
        modify that virtual environment, even if the virtualenv is
        linked to global site-packages.

        
Saves archive to provided build_dir.

        Used for saving downloaded VCS requirements as part of `pip download`.
        

---


Requirements file parsing

Parse a requirements file and yield ParsedRequirement instances.

    :param filename:    Path or url of requirements file.
    :param session:     PipSession instance.
    :param finder:      Instance of pip.index.PackageFinder.
    :param options:     cli options.
    :param constraint:  If true, parsing a constraint file rather than
        requirements file.
    
Split, filter, and join lines, and return a line iterator

    :param content: the content of the requirements file
    
Handle a single parsed requirements line; This can result in
    creating/yielding requirements, or updating the finder.

    :param line:        The parsed line to be processed.
    :param options:     CLI options.
    :param finder:      The finder - updated by non-requirement lines.
    :param session:     The session - updated by non-requirement lines.

    Returns a ParsedRequirement object if the line is a requirement line,
    otherwise returns None.

    For lines that contain requirements, the only options that have an effect
    are from SUPPORTED_OPTIONS_REQ, and they are scoped to the
    requirement. Other options from SUPPORTED_OPTIONS may be present, but are
    ignored.

    For lines that do not contain requirements, the only options that have an
    effect are from SUPPORTED_OPTIONS. Options from SUPPORTED_OPTIONS_REQ may
    be present, but are ignored. These lines may contain multiple options
    (although our docs imply only one is supported), and all our parsed and
    affect the finder.
    
Parse a given file, yielding parsed lines.
Break up the line into an args and options string.  We only want to shlex
    (and then optparse) the options, not the args.  args can contain markers
    which are corrupted by shlex.
    

    Return a parser for parsing requirement lines
    
Joins a line ending in '\' with the previous line (except when following
    comments).  The joined line takes on the index of the first line.
    

    Strips comments and filter empty lines.
    
Replace all environment variables that can be retrieved via `os.getenv`.

    The only allowed format for environment variables defined in the
    requirement file is `${MY_VARIABLE_1}` to ensure two things:

    1. Strings that contain a `$` aren't accidentally (partially) expanded.
    2. Ensure consistency across platforms for requirement files.

    These points are the result of a discussion on the `github pull
    request #3514 <https://github.com/pypa/pip/pull/3514>`_.

    Valid characters in variable names follow the `POSIX standard
    <http://pubs.opengroup.org/onlinepubs/9699919799/>`_ and are limited
    to uppercase letter, digits and the `_` (underscore).
    
Gets the content of a file; it may be a filename, file: URL, or
    http: URL.  Returns (location, content).  Content is unicode.
    Respects # -*- coding: declarations on the retrieved files.

    :param url:         File path or url.
    :param session:     PipSession instance.
    

---


    Install everything in the given list.

    (to be called after having downloaded and unpacked the packages)
    

---

Validation of dependencies of packages
Converts a list of distributions into a PackageSet.
Check if a package set is consistent

    If should_ignore is passed, it should be a callable that takes a
    package name and returns a boolean.
    
For checking if the dependency graph would be consistent after \
    installing given requirements
    
Computes the version of packages after installing to_install.

---

Prepares a distribution for installation
Prepare a distribution for installation.
Get file and optionally check its hash.
Unpack link into location, downloading if required.

    :param hashes: A Hashes object, one of whose embedded hashes must match,
        or HashMismatch will be raised. If the Hashes is empty, no matches are
        required, and unhashable types of requirements (like VCS ones, which
        would ordinarily raise HashUnsupported) are allowed.
    
Check download_dir for previously downloaded file with correct hash
    If a correct file is found return its path else None
    
Prepares a Requirement
Provide context for the requirement being prepared.
Ensure source_dir of a linked InstallRequirement.
Fetch metadata from the data-dist-info-metadata attribute, if possible.
Fetch metadata using lazy wheel, if possible.
Download any requirements which were only fetched by metadata.
Prepare a requirement to be obtained from req.link.
Prepare linked requirements more, if needed.
Prepare an editable requirement.
Prepare an already-installed requirement.

---



---


    Compute and return values (req, comments) for use in
    FrozenRequirement.from_dist().
    

---

Support for installing and building the "wheel" binary package format.
Return (encoded_digest, length) for path using hashlib.sha256()
Return keyword arguments to properly open a CSV file
    in the given mode.
    
Replace #!python with #!/path/to/python
    Return True if file was changed.
    
Determine if any scripts are not on PATH and format a warning.
    Returns a warning message if one or more scripts are not on PATH,
    otherwise None.
    
Normalize the given rows of a RECORD file.

    Items in each row are converted into str. Rows are then sorted to make
    the value more predictable for tests.

    Each row is a 3-tuple (path, hash, size) and corresponds to a record of
    a RECORD file (see PEP 376 and PEP 427 for details).  For the rows
    passed to this function, the size can be an integer as an int or string,
    or the empty string.
    

    :param installed: A map from archive RECORD path to installation RECORD
        path.
    

    Given the mapping from entrypoint name to callable, return the relevant
    console script specs.
    
Install a wheel.

    :param name: Name of the project to install
    :param wheel_zip: open ZipFile for wheel being installed
    :param scheme: Distutils scheme dictating the install directories
    :param req_description: String used in place of the requirement, for
        logging
    :param pycompile: Whether to byte-compile installed Python files
    :param warn_script_location: Whether to check that scripts are installed
        into a directory on PATH
    :raises UnsupportedWheel:
        * when the directory holds an unpacked wheel with incompatible
          Wheel-Version
        * when the .dist-info dir does not match the wheel
    
Map archive RECORD paths to installation RECORD paths.
Return the path the pyc file would have been written to.

---

For modules related to installing packages.

---

Legacy editable installation process, i.e. `setup.py develop`.
Install a package in editable mode. Most arguments are pass-through
    to setuptools.
    

---

Build one InstallRequirement using the PEP 660 build process.

    Returns path to wheel if successfully built. Otherwise, returns None.
    

---

Metadata generation logic for legacy source distributions.
Find an .egg-info subdirectory in `directory`.
Generate metadata using setup.py-based defacto mechanisms.

    Returns the generated metadata directory.
    

---

Metadata generation logic for source distributions.
Generate metadata using mechanisms described in PEP 517.

    Returns the generated metadata directory.
    

---

Metadata generation logic for source distributions.
Generate metadata using mechanisms described in PEP 660.

    Returns the generated metadata directory.
    

---

Uniquely identifying string provided to the build tracker.
Ensure that an sdist cannot request itself as a setup requirement.

    When an sdist is prepared, it identifies its setup requirements in the
    context of ``BuildTracker.track()``. If a requirement shows up recursively, this
    raises an exception.

    This stops fork bombs embedded in malicious packages.
Add an InstallRequirement to build tracking.
Remove an InstallRequirement from build tracking.
Ensure that `key` cannot install itself as a setup requirement.

        :raises LookupError: If `key` was already provided in a parent invocation of
                             the context introduced by this method.

---

Build one InstallRequirement using the PEP 517 build process.

    Returns path to wheel if successfully built. Otherwise, returns None.
    

---



---

Format command information for logging.
Return the path to the wheel in the temporary build directory.
Build one unpacked package using the "legacy" build process.

    Returns path to wheel if successfully built. Otherwise, returns None.
    

---

Convert a legacy installed-files.txt path into modern RECORD path.

    The legacy format stores paths relative to the info directory, while the
    modern format stores paths relative to the package root, e.g. the
    site-packages directory.

    :param entry: Path parts of the installed-files.txt entry.
    :param info: Path parts of the egg-info directory relative to package root.
    :returns: The converted entry.

    For best compatibility with symlinks, this does not use ``abspath()`` or
    ``Path.resolve()``, but tries to work with path parts:

    1. While ``entry`` starts with ``..``, remove the equal amounts of parts
       from ``info``; if ``info`` is empty, start appending ``..`` instead.
    2. Join the two directly.
    
Load the distribution from a metadata directory.

        :param directory: Path to a metadata directory, e.g. ``.dist-info``.
        
Load the distribution from the contents of a METADATA file.

        This is used to implement PEP 658 by generating a "shallow" dist object that can
        be used for resolution without downloading or building the actual dist yet.

        :param metadata_contents: The contents of a METADATA file.
        :param filename: File name for the dist with this metadata.
        :param project_name: Name of the project this dist represents.
        
Load the distribution from a given wheel.

        :param wheel: A concrete wheel definition.
        :param name: File name of the wheel.

        :raises InvalidWheel: Whenever loading of the wheel causes a
            :py:exc:`zipfile.BadZipFile` exception to be thrown.
        :raises UnsupportedWheel: If the wheel is a valid zip, but malformed
            internally.
        
Where the distribution is loaded from.

        A string value is not necessarily a filesystem path, since distributions
        can be loaded from other sources, e.g. arbitrary zip archives. ``None``
        means the distribution is created in-memory.

        Do not canonicalize this value with e.g. ``pathlib.Path.resolve()``. If
        this is a symbolic link, we want to preserve the relative path between
        it and files in the distribution.
        
The project location for editable distributions.

        This is the directory where pyproject.toml or setup.py is located.
        None if the distribution is not installed in editable mode.
        
The distribution's "installed" location.

        This should generally be a ``site-packages`` directory. This is
        usually ``dist.location``, except for legacy develop-installed packages,
        where ``dist.location`` is the source code location, and this is where
        the ``.egg-link`` file is.

        The returned location is normalized (in particular, with symlinks removed).
        
Location of the .[egg|dist]-info directory or file.

        Similarly to ``location``, a string value is not necessarily a
        filesystem path. ``None`` means the distribution is created in-memory.

        For a modern .dist-info installation on disk, this should be something
        like ``{location}/{raw_name}-{version}.dist-info``.

        Do not canonicalize this value with e.g. ``pathlib.Path.resolve()``. If
        this is a symbolic link, we want to preserve the relative path between
        it and other files in the distribution.
        
Whether this distribution is installed with legacy distutils format.

        A distribution installed with "raw" distutils not patched by setuptools
        uses one single file at ``info_location`` to store metadata. We need to
        treat this specially on uninstallation.
        
Whether this distribution is installed as an egg.

        This usually indicates the distribution was installed by (older versions
        of) easy_install.
        
Whether this distribution is installed with the ``.egg-info`` format.

        This usually indicates the distribution was installed with setuptools
        with an old pip version or with ``single-version-externally-managed``.

        Note that this ensure the metadata store is a directory. distutils can
        also installs an ``.egg-info``, but as a file, not a directory. This
        property is *False* for that case. Also see ``installed_by_distutils``.
        
Whether this distribution is installed with the "modern format".

        This indicates a "modern" installation, e.g. storing metadata in the
        ``.dist-info`` directory. This applies to installations made by
        setuptools (but through pip, not directly), or anything using the
        standardized build backend interface (PEP 517).
        
Convert a project name to its setuptools-compatible filename.

        This is a copy of ``pkg_resources.to_filename()`` for compatibility.
        
Obtain a DirectUrl from this distribution.

        Returns None if the distribution has no `direct_url.json` metadata,
        or if `direct_url.json` is invalid.
        
If distribution is installed in the current virtual environment.

        Always True if we're not in a virtualenv.
        
Check whether an entry in the info directory is a file.
Find distutils 'scripts' entries metadata.

        If 'scripts' is supplied in ``setup.py``, distutils records those in the
        installed distribution's ``scripts`` directory, a file for each script.
        
Read a file in the info directory.

        :raise FileNotFoundError: If ``path`` does not exist in the directory.
        :raise NoneMetadataError: If ``path`` exists in the info directory, but
            cannot be read.
        
Metadata of distribution parsed from e.g. METADATA or PKG-INFO.

        This should return an empty message if the metadata file is unavailable.

        :raises NoneMetadataError: If the metadata file is available, but does
            not contain valid metadata.
        
PEP 566 compliant JSON-serializable representation of METADATA or PKG-INFO.

        This should return an empty dict if the metadata file is unavailable.

        :raises NoneMetadataError: If the metadata file is available, but does
            not contain valid metadata.
        
Value of "Metadata-Version:" in distribution metadata, if available.
Value of "Name:" in distribution metadata.
Value of "Requires-Python:" in distribution metadata.

        If the key does not exist or contains an invalid value, an empty
        SpecifierSet should be returned.
        
Dependencies of this distribution.

        For modern .dist-info distributions, this is the collection of
        "Requires-Dist:" entries in distribution metadata.
        
Raw Requires-Dist metadata.
Extras provided by this distribution.

        For modern .dist-info distributions, this is the collection of
        "Provides-Extra:" entries in distribution metadata.

        The return value of this function is expected to be normalised names,
        per PEP 685, with the returned value being handled appropriately by
        `iter_dependencies`.
        
Iterate through file entries declared in this distribution.

        For modern .dist-info distributions, this is the files listed in the
        ``RECORD`` metadata file. For legacy setuptools distributions, this
        comes from ``installed-files.txt``, with entries normalized to be
        compatible with the format used by ``RECORD``.

        :return: An iterator for listed entries, or None if the distribution
            contains neither ``RECORD`` nor ``installed-files.txt``.
        
Parse a ``requires.txt`` in an egg-info directory.

        This is an INI-ish format where an egg-info stores dependencies. A
        section name describes extra other environment markers, while each entry
        is an arbitrary string (not a key-value pair) representing a dependency
        as a requirement string (no markers).

        There is a construct in ``importlib.metadata`` called ``Sectioned`` that
        does mostly the same, but the format is currently considered private.
        
Get extras from the egg-info directory.
Get distribution dependencies from the egg-info directory.

        To ease parsing, this converts a legacy dependency entry into a PEP 508
        requirement string. Like ``_iter_requires_txt_entries()``, there is code
        in ``importlib.metadata`` that does mostly the same, but not do exactly
        what we need.

        Namely, ``importlib.metadata`` does not normalize the extra name before
        putting it into the requirement string, which causes marker comparison
        to fail because the dist-info format do normalize. This is consistent in
        all currently available PEP 517 backends, although not standardized.
        
Add egg-info requires.txt information to the metadata.
An environment containing distributions to introspect.
Given a requirement name, return the installed distributions.

        The name may not be normalized. The implementation must canonicalize
        it for lookup.
        
Iterate through installed distributions.

        This function should be implemented by subclass, but never called
        directly. Use the public ``iter_distribution()`` instead, which
        implements additional logic to make sure the distributions are valid.
        
Iterate through all installed distributions without any filtering.
Return a list of installed distributions.

        This is based on ``iter_all_distributions()`` with additional filtering
        options. Note that ``iter_installed_distributions()`` without arguments
        is *not* equal to ``iter_all_distributions()``, since some of the
        configurations exclude packages by default.

        :param local_only: If True (default), only return installations
        local to the current virtualenv, if in a virtualenv.
        :param skip: An iterable of canonicalized project names to ignore;
            defaults to ``stdlib_pkgs``.
        :param include_editables: If False, don't report editables.
        :param editables_only: If True, only report editables.
        :param user_only: If True, only report installations in the user
        site directory.
        

---

Convert a Message object into a JSON-compatible dictionary.

---

IMetadataProvider that reads metadata files from a dictionary.

    This also maps metadata decoding exceptions to our internal exception type.
    

        :raises NoneMetadataError: if the distribution reports `has_metadata()`
            True but `get_metadata()` returns None.
        
Find a distribution matching the ``name`` in the environment.

        This searches from *all* distributions available in the environment, to
        match the behavior of ``pkg_resources.get_distribution()``.
        

---

Whether to use the ``importlib.metadata`` or ``pkg_resources`` backend.

    By default, pip uses ``importlib.metadata`` on Python 3.11+, and
    ``pkg_resources`` otherwise. Up to Python 3.13, This can be
    overridden by a couple of ways:

    * If environment variable ``_PIP_USE_IMPORTLIB_METADATA`` is set, it
      dictates whether ``importlib.metadata`` is used, for Python <3.14.
    * On Python 3.11, 3.12 and 3.13, Python distributors can patch
      ``importlib.metadata`` to add a global constant
      ``_PIP_USE_IMPORTLIB_METADATA = False``. This makes pip use
      ``pkg_resources`` (unless the user set the aforementioned environment
      variable to *True*).

    On Python 3.14+, the ``pkg_resources`` backend cannot be used.
    
Get the default representation for the current environment.

    This returns an Environment instance from the chosen backend. The default
    Environment instance should be built from ``sys.path`` and may use caching
    to share instance state across calls.
    
Get a representation of the environment specified by ``paths``.

    This returns an Environment instance from the chosen backend based on the
    given import paths. The backend must build a fresh instance representing
    the state of installed distributions when this function is called.
    
Get the distribution metadata representation in the specified directory.

    This returns a Distribution instance from the chosen backend based on
    the given on-disk ``.dist-info`` directory.
    
Get the representation of the specified wheel's distribution metadata.

    This returns a Distribution instance from the chosen backend based on
    the given wheel's ``.dist-info`` directory.

    :param canonical_name: Normalized project name of the given wheel.
    
Get the dist representation of the specified METADATA file contents.

    This returns a Distribution instance from the chosen backend sourced from the data
    in `metadata_contents`.

    :param metadata_contents: Contents of a METADATA file within a dist, or one served
                              via PEP 658.
    :param filename: Filename for the dist this metadata represents.
    :param canonical_name: Normalized project name of the given dist.
    

---

A protocol that various path objects conform.

    This exists because importlib.metadata uses both ``pathlib.Path`` and
    ``zipfile.Path``, and we need a common base for type hints (Union does not
    work well since ``zipfile.Path`` is too new for our linter setup).

    This does not mean to be exhaustive, but only contains things that present
    in both classes *that we need*.
    
Find the path to the distribution's metadata directory.

    HACK: This relies on importlib.metadata's private ``_path`` attribute. Not
    all distributions exist on disk, so importlib.metadata is correct to not
    expose the attribute as public. But pip's code base is old and not as clean,
    so we do this to avoid having to rewrite too many things. Hopefully we can
    eliminate this some day.
    
Get a name and version from the metadata directory name.

    This is much faster than reading distribution metadata.
    
Get the distribution's normalized name.

    The ``name`` attribute is only available in Python 3.10 or later. We are
    targeting exactly that, but Mypy does not know this.
    

---

An ``importlib.metadata.Distribution`` read from a wheel.

    Although ``importlib.metadata.PathDistribution`` accepts ``zipfile.Path``,
    its implementation is too "lazy" for pip's needs (we can't keep the ZipFile
    handle open for the entire lifetime of the distribution object).

    This implementation eagerly reads the entire metadata directory into the
    memory instead, and operates from that.
    

---



---

Finder to locate distributions.

    The main purpose of this class is to memoize found distributions' names, so
    only one distribution is returned for each package name. At lot of pip code
    assumes this (because it is setuptools's behavior), and not doing the same
    can potentially cause a distribution in lower precedence path to override a
    higher precedence one if the caller is not careful.

    Eventually we probably want to make it possible to see lower precedence
    installations as well. It's useful feature, after all.
    
Find distributions in a location.
Find distributions in a location.

        The path can be either a directory, or a ZIP archive.
        
Read location in egg-link files and return distributions in there.

        The path should be a directory; otherwise this returns nothing. This
        follows how setuptools does this for compatibility. The first non-empty
        line in the egg-link is read as a path (resolved against the egg-link's
        containing directory if relative). Distributions found at that linked
        location are returned.
        

---


    Return the major-minor version of the current Python as a string, e.g.
    "3.7" or "3.10".
    
Return 'pathname' with 'new_root' prepended.

    If 'pathname' is relative, this is equivalent to os.path.join(new_root, pathname).
    Otherwise, it requires making 'pathname' relative and then joining the
    two, which is tricky on DOS/Windows and Mac OS.

    This is borrowed from Python's standard library's distutils module.
    

---

Check for Apple's ``osx_framework_library`` scheme.

    Python distributed by Apple's Command Line Tools has this special scheme
    that's used when:

    * This is a framework build.
    * We are installing into the system prefix.

    This does not account for ``pip install --prefix`` (also means we're not
    installing to the system prefix), which should use ``posix_prefix``, but
    logic here means ``_infer_prefix()`` outputs ``osx_framework_library``. But
    since ``prefix`` is not available for ``sysconfig.get_default_scheme()``,
    which is the stdlib replacement for ``_infer_prefix()``, presumably Apple
    wouldn't be able to magically switch between ``osx_framework_library`` and
    ``posix_prefix``. ``_infer_prefix()`` returning ``osx_framework_library``
    means its behavior is consistent whether we use the stdlib implementation
    or our own, and we deal with this special case in ``get_scheme()`` instead.
    
Try to find a prefix scheme for the current platform.

    This tries:

    * A special ``osx_framework_library`` for Python distributed by Apple's
      Command Line Tools, when not running in a virtual environment.
    * Implementation + OS, used by PyPy on Windows (``pypy_nt``).
    * Implementation without OS, used by PyPy on POSIX (``pypy``).
    * OS + "prefix", used by CPython on POSIX (``posix_prefix``).
    * Just the OS name, used by CPython on Windows (``nt``).

    If none of the above works, fall back to ``posix_prefix``.
    
Try to find a user scheme for the current platform.
Try to find a home for the current platform.

    Get the "scheme" corresponding to the input parameters.

    :param dist_name: the name of the package to retrieve the scheme for, used
        in the headers scheme path
    :param user: indicates to use the "user" scheme
    :param home: indicates to use the "home" scheme
    :param root: root under which other directories are re-based
    :param isolated: ignored, but kept for distutils compatibility (where
        this controls whether the user-site pydistutils.cfg is honored)
    :param prefix: indicates to use the "prefix" scheme and provides the
        base directory for the same
    

---

Locations where we look for configs, install stuff, etc

    Return a distutils install scheme
    

    Get the "scheme" corresponding to the input parameters. The distutils
    documentation provides the context for the available schemes:
    https://docs.python.org/3/install/index.html#alternate-installation

    :param dist_name: the name of the package to retrieve the scheme for, used
        in the headers scheme path
    :param user: indicates to use the "user" scheme
    :param home: indicates to use the "home" scheme and provides the base
        directory for the same
    :param root: root under which other directories are re-based
    :param isolated: equivalent to --no-user-cfg, i.e. do not consider
        ~/.pydistutils.cfg (posix) or ~/pydistutils.cfg (non-posix) for
        scheme paths
    :param prefix: indicates to use the "prefix" scheme and provides the
        base directory for the same
    

---

This function determines the value of _USE_SYSCONFIG.

    By default, pip uses sysconfig on Python 3.10+.
    But Python distributors can override this decision by setting:
        sysconfig._PIP_USE_SYSCONFIG = True / False
    Rationale in https://github.com/pypa/pip/issues/10647

    This is a function for testability, but should be constant during any one
    run.
    
The resolution to bpo-44860 will change this incorrect platlib.

    See <https://bugs.python.org/issue44860>.
    
Red Hat patches platlib in unix_prefix and unix_home, but not purelib.

    This is the only way I can see to tell a Red Hat-patched Python.
    
Debian adds two additional schemes.
Red Hat patches ``sys.prefix`` and ``sys.exec_prefix``.

    Red Hat's ``00251-change-user-install-location.patch`` changes the install
    command's ``prefix`` and ``exec_prefix`` to append ``"/local"``. This is
    (fortunately?) done quite unconditionally, so we create a default command
    object without any configuration to detect this.
    
Slackware patches sysconfig but fails to patch distutils and site.

    Slackware changes sysconfig's user scheme to use ``"lib64"`` for the lib
    path, but does not do the same to the site module.
    
MSYS2 patches distutils and sysconfig to use a UNIX-like scheme.

    However, MSYS2 incorrectly patches sysconfig ``nt`` scheme. The fix is
    likely going to be included in their 3.10 release, so we ignore the warning.
    See msys2/MINGW-packages#9319.

    MSYS2 MINGW's patch uses lowercase ``"lib"`` instead of the usual uppercase,
    and is missing the final ``"site-packages"``.
    
Check if the value is Debian's APT-controlled dist-packages.

    Debian's ``distutils.sysconfig.get_python_lib()`` implementation returns the
    default package path controlled by APT, but does not patch ``sysconfig`` to
    do the same. This is similar to the bug worked around in ``get_scheme()``,
    but here the default is ``deb_system`` instead of ``unix_local``. Ultimately
    we can't do anything about this Debian bug, and this detection allows us to
    skip the warning when needed.
    
Return the default pure-Python lib location.
Return the default platform-shared lib location.

---

Filetype information.
Return True if `name` is a considered as an archive file.

---

A wrapper that builds multiple hashes at once and checks them against
    known-good values

    

        :param hashes: A dict of algorithm names pointing to lists of allowed
            hex digests
        
Return whether the given hex digest is allowed.
Check good hashes against ones built from iterable of chunks of
        data.

        Raise HashMismatch if none match.

        
Check good hashes against a file-like object

        Raise HashMismatch if none match.

        
Return whether any of the given hashes are allowed.
Return whether I know any known-good hashes.
A workalike for Hashes used when we're missing a hash for a requirement

    It computes the actual hash of the requirement and raises a HashMissing
    exception showing it to the user.

    
Don't offer the ``hashes`` kwarg.

---

Checks if sys.base_prefix and sys.prefix match.

    This handles PEP 405 compliant virtual environments.
    
Checks if sys.real_prefix is set.

    This handles virtual environments created with pypa's virtualenv.
    
True if we're running inside a virtual environment, False otherwise.
Reads {sys.prefix}/pyvenv.cfg and returns its contents as list of lines

    Returns None, if it could not read/access the file.
    
Check `{sys.prefix}/pyvenv.cfg` for system site-packages inclusion

    PEP 405 specifies that when system site-packages are not supposed to be
    visible from a virtual environment, `pyvenv.cfg` must contain the following
    line:

        include-system-site-packages = false

    Additionally, log a warning if accessing the file fails.
    
Check if "no-global-site-packages.txt" exists beside site.py

    This mirrors logic in pypa/virtualenv for determining whether system
    site-packages are visible in the virtual environment.
    
Returns a boolean, whether running in venv with no system site-packages.

---

Try to determine the glibc version

    Returns a tuple of strings (lib, version) which default to empty strings
    in case the lookup fails.
    

---

Manages temp directory behavior
Indicate whether a TempDirectory of the given kind should be
        auto-deleted.
        
Get configured auto-delete flag for a given TempDirectory type,
        default True.
        
Provides a scoped global tempdir registry that can be used to dictate
    whether directories should be deleted.
    
Helper class that owns and cleans up a temporary directory.

    This class can be used as a context manager or as an OO representation of a
    temporary directory.

    Attributes:
        path
            Location to the created temporary directory
        delete
            Whether the directory should be deleted when exiting
            (when used as a contextmanager)

    Methods:
        cleanup()
            Deletes the temporary directory

    When used as a context manager, if the delete attribute is True, on
    exiting the context the temporary directory is deleted.
    
Create a temporary directory and store its path in self.path
Remove the temporary directory created and reset state
Log a warning for a `rmtree` error and continue
Helper class that creates a temporary directory adjacent to a real one.

    Attributes:
        original
            The original directory to create a temp directory for.
        path
            After calling create() or entering, contains the full
            path to the temporary directory.
        delete
            Whether the directory should be deleted when exiting
            (when used as a contextmanager)

    
Generates a series of temporary names.

        The algorithm replaces the leading characters in the name
        with ones that are valid filesystem characters, but are not
        valid package names (for both Python and pip definitions of
        package).
        

---


    Convert a tuple of ints representing a Python version to one of length
    three.

    :param py_version_info: a tuple of ints representing a Python version,
        or None to specify no version. The tuple can have any length.

    :return: a tuple of length three if `py_version_info` is non-None.
        Otherwise, return `py_version_info` unchanged (i.e. None).
    
os.path.makedirs without EEXIST.

    `rmtree` error handler to 'force' a file remove (i.e. like `rm -f`).

    * If a file is readonly then it's write flag is set and operation is
      retried.

    * `onerror` is the original callback from `rmtree(... onerror=onerror)`
      that is chained at the end if the "rm -f" still fails.
    
Gives the display value for a given path, making it relative to cwd
    if possible.
Figure out the name of a directory to back up the given dir to
    (adding .bak, .bak2, etc)
Raise an error if no input is allowed.
Ask the message interactively, with the given possible responses
Ask for input interactively.
Ask for a password interactively.
Convert a string representation of truth to true (1) or false (0).

    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    
Return a list of formatted rows and a list of column sizes.

    For example::

    >>> tabulate([['foobar', 2000], [0xdeadbeef]])
    (['foobar     2000', '3735928559'], [10, 4])
    
Is path is a directory containing pyproject.toml or setup.py?

    If pyproject.toml exists, this is a PEP 517 project. Otherwise we look for
    a legacy setuptools layout by identifying setup.py. We don't check for the
    setup.cfg because using it without setup.py is only available for PEP 517
    projects, which are already covered by the pyproject.toml check.
    
Yield pieces of data from a file-like object until EOF.

    Convert a path to its canonical, case-normalized, absolute version.

    
Like os.path.splitext, but take off .tar too
Like os.renames(), but handles renaming across devices.

    Return True if path is within sys.prefix, if we're running in a virtualenv.

    If we're not in a virtualenv, all paths are considered "local."

    Caution: this function assumes the head of path has been normalized
    with normalize_path.
    

    Build a netloc from a host-port pair
    

    Build a full URL from a netloc.
    

    Return the host-port pair from a netloc.
    

    Parse out and remove the auth information from a netloc.

    Returns: (netloc, (username, password)).
    

    Replace the sensitive data in a netloc with "****", if it exists.

    For example:
        - "user:pass@example.com" returns "user:****@example.com"
        - "accesstoken@example.com" returns "****@example.com"
    
Transform and replace netloc in a url.

    transform_netloc is a function taking the netloc and returning a
    tuple. The first element of this tuple is the new netloc. The
    entire tuple is returned.

    Returns a tuple containing the transformed url as item 0 and the
    original tuple returned by transform_netloc as item 1.
    

    Parse a url into separate netloc, auth, and url with no auth.

    Returns: (url_without_auth, netloc, (username, password))
    
Return a copy of url with 'username:password@' removed.
Replace the password in a given url with ****.
Replace the password in a given requirement url with ****.
Protection of pip.exe from modification on Windows

    On Windows, any operation modifying pip should be run as:
        python -m pip ...
    
Check whether the current environment is externally managed.

    If the ``EXTERNALLY-MANAGED`` config file is found, the current environment
    is considered externally managed, and an ExternallyManagedEnvironment is
    raised.
    
Is this console interactive?
Return (hash, length) for path using hashlib.sha256()

    Return paired elements.

    For example:
        s -> (s0, s1), (s2, s3), (s4, s5), ...
    

    Use a predicate to partition entries into false entries and true entries,
    like

        partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    
Output a warning for sudo users on Unix.

    In a virtual environment, sudo pip still writes to virtualenv.
    On Windows, users may run pip as Administrator without issues.
    This warning only applies to Unix root users outside of virtualenv.
    

---

Generate and work with PEP 425 Compatibility Tags.
Return a list of supported tags for each version specified in
    `versions`.

    :param version: a string version, of the form "33" or "32",
        or None. The version will be assumed to support our ABI.
    :param platform: specify a list of platforms you want valid
        tags for, or None. If None, use the local system platform.
    :param impl: specify the exact implementation you want valid
        tags for, or None. If None, use the local interpreter impl.
    :param abis: specify a list of abis you want valid
        tags for, or None. If None, use the local interpreter abi.
    

---


    Create a CommandArgs object.
    

    Format command arguments for display.
    

    Return the arguments in their raw, unredacted form.
    

    Args:
      show_stdout: if true, use INFO to log the subprocess's stderr and
        stdout streams.  Otherwise, use DEBUG.  Defaults to False.
      extra_ok_returncodes: an iterable of integer return codes that are
        acceptable, in addition to 0. Defaults to None, which means [].
      unset_environ: an iterable of environment variable names to unset
        prior to calling subprocess.Popen().
      log_failed_cmd: if false, failed commands are not logged, only raised.
      stdout_only: if true, return only stdout, else return both. When true,
        logging of both stdout and stderr occurs when the subprocess has
        terminated, else logging occurs as subprocess output is produced.
    
Provide a subprocess_runner that shows a spinner message.

    Intended for use with for BuildBackendHookCaller. Thus, the runner has
    an API that matches what's expected by BuildBackendHookCaller.subprocess_runner.
    

---

Central wrapper for all old entrypoints.

    Historically pip has had several entrypoints defined. Because of issues
    arising from PATH, sys.path, multiple Pythons, their interactions, and most
    of them having a pip installed, users suffer every time an entrypoint gets
    moved.

    To alleviate this pain, and provide a mechanism for warning users and
    directing them to an appropriate place for help, we now define all of
    our old entrypoints as wrappers for the current one.
    
Try to figure out the best way to invoke pip in the current environment.
Try to figure out the best way to invoke the current Python.

---


This code wraps the vendored appdirs module to so the return values are
compatible for the current pip code base.

The intention is to rewrite current usages gradually, keeping the tests pass,
and eventually drop this after all usages are changed.


---


    Convert a path to a file: URL.  The path will be made absolute and have
    quoted path parts.
    

    Convert a file: URL to a path.
    

---


    exec(compile('''
    # This is <pip-setuptools-caller> -- a caller that pip uses to run setup.py
    #
    # - It imports setuptools before invoking setup.py, to enable projects that directly
    #   import from `distutils.core` to work with newer packaging standards.
    # - It provides a clear error message when setuptools is not installed.
    # - It sets `sys.argv[0]` to the underlying `setup.py`, when invoking `setup.py` so
    #   setuptools doesn't think the script is `-c`. This avoids the following warning:
    #     manifest_maker: standard file '-c' not found".
    # - It generates a shim setup.py, for handling setup.cfg-only projects.
    import os, sys, tokenize, traceback

    try:
        import setuptools
    except ImportError:
        print(
            "ERROR: Can not execute `setup.py` since setuptools failed to import in "
            "the build environment with exception:",
            file=sys.stderr,
        )
        traceback.print_exc()
        sys.exit(1)

    __file__ = %r
    sys.argv[0] = __file__

    if os.path.exists(__file__):
        filename = __file__
        with tokenize.open(__file__) as f:
            setup_py_code = f.read()
    else:
        filename = "<auto-generated setuptools caller>"
        setup_py_code = "from setuptools import setup; setup()"

    exec(compile(setup_py_code, filename, "exec"))
    ''' % ({!r},), "<pip-setuptools-caller>", "exec"))
    

    Get setuptools command arguments with shim wrapped setup file invocation.

    :param setup_py_path: The path to setup.py to be wrapped.
    :param global_options: Additional global options.
    :param no_user_config: If True, disables personal user configuration.
    :param unbuffered_output: If True, adds the unbuffered switch to the
     argument list.
    

---

Customize logging

Defines custom logger class for the `logger.verbose(...)` method.

init_logging() must be called before any other modules that call logging.getLogger.

Custom Logger, defining a verbose log-level

    VERBOSE is between INFO and DEBUG.
    
logging.getLogger, but ensures our VerboseLogger class is returned
Register our VerboseLogger and VERBOSE log level.

    Should be called before any calls to getLogger(),
    i.e. in pip._internal.__init__
    

---


    Raised if BrokenPipeError occurs for the stdout stream while logging.
    

    A context manager which will cause the log output to be indented for any
    log messages emitted inside it.
    

        A logging.Formatter that obeys the indent_log() context manager.

        :param add_timestamp: A bool indicating output lines should be prefixed
            with their record's timestamp.
        

        Return the start of the formatted log message (not counting the
        prefix to add to each line).
        

        Calls the standard formatter, but will indent all of the log message
        lines by our current indentation level.
        
Called when logging is unable to log some output.

    A logging Filter that excludes records from a logger (or its children).
    
Configures and sets up all of the logging

    Returns the requested logging level, as its integer value.
    

---

Convert a DirectUrl to a pip requirement string.

---

Return a file-like object pointing to a tmp file next to path.

    The file is created securely and is ensured to be written to disk
    after the context reaches its end.

    kwargs will be passed to tempfile.NamedTemporaryFile to control
    the way the temporary file will be opened.
    
Check if a directory is writable.

    Uses os.access() on POSIX, tries creating files on Windows.
    
Returns a list of absolute paths of files beneath path, recursively,
    with filenames which match the UNIX-style shell glob pattern.

---


A module that implements tooling to enable easy warnings about deprecations.

Helper to deprecate existing functionality.

    reason:
        Textual reason shown to the user about why this functionality has
        been deprecated. Should be a complete sentence.
    replacement:
        Textual suggestion shown to the user about what alternative
        functionality they can use.
    gone_in:
        The version of pip does this functionality should get removed in.
        Raises an error if pip's current version is greater than or equal to
        this.
    feature_flag:
        Command-line flag of the form --use-feature={feature_flag} for testing
        upcoming functionality.
    issue:
        Issue number on the tracker that would serve as a useful place for
        users to find related discussion and provide feedback.
    

---

Functions brought over from jaraco.text.

These functions are not supposed to be used within `pip._internal`. These are
helper functions brought over from `jaraco.text` to enable vendoring newer
copies of `pkg_resources` without having to vendor `jaraco.text` and its entire
dependency cone; something that our vendoring setup is not currently capable of
handling.

License reproduced from original source below:

Copyright Jason R. Coombs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.


    Yield valid lines of a string or iterable.

    >>> list(yield_lines(''))
    []
    >>> list(yield_lines(['foo', 'bar']))
    ['foo', 'bar']
    >>> list(yield_lines('foo\nbar'))
    ['foo', 'bar']
    >>> list(yield_lines('\nfoo\n#bar\nbaz #comment'))
    ['foo', 'baz #comment']
    >>> list(yield_lines(['foo\nbar', 'baz', 'bing\n\n\n']))
    ['foo', 'bar', 'baz', 'bing']
    

    Drop comments.

    >>> drop_comment('foo # bar')
    'foo'

    A hash without a space may be in a URL.

    >>> drop_comment('http://example.com/foo#bar')
    'http://example.com/foo#bar'
    

    Join lines continued by a trailing backslash.

    >>> list(join_continuation(['foo \\', 'bar', 'baz']))
    ['foobar', 'baz']
    >>> list(join_continuation(['foo \\', 'bar', 'baz']))
    ['foobar', 'baz']
    >>> list(join_continuation(['foo \\', 'bar \\', 'baz']))
    ['foobarbaz']

    Not sure why, but...
    The character preceding the backslash is also elided.

    >>> list(join_continuation(['goo\\', 'dly']))
    ['godly']

    A terrible idea, but...
    If no line is available to continue, suppress the lines.

    >>> list(join_continuation(['foo', 'bar\\', 'baz\\']))
    ['foo']
    

---

Support functions for working with wheel files.
Extract information from the provided wheel, ensuring it meets basic
    standards.

    Returns the name of the .dist-info directory and the parsed WHEEL metadata.
    
Returns the name of the contained .dist-info directory.

    Raises AssertionError or UnsupportedWheel if not found, >1 found, or
    it doesn't match the provided name.
    
Return the WHEEL metadata of an extracted wheel, if possible.
    Otherwise, raise UnsupportedWheel.
    
Given WHEEL metadata, return the parsed Wheel-Version.
    Otherwise, raise UnsupportedWheel.
    
Raises errors or warns if called with an incompatible Wheel-Version.

    pip should refuse to install a Wheel-Version that's a major series
    ahead of what it's compatible with (e.g 2.0 > 1.1); and warn when
    installing a version only minor version ahead (e.g 1.2 > 1.1).

    version: a 2-tuple representing a Wheel-Version (Major, Minor)
    name: name of wheel or package to raise exception about

    :raises UnsupportedWheel: when an incompatible Wheel-Version is given
    

---



---

Utilities related archives.
Get the current umask which involves having to set it temporarily.
Returns true if all the paths have the same leading path name
    (i.e., everything is in one subdirectory in an archive)

    Return true if the absolute path of target is within the directory
    

    Make file present at path have execute for user/group/world
    (chmod +x) is no-op on windows per python docs
    

    Unzip the file (with path `filename`) to the destination `location`.  All
    files are written based on system defaults and umask (i.e. permissions are
    not preserved), except that regular file members with any execute
    permissions (user, group, or world) have "chmod +x" applied after being
    written. Note that for windows, any execute changes using os.chmod are
    no-ops per the python docs.
    

    Untar the file (with path `filename`) to the destination `location`.
    All files are written based on system defaults and umask (i.e. permissions
    are not preserved), except that regular file members with any execute
    permissions (user, group, or world) have "chmod +x" applied on top of the
    default.  Note that for windows, any execute changes using os.chmod are
    no-ops per the python docs.
    
Fallback for Python without tarfile.data_filter

---


    Check if the given Python version matches a "Requires-Python" specifier.

    :param version_info: A 3-tuple of ints representing a Python
        major-minor-micro version to check (e.g. `sys.version_info[:3]`).

    :return: `True` if the given Python version satisfies the requirement.
        Otherwise, return `False`.

    :raises InvalidSpecifier: If `requires_python` has an invalid format.
    
Construct a packaging.Requirement object with caching

---

Decorator to automatically retry a function on error.

    If the function raises, the function is recalled with the same arguments
    until it returns or the time limit is reached. When the time limit is
    surpassed, the last exception raised is reraised.

    :param wait: The time to wait after an error before retrying, in seconds.
    :param stop_after_delay: The time limit after which retries will cease,
        in seconds.
    

---

Stuff that differs in different Python versions and platform
distributions.

    Return path's uid.

    Does not follow symlinks:
        https://github.com/pypa/pip/pull/935#discussion_r5307003

    Placed this function in compat due to differences on AIX and
    Jython, that should eventually go away.

    :raises OSError: When path is a symlink or can't be read.
    

---


    Convert a Name metadata value to a .egg-link name, by applying
    the same substitution as pkg_resources's safe_name function.
    Note: we cannot use canonicalize_name because it has a different logic.

    We also look for the raw name (without normalization) as setuptools 69 changed
    the way it names .egg-link files (https://github.com/pypa/setuptools/issues/4167).
    

    Look for a .egg-link file for project name, by walking sys.path.
    

    Return the path for the .egg-link file if it exists, otherwise, None.

    There's 3 scenarios:
    1) not in a virtualenv
       try to find in site.USER_SITE, then site_packages
    2) in a no-global virtualenv
       try to find in site_packages
    3) in a yes-global virtualenv
       try to find in site_packages, then site.USER_SITE
       (don't look in global location)

    For #1 and #3, there could be odd cases, where there's an egg-link in 2
    locations.

    This method will just return the first one found.
    

---

For when pip wants to check the date or time.

---

xmlrpclib.Transport implementation
Provide a `xmlrpclib.Transport` implementation via a `PipSession`
    object.
    

---

Network Authentication Helpers

Contains interface (MultiDomainBasicAuth) and associated glue code for
providing credentials in the context of network requests.

Keyring base provider interface
Keyring null provider
Keyring interface which uses locally imported `keyring`
Provider which uses `keyring` cli

    Instead of calling the keyring package installed alongside pip
    we call keyring on the command line which will enable pip to
    use which ever installation of keyring is available first in
    PATH.
    
Mirror the implementation of keyring.get_password using cli
Mirror the implementation of keyring.set_password using cli
Return the tuple auth for a given url from keyring.
Return the original index URL matching the requested URL.

        Cached or dynamically generated credentials may work against
        the original index URL rather than just the netloc.

        The provided url should have had its username and password
        removed already. If the original index url had credentials then
        they will be included in the return value.

        Returns None if no matching index was found, or if --no-index
        was specified by the user.
        
Find and return credentials for the specified URL.
Return the credentials to use for the provided URL.

        If allowed, netrc and keyring may be used to obtain the
        correct credentials.

        Returns (url_without_credentials, username, password). Note
        that even if the original URL contains credentials, this
        function may return a different username and password.
        
Response callback to warn about incorrect credentials.
Response callback to save credentials on success.

---

Download files with progress indicators.

    Return either the ETag or Last-Modified header (or None if neither exists).
    The return value can be used in an If-Range header.
    

    Sanitize the "filename" value from a Content-Disposition header.
    

    Parse the "filename" value from a Content-Disposition header, and
    return the default filename if the result is empty.
    
Get an ideal filename from the given HTTP response, falling back to
    the link filename if not provided.
    
Download the file given by link into location.
Process the response and write the chunks to the file.
Write the chunks to the file and return the number of bytes received.
Attempt to resume the download if connection was dropped.
Reset the download state to restart downloading from the beginning.
Download the files given by links into location.

---

PipSession and supporting code, containing all pip-specific
network request configuration and behavior.


    Return whether it looks like pip is running under CI.
    

    Return a string representing the user agent.
    
Mixin to add the ``ssl_context`` constructor argument to HTTP adapters.

    The additional argument is forwarded directly to the pool manager. This allows us
    to dynamically decide what SSL store to use at runtime, which is used to implement
    the optional ``truststore`` backend.
    

        :param trusted_hosts: Domains not to emit warnings for when not using
            HTTPS.
        

        :param new_index_urls: New index urls to update the authentication
            handler with.
        

        :param host: It is okay to provide a host that has previously been
            added.
        :param source: An optional source string, for logging where the host
            string came from.
        

---

Lazy ZIP over HTTP
Return a distribution object from the given wheel URL.

    This uses HTTP range requests to only fetch the portion of the wheel
    containing metadata, just enough for the object to be constructed.
    If such requests are not supported, HTTPRangeRequestUnsupported
    is raised.
    
File-like object mapped to a ZIP file over HTTP.

    This uses HTTP range requests to lazily fetch the file's content,
    which is supposed to be fed to ZipFile.  If such requests are not
    supported by the server, raise HTTPRangeRequestUnsupported
    during initialization.
    
Opening mode, which is always rb.
Path to the underlying file.
Return whether random access is supported, which is True.
Close the file.
Whether the file is closed.
Read up to size bytes from the object and return them.

        As a convenience, if size is unspecified or -1,
        all bytes until EOF are returned.  Fewer than
        size bytes may be returned if EOF is reached.
        
Return whether the file is readable, which is True.
Change stream position and return the new absolute position.

        Seek to offset relative position indicated by whence:
        * 0: Start of stream (the default).  pos should be >= 0;
        * 1: Current position - pos may be negative;
        * 2: End of stream - pos usually negative.
        
Return the current position.
Resize the stream to the given size in bytes.

        If size is unspecified resize to the current position.
        The current stream position isn't changed.

        Return the new file size.
        
Return False.
Return a context manager keeping the position.

        At the end of the block, seek back to original position.
        
Check and download until the file is a valid ZIP.
Return HTTP response to a range request from start to end.
Return a generator of intervals to be fetched.

        Args:
            start (int): Start of needed interval
            end (int): End of needed interval
            left (int): Index of first overlapping downloaded data
            right (int): Index after last overlapping downloaded data
        
Download bytes from start to end inclusively.

---

HTTP cache implementation.
If we can't access the cache then we can just skip caching and process
    requests as if caching wasn't enabled.
    

    A file based cache which is safe to use even when the target directory may
    not be accessible or writable.

    There is a race condition when two processes try to write and/or read the
    same entry at the same time, since each entry consists of two separate
    files (https://github.com/psf/cachecontrol/issues/324).  We therefore have
    additional logic that makes sure that both files to be present before
    returning an entry; this fixes the read side of the race condition.

    For the write side, we assume that the server will only ever return the
    same data for the same URL, which ought to be the case for files pip is
    downloading.  PyPI does not have a mechanism to swap out a wheel for
    another wheel, for example.  If this assumption is not true, the
    CacheControl issue will need to be fixed.
    

---

Contains purely network-related utilities.

---

Given a requests Response, provide the data chunks.

---


The main purpose of this module is to expose LinkCollector.collect_sources().

Look for VCS schemes in the URL.

    Returns the matched VCS scheme, or None if there's no match.
    

    Check the Content-Type header to ensure the response contains a Simple
    API Response.

    Raises `_NotAPIContent` if the content type is not a valid content-type.
    

    Send a HEAD request to the URL, and ensure the response contains a simple
    API Response.

    Raises `_NotHTTP` if the URL is not available for a HEAD request, or
    `_NotAPIContent` if the content type is not a valid content type.
    
Access an Simple API response with GET, and return the response.

    This consists of three parts:

    1. If the URL looks suspiciously like an archive, send a HEAD first to
       check the Content-Type is HTML or Simple API, to avoid downloading a
       large file. Raise `_NotHTTP` if the content type cannot be determined, or
       `_NotAPIContent` if it is not HTML or a Simple API.
    2. Actually perform the request. Raise HTTP exceptions on network failures.
    3. Check the Content-Type header to make sure we got a Simple API response,
       and raise `_NotAPIContent` otherwise.
    
Determine if we have any encoding information in our headers.

    Given a function that parses an Iterable[Link] from an IndexContent, cache the
    function's result (keyed by CacheablePageContent), unless the IndexContent
    `page` has `page.cache_link_parsing == False`.
    

    Parse a Simple API's Index Content, and yield its anchor elements as Link objects.
    
Represents one response (or page), along with its URL.

    :param encoding: the encoding to decode the given content.
    :param url: the URL from which the HTML was downloaded.
    :param cache_link_parsing: whether links parsed from this page's url
                               should be cached. PyPI index urls should
                               have this set to False, for example.
    

    HTMLParser that keeps the first base HREF and a list of all anchor
    elements' attributes.
    

    Responsible for collecting Link objects from all configured locations,
    making network requests as needed.

    The class's main method is its collect_sources() method.
    

        :param session: The Session to use to make requests.
        :param suppress_no_index: Whether to ignore the --no-index option
            when constructing the SearchScope object.
        

        Fetch an HTML page containing package links.
        

---

Routines related to PyPI, indexes

    Return whether the given Python version is compatible with a link's
    "Requires-Python" value.

    :param version_info: A 3-tuple of ints representing the Python
        major-minor-micro version to check.
    :param ignore_requires_python: Whether to ignore the "Requires-Python"
        value if the given Python version isn't compatible.
    

    Responsible for evaluating links for a particular project.
    

        :param project_name: The user supplied package name.
        :param canonical_name: The canonical package name.
        :param formats: The formats allowed for this package. Should be a set
            with 'binary' or 'source' or both in it.
        :param target_python: The target Python interpreter to use when
            evaluating link compatibility. This is used, for example, to
            check wheel compatibility, as well as when checking the Python
            version, e.g. the Python version embedded in a link filename
            (or egg fragment) and against an HTML link's optional PEP 503
            "data-requires-python" attribute.
        :param allow_yanked: Whether files marked as yanked (in the sense
            of PEP 592) are permitted to be candidates for install.
        :param ignore_requires_python: Whether to ignore incompatible
            PEP 503 "data-requires-python" values in HTML links. Defaults
            to False.
        

        Determine whether a link is a candidate for installation.

        :return: A tuple (result, detail), where *result* is an enum
            representing whether the evaluation found a candidate, or the reason
            why one is not found. If a candidate is found, *detail* will be the
            candidate's version string; if one is not found, it contains the
            reason the link fails to qualify.
        

    Filter out candidates whose hashes aren't allowed, and return a new
    list of candidates.

    If at least one candidate has an allowed hash, then all candidates with
    either an allowed hash or no hash specified are returned.  Otherwise,
    the given candidates are returned.

    Including the candidates with no hash specified when there is a match
    allows a warning to be logged if there is a more preferred candidate
    with no hash specified.  Returning all candidates in the case of no
    matches lets pip report the hash of the candidate that would otherwise
    have been installed (e.g. permitting the user to more easily update
    their requirements file with the desired hash).
    

    Encapsulates some of the preferences for filtering and sorting
    InstallationCandidate objects.
    
A collection of candidates, returned by `PackageFinder.find_best_candidate`.

    This class is only intended to be instantiated by CandidateEvaluator's
    `compute_best_candidate()` method.

    :param all_candidates: A sequence of all available candidates found.
    :param applicable_candidates: The applicable candidates.
    :param best_candidate: The most preferred candidate found, or None
        if no applicable candidates were found.
    

    Responsible for filtering and sorting candidates for installation based
    on what tags are valid.
    
Create a CandidateEvaluator object.

        :param target_python: The target Python interpreter to use when
            checking compatibility. If None (the default), a TargetPython
            object will be constructed from the running Python.
        :param specifier: An optional object implementing `filter`
            (e.g. `packaging.specifiers.SpecifierSet`) to filter applicable
            versions.
        :param hashes: An optional collection of allowed hashes.
        

        :param supported_tags: The PEP 425 tags supported by the target
            Python in order of preference (most preferred first).
        

        Return the applicable candidates from a list of candidates.
        

        Function to pass as the `key` argument to a call to sorted() to sort
        InstallationCandidates by preference.

        Returns a tuple such that tuples sorting as greater using Python's
        default comparison operator are more preferred.

        The preference is as follows:

        First and foremost, candidates with allowed (matching) hashes are
        always preferred over candidates without matching hashes. This is
        because e.g. if the only candidate with an allowed hash is yanked,
        we still want to use that candidate.

        Second, excepting hash considerations, candidates that have been
        yanked (in the sense of PEP 592) are always less preferred than
        candidates that haven't been yanked. Then:

        If not finding wheels, they are sorted by version only.
        If finding wheels, then the sort order is by version, then:
          1. existing installs
          2. wheels ordered via Wheel.support_index_min(self._supported_tags)
          3. source archives
        If prefer_binary was set, then all wheels are sorted above sources.

        Note: it was considered to embed this logic into the Link
              comparison operators, but then different sdist links
              with the same version, would have to be considered equal
        

        Return the best candidate per the instance's sort order, or None if
        no candidate is acceptable.
        

        Compute and return a `BestCandidateResult` instance.
        
This finds packages.

    This is meant to match easy_install's technique for looking for
    packages, by reading pages and looking for appropriate links.
    

        This constructor is primarily meant to be used by the create() class
        method and from tests.

        :param format_control: A FormatControl object, used to control
            the selection of source packages / binary packages when consulting
            the index and links.
        :param candidate_prefs: Options to use when creating a
            CandidateEvaluator object.
        
Create a PackageFinder.

        :param selection_prefs: The candidate selection preferences, as a
            SelectionPreferences object.
        :param target_python: The target Python interpreter to use when
            checking compatibility. If None (the default), a TargetPython
            object will be constructed from the running Python.
        

        Returns elements of links in order, non-egg links first, egg links
        second, while eliminating duplicates
        

        If the link is a candidate for install, convert it to an
        InstallationCandidate and return it. Otherwise, return None.
        

        Convert links that are candidates to InstallationCandidate objects.
        
Find all available InstallationCandidate for project_name

        This checks index_urls and find_links.
        All versions found are returned as an InstallationCandidate list.

        See LinkEvaluator.evaluate_link() for details on which files
        are accepted.
        
Create a CandidateEvaluator object to use.
Find matches for the given project and specifier.

        :param specifier: An optional object implementing `filter`
            (e.g. `packaging.specifiers.SpecifierSet`) to filter applicable
            versions.

        :return: A `BestCandidateResult` instance.
        
Try to find a Link matching req

        Expects req, an InstallRequirement and upgrade, a boolean
        Returns a InstallationCandidate if found,
        Raises DistributionNotFound or BestVersionAlreadyInstalled otherwise
        
Find the separator's index based on the package's canonical name.

    :param fragment: A <package>+<version> filename "fragment" (stem) or
        egg fragment.
    :param canonical_name: The package's canonical name.

    This function is needed since the canonicalized name does not necessarily
    have the same length as the egg info's name part. An example::

    >>> fragment = 'foo__bar-1.0'
    >>> canonical_name = 'foo-bar'
    >>> _find_name_version_sep(fragment, canonical_name)
    8
    
Parse the version string from a <package>+<version> filename
    "fragment" (stem) or egg fragment.

    :param fragment: The string to parse. E.g. foo-2.1
    :param canonical_name: The canonicalized name of the package this
        belongs to.
    

---

Index interaction code

---

Returns the underlying link, if there's one.
Candidates found by parsing an archive listing HTML file.
Links found by specifying archives directly.
Scans directory and caches results
Scans directory once and populates both page_candidates
        and project_name_to_urls at the same time
        
Link source specified by ``--find-links=<path-to-dir>``.

    This looks the content of the directory, and returns:

    * ``page_candidates``: Links listed on each HTML file in the directory.
    * ``file_candidates``: Archives in the directory.
    
``--find-links=<path-or-url>`` or ``--[extra-]index-url=<path-or-url>``.

    If a URL is supplied, it must be a ``file:`` URL. If a path is supplied to
    the option, it is converted to a URL first. This returns:

    * ``page_candidates``: Links listed on an HTML file.
    * ``file_candidates``: The non-HTML file.
    
``--find-links=<url>`` or ``--[extra-]index-url=<url>``.

    This returns:

    * ``page_candidates``: Links listed on an HTML file.
    * ``file_candidates``: The non-HTML file.
    
``--[extra-]index-url=<path-to-directory>``.

    This is treated like a remote URL; ``candidates_from_page`` contains logic
    for this by appending ``index.html`` to the link.
    

---


requests.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Requests' exceptions.

There was an ambiguous exception that occurred while handling your
    request.
    
Initialize RequestException with `request` and `response` objects.
A JSON error occurred.
Couldn't decode the text into json

        Construct the JSONDecodeError instance first with all
        args. Then use it's args to construct the IOError so that
        the json specific args aren't used as IOError specific args
        and the error message from JSONDecodeError is preserved.
        

        The __reduce__ method called when pickling the object must
        be the one from the JSONDecodeError (be it json/simplejson)
        as it expects all the arguments for instantiation, not just
        one like the IOError, and the MRO would by default call the
        __reduce__ method from the IOError due to the inheritance order.
        
An HTTP error occurred.
A Connection error occurred.
A proxy error occurred.
An SSL error occurred.
The request timed out.

    Catching this error will catch both
    :exc:`~requests.exceptions.ConnectTimeout` and
    :exc:`~requests.exceptions.ReadTimeout` errors.
    
The request timed out while trying to connect to the remote server.

    Requests that produced this error are safe to retry.
    
The server did not send any data in the allotted amount of time.
A valid URL is required to make a request.
Too many redirects.
The URL scheme (e.g. http or https) is missing.
The URL scheme provided is either invalid or unsupported.
The URL provided was somehow invalid.
The header value provided was somehow invalid.
The proxy URL provided is invalid.
The server declared chunked encoding but sent an invalid chunk.
Failed to decode response content.
The content for this response was already consumed.
Custom retries logic failed
Requests encountered an error when trying to rewind a body.
Base warning for Requests.
A file was opened in text mode, but Requests determined its binary length.
An imported dependency doesn't match the expected version range.

---


requests.auth
~~~~~~~~~~~~~

This module contains the authentication handlers for Requests.

Returns a Basic Auth string.
Base class that all auth implementations derive from
Attaches HTTP Basic Authentication to the given Request object.
Attaches HTTP Proxy Authentication to a given Request object.
Attaches HTTP Digest Authentication to the given Request object.

        :rtype: str
        
Reset num_401_calls counter on redirects.

        Takes the given response and tries digest-auth, if needed.

        :rtype: requests.Response
        

---


requests.api
~~~~~~~~~~~~

This module implements the Requests API.

:copyright: (c) 2012 by Kenneth Reitz.
:license: Apache2, see LICENSE for more details.

Constructs and sends a :class:`Request <Request>`.

    :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content_type'`` is a string
        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
        to add for the file.
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read
        timeout) <timeouts>` tuple.
    :type timeout: float or tuple
    :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
    :type allow_redirects: bool
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    Usage::

      >>> import requests
      >>> req = requests.request('GET', 'https://httpbin.org/get')
      >>> req
      <Response [200]>
    
Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
Sends an OPTIONS request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
Sends a HEAD request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes. If
        `allow_redirects` is not provided, it will be set to `False` (as
        opposed to the default :meth:`request` behavior).
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
Sends a PUT request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
Sends a PATCH request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
Sends a DELETE request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    

---


requests.adapters
~~~~~~~~~~~~~~~~~

This module contains the transport adapters that Requests uses to define
and maintain connections.

The Base Transport Adapter
Sends PreparedRequest object. Returns Response object.

        :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
        :param stream: (optional) Whether to stream the request content.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use
        :param cert: (optional) Any user-provided SSL certificate to be trusted.
        :param proxies: (optional) The proxies dictionary to apply to the request.
        
Cleans up adapter specific items.
The built-in HTTP Adapter for urllib3.

    Provides a general-case interface for Requests sessions to contact HTTP and
    HTTPS urls by implementing the Transport Adapter interface. This class will
    usually be created by the :class:`Session <Session>` class under the
    covers.

    :param pool_connections: The number of urllib3 connection pools to cache.
    :param pool_maxsize: The maximum number of connections to save in the pool.
    :param max_retries: The maximum number of retries each connection
        should attempt. Note, this applies only to failed DNS lookups, socket
        connections and connection timeouts, never to requests where data has
        made it to the server. By default, Requests does not retry failed
        connections. If you need granular control over the conditions under
        which we retry a request, import urllib3's ``Retry`` class and pass
        that instead.
    :param pool_block: Whether the connection pool should block for connections.

    Usage::

      >>> import requests
      >>> s = requests.Session()
      >>> a = requests.adapters.HTTPAdapter(max_retries=3)
      >>> s.mount('http://', a)
    
Initializes a urllib3 PoolManager.

        This method should not be called from user code, and is only
        exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param connections: The number of urllib3 connection pools to cache.
        :param maxsize: The maximum number of connections to save in the pool.
        :param block: Block when no free connections are available.
        :param pool_kwargs: Extra keyword arguments used to initialize the Pool Manager.
        
Return urllib3 ProxyManager for the given proxy.

        This method should not be called from user code, and is only
        exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param proxy: The proxy to return a urllib3 ProxyManager for.
        :param proxy_kwargs: Extra keyword arguments used to configure the Proxy Manager.
        :returns: ProxyManager
        :rtype: urllib3.ProxyManager
        
Verify a SSL certificate. This method should not be called from user
        code, and is only exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param conn: The urllib3 connection object associated with the cert.
        :param url: The requested URL.
        :param verify: Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use
        :param cert: The SSL certificate to verify.
        
Builds a :class:`Response <requests.Response>` object from a urllib3
        response. This should not be called from user code, and is only exposed
        for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`

        :param req: The :class:`PreparedRequest <PreparedRequest>` used to generate the response.
        :param resp: The urllib3 response object.
        :rtype: requests.Response
        
Build the PoolKey attributes used by urllib3 to return a connection.

        This looks at the PreparedRequest, the user-specified verify value,
        and the value of the cert parameter to determine what PoolKey values
        to use to select a connection from a given urllib3 Connection Pool.

        The SSL related pool key arguments are not consistently set. As of
        this writing, use the following to determine what keys may be in that
        dictionary:

        * If ``verify`` is ``True``, ``"ssl_context"`` will be set and will be the
          default Requests SSL Context
        * If ``verify`` is ``False``, ``"ssl_context"`` will not be set but
          ``"cert_reqs"`` will be set
        * If ``verify`` is a string, (i.e., it is a user-specified trust bundle)
          ``"ca_certs"`` will be set if the string is not a directory recognized
          by :py:func:`os.path.isdir`, otherwise ``"ca_certs_dir"`` will be
          set.
        * If ``"cert"`` is specified, ``"cert_file"`` will always be set. If
          ``"cert"`` is a tuple with a second item, ``"key_file"`` will also
          be present

        To override these settings, one may subclass this class, call this
        method and use the above logic to change parameters as desired. For
        example, if one wishes to use a custom :py:class:`ssl.SSLContext` one
        must both set ``"ssl_context"`` and based on what else they require,
        alter the other keys to ensure the desired behaviour.

        :param request:
            The PreparedReqest being sent over the connection.
        :type request:
            :class:`~requests.models.PreparedRequest`
        :param verify:
            Either a boolean, in which case it controls whether
            we verify the server's TLS certificate, or a string, in which case it
            must be a path to a CA bundle to use.
        :param cert:
            (optional) Any user-provided SSL certificate for client
            authentication (a.k.a., mTLS). This may be a string (i.e., just
            the path to a file which holds both certificate and key) or a
            tuple of length 2 with the certificate file path and key file
            path.
        :returns:
            A tuple of two dictionaries. The first is the "host parameters"
            portion of the Pool Key including scheme, hostname, and port. The
            second is a dictionary of SSLContext related parameters.
        
Returns a urllib3 connection for the given request and TLS settings.
        This should not be called from user code, and is only exposed for use
        when subclassing the :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param request:
            The :class:`PreparedRequest <PreparedRequest>` object to be sent
            over the connection.
        :param verify:
            Either a boolean, in which case it controls whether we verify the
            server's TLS certificate, or a string, in which case it must be a
            path to a CA bundle to use.
        :param proxies:
            (optional) The proxies dictionary to apply to the request.
        :param cert:
            (optional) Any user-provided SSL certificate to be used for client
            authentication (a.k.a., mTLS).
        :rtype:
            urllib3.ConnectionPool
        
DEPRECATED: Users should move to `get_connection_with_tls_context`
        for all subclasses of HTTPAdapter using Requests>=2.32.2.

        Returns a urllib3 connection for the given URL. This should not be
        called from user code, and is only exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param url: The URL to connect to.
        :param proxies: (optional) A Requests-style dictionary of proxies used on this request.
        :rtype: urllib3.ConnectionPool
        
Disposes of any internal state.

        Currently, this closes the PoolManager and any active ProxyManager,
        which closes any pooled connections.
        
Obtain the url to use when making the final request.

        If the message is being sent through a HTTP proxy, the full URL has to
        be used. Otherwise, we should only use the path portion of the URL.

        This should not be called from user code, and is only exposed for use
        when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
        :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs.
        :rtype: str
        
Add any headers needed by the connection. As of v2.0 this does
        nothing by default, but is left for overriding by users that subclass
        the :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        This should not be called from user code, and is only exposed for use
        when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param request: The :class:`PreparedRequest <PreparedRequest>` to add headers to.
        :param kwargs: The keyword arguments from the call to send().
        
Returns a dictionary of the headers to add to any request sent
        through a proxy. This works with urllib3 magic to ensure that they are
        correctly sent to the proxy, rather than in a tunnelled request if
        CONNECT is being used.

        This should not be called from user code, and is only exposed for use
        when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param proxy: The url of the proxy being used for this request.
        :rtype: dict
        
Sends PreparedRequest object. Returns Response object.

        :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
        :param stream: (optional) Whether to stream the request content.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple or urllib3 Timeout object
        :param verify: (optional) Either a boolean, in which case it controls whether
            we verify the server's TLS certificate, or a string, in which case it
            must be a path to a CA bundle to use
        :param cert: (optional) Any user-provided SSL certificate to be trusted.
        :param proxies: (optional) The proxies dictionary to apply to the request.
        :rtype: requests.Response
        

---


requests.cookies
~~~~~~~~~~~~~~~~

Compatibility code to be able to use `http.cookiejar.CookieJar` with requests.

requests.utils imports from here, so be careful with imports.

Wraps a `requests.Request` to mimic a `urllib2.Request`.

    The code in `http.cookiejar.CookieJar` expects this interface in order to correctly
    manage cookie policies, i.e., determine whether a cookie can be set, given the
    domains of the request and the cookie.

    The original request object is read-only. The client is responsible for collecting
    the new headers via `get_new_headers()` and interpreting them appropriately. You
    probably want `get_cookie_header`, defined below.
    
cookiejar has no legitimate use for this method; add it back if you find one.
Wraps a `httplib.HTTPMessage` to mimic a `urllib.addinfourl`.

    ...what? Basically, expose the parsed HTTP headers from the server response
    the way `http.cookiejar` expects to see them.
    
Make a MockResponse for `cookiejar` to read.

        :param headers: a httplib.HTTPMessage or analogous carrying the headers
        
Extract the cookies from the response into a CookieJar.

    :param jar: http.cookiejar.CookieJar (not necessarily a RequestsCookieJar)
    :param request: our own requests.Request object
    :param response: urllib3.HTTPResponse object
    

    Produce an appropriate Cookie header string to be sent with `request`, or None.

    :rtype: str
    
Unsets a cookie by name, by default over all domains and paths.

    Wraps CookieJar.clear(), is O(n).
    
There are two cookies that meet the criteria specified in the cookie jar.
    Use .get and .set and include domain and path args in order to be more specific.
    
Compatibility class; is a http.cookiejar.CookieJar, but exposes a dict
    interface.

    This is the CookieJar we create by default for requests and sessions that
    don't specify one, since some clients may expect response.cookies and
    session.cookies to support dict operations.

    Requests does not use the dict interface internally; it's just for
    compatibility with external client code. All requests code should work
    out of the box with externally provided instances of ``CookieJar``, e.g.
    ``LWPCookieJar`` and ``FileCookieJar``.

    Unlike a regular CookieJar, this class is pickleable.

    .. warning:: dictionary operations that are normally O(1) may be O(n).
    
Dict-like get() that also supports optional domain and path args in
        order to resolve naming collisions from using one cookie jar over
        multiple domains.

        .. warning:: operation is O(n), not O(1).
        
Dict-like set() that also supports optional domain and path args in
        order to resolve naming collisions from using one cookie jar over
        multiple domains.
        
Dict-like iterkeys() that returns an iterator of names of cookies
        from the jar.

        .. seealso:: itervalues() and iteritems().
        
Dict-like keys() that returns a list of names of cookies from the
        jar.

        .. seealso:: values() and items().
        
Dict-like itervalues() that returns an iterator of values of cookies
        from the jar.

        .. seealso:: iterkeys() and iteritems().
        
Dict-like values() that returns a list of values of cookies from the
        jar.

        .. seealso:: keys() and items().
        
Dict-like iteritems() that returns an iterator of name-value tuples
        from the jar.

        .. seealso:: iterkeys() and itervalues().
        
Dict-like items() that returns a list of name-value tuples from the
        jar. Allows client-code to call ``dict(RequestsCookieJar)`` and get a
        vanilla python dict of key value pairs.

        .. seealso:: keys() and values().
        
Utility method to list all the domains in the jar.
Utility method to list all the paths in the jar.
Returns True if there are multiple domains in the jar.
        Returns False otherwise.

        :rtype: bool
        
Takes as an argument an optional domain and path and returns a plain
        old Python dict of name-value pairs of cookies that meet the
        requirements.

        :rtype: dict
        
Dict-like __getitem__() for compatibility with client code. Throws
        exception if there are more than one cookie with name. In that case,
        use the more explicit get() method instead.

        .. warning:: operation is O(n), not O(1).
        
Dict-like __setitem__ for compatibility with client code. Throws
        exception if there is already a cookie of that name in the jar. In that
        case, use the more explicit set() method instead.
        
Deletes a cookie given a name. Wraps ``http.cookiejar.CookieJar``'s
        ``remove_cookie_by_name()``.
        
Updates this jar with cookies from another CookieJar or dict-like
Requests uses this method internally to get cookie values.

        If there are conflicting cookies, _find arbitrarily chooses one.
        See _find_no_duplicates if you want an exception thrown if there are
        conflicting cookies.

        :param name: a string containing name of cookie
        :param domain: (optional) string containing domain of cookie
        :param path: (optional) string containing path of cookie
        :return: cookie.value
        
Both ``__get_item__`` and ``get`` call this function: it's never
        used elsewhere in Requests.

        :param name: a string containing name of cookie
        :param domain: (optional) string containing domain of cookie
        :param path: (optional) string containing path of cookie
        :raises KeyError: if cookie is not found
        :raises CookieConflictError: if there are multiple cookies
            that match name and optionally domain and path
        :return: cookie.value
        
Unlike a normal CookieJar, this class is pickleable.
Unlike a normal CookieJar, this class is pickleable.
Return a copy of this RequestsCookieJar.
Return the CookiePolicy instance used.
Make a cookie from underspecified parameters.

    By default, the pair of `name` and `value` will be set for the domain ''
    and sent on every request (this is sometimes called a "supercookie").
    
Convert a Morsel object into a Cookie containing the one k/v pair.
Returns a CookieJar from a key/value dictionary.

    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :param cookiejar: (optional) A cookiejar to add the cookies to.
    :param overwrite: (optional) If False, will not replace cookies
        already in the jar with new ones.
    :rtype: CookieJar
    
Add cookies to cookiejar and returns a merged CookieJar.

    :param cookiejar: CookieJar object to add the cookies to.
    :param cookies: Dictionary or CookieJar object to be added.
    :rtype: CookieJar
    

---



---


requests.models
~~~~~~~~~~~~~~~

This module contains the primary objects that power Requests.

Build the path URL to use.
Encode parameters in a piece of data.

        Will successfully encode parameters when passed as a dict or a list of
        2-tuples. Order is retained if data is a list of 2-tuples but arbitrary
        if parameters are supplied as a dict.
        
Build the body for a multipart/form-data request.

        Will successfully encode files when passed as a dict or a list of
        tuples. Order is retained if data is a list of tuples but arbitrary
        if parameters are supplied as a dict.
        The tuples may be 2-tuples (filename, fileobj), 3-tuples (filename, fileobj, contentype)
        or 4-tuples (filename, fileobj, contentype, custom_headers).
        
Properly register a hook.
Deregister a previously registered hook.
        Returns True if the hook existed, False if not.
        
A user-created :class:`Request <Request>` object.

    Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.

    :param method: HTTP method to use.
    :param url: URL to send.
    :param headers: dictionary of headers to send.
    :param files: dictionary of {filename: fileobject} files to multipart upload.
    :param data: the body to attach to the request. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param json: json for the body to attach to the request (if files or data is not specified).
    :param params: URL parameters to append to the URL. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param auth: Auth handler or (user, pass) tuple.
    :param cookies: dictionary or CookieJar of cookies to attach to this request.
    :param hooks: dictionary of callback hooks, for internal usage.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> req.prepare()
      <PreparedRequest [GET]>
    
Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it.
The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
    containing the exact bytes that will be sent to the server.

    Instances are generated from a :class:`Request <Request>` object, and
    should not be instantiated manually; doing so may produce undesirable
    effects.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> r = req.prepare()
      >>> r
      <PreparedRequest [GET]>

      >>> s = requests.Session()
      >>> s.send(r)
      <Response [200]>
    
Prepares the entire request with the given parameters.
Prepares the given HTTP method.
Prepares the given HTTP URL.
Prepares the given HTTP headers.
Prepares the given HTTP body data.
Prepare Content-Length header based on request method and body
Prepares the given HTTP auth data.
Prepares the given HTTP cookie data.

        This function eventually generates a ``Cookie`` header from the
        given cookies using cookielib. Due to cookielib's design, the header
        will not be regenerated if it already exists, meaning this function
        can only be called once for the life of the
        :class:`PreparedRequest <PreparedRequest>` object. Any subsequent calls
        to ``prepare_cookies`` will have no actual effect, unless the "Cookie"
        header is removed beforehand.
        
Prepares the given hooks.
The :class:`Response <Response>` object, which contains a
    server's response to an HTTP request.
    
Returns True if :attr:`status_code` is less than 400.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        
Returns True if :attr:`status_code` is less than 400.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        
Allows you to use a response as an iterator.
Returns True if :attr:`status_code` is less than 400, False if not.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        
True if this Response is a well-formed HTTP redirect that could have
        been processed automatically (by :meth:`Session.resolve_redirects`).
        
True if this Response one of the permanent versions of redirect.
Returns a PreparedRequest for the next request in a redirect chain, if there is one.
The apparent encoding, provided by the charset_normalizer or chardet libraries.
Iterates over the response data.  When stream=True is set on the
        request, this avoids reading the content at once into memory for
        large responses.  The chunk size is the number of bytes it should
        read into memory.  This is not necessarily the length of each item
        returned as decoding can take place.

        chunk_size must be of type int or None. A value of None will
        function differently depending on the value of `stream`.
        stream=True will read data as it arrives in whatever size the
        chunks are received. If stream=False, data is returned as
        a single chunk.

        If decode_unicode is True, content will be decoded using the best
        available encoding based on the response.
        
Iterates over the response data, one line at a time.  When
        stream=True is set on the request, this avoids reading the
        content at once into memory for large responses.

        .. note:: This method is not reentrant safe.
        
Content of the response, in bytes.
Content of the response, in unicode.

        If Response.encoding is None, encoding will be guessed using
        ``charset_normalizer`` or ``chardet``.

        The encoding of the response content is determined based solely on HTTP
        headers, following RFC 2616 to the letter. If you can take advantage of
        non-HTTP knowledge to make a better guess at the encoding, you should
        set ``r.encoding`` appropriately before accessing this property.
        
Decodes the JSON response body (if any) as a Python object.

        This may return a dictionary, list, etc. depending on what is in the response.

        :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
        :raises requests.exceptions.JSONDecodeError: If the response body does not
            contain valid json.
        
Returns the parsed header links of the response, if any.
Raises :class:`HTTPError`, if one occurred.
Releases the connection back to the pool. Once this method has been
        called the underlying ``raw`` object must not be accessed again.

        *Note: Should not normally need to be called explicitly.*
        

---


requests.hooks
~~~~~~~~~~~~~~

This module provides the capabilities for the Requests hooks system.

Available hooks:

``response``:
    The response generated from a Request.

Dispatches a hook dictionary on a given piece of data.

---


requests._internal_utils
~~~~~~~~~~~~~~

Provides utility functions that are consumed internally by Requests
which depend on extremely few external helpers (such as compat)

Given a string object, regardless of type, returns a representation of
    that string in the native string type, encoding and decoding where
    necessary. This assumes ASCII unless told otherwise.
    
Determine if unicode string only contains ASCII characters.

    :param str u_string: unicode string to check. Must be unicode
        and not Python 2 `str`.
    :rtype: bool
    

---


requests.sessions
~~~~~~~~~~~~~~~~~

This module provides a Session object to manage and persist settings across
requests (cookies, auth, proxies).

Determines appropriate setting for a given request, taking into account
    the explicit setting on that request, and the setting in the session. If a
    setting is a dictionary, they will be merged together using `dict_class`
    
Properly merges both requests and session hooks.

    This is necessary because when request_hooks == {'response': []}, the
    merge breaks Session hooks entirely.
    
Receives a Response. Returns a redirect URI or ``None``
Decide whether Authorization header should be removed when redirecting
Receives a Response. Returns a generator of Responses or Requests.
When being redirected we may want to strip authentication from the
        request to avoid leaking credentials. This method intelligently removes
        and reapplies authentication where possible to avoid credential loss.
        
This method re-evaluates the proxy configuration by considering the
        environment variables. If we are redirected to a URL covered by
        NO_PROXY, we strip the proxy configuration. Otherwise, we set missing
        proxy keys for this URL (in case they were stripped by a previous
        redirect).

        This method also replaces the Proxy-Authorization header where
        necessary.

        :rtype: dict
        
When being redirected we may want to change the method of the request
        based on certain specs or browser behavior.
        
A Requests session.

    Provides cookie persistence, connection-pooling, and configuration.

    Basic Usage::

      >>> import requests
      >>> s = requests.Session()
      >>> s.get('https://httpbin.org/get')
      <Response [200]>

    Or as a context manager::

      >>> with requests.Session() as s:
      ...     s.get('https://httpbin.org/get')
      <Response [200]>
    
Constructs a :class:`PreparedRequest <PreparedRequest>` for
        transmission and returns it. The :class:`PreparedRequest` has settings
        merged from the :class:`Request <Request>` instance and those of the
        :class:`Session`.

        :param request: :class:`Request` instance to prepare with this
            session's settings.
        :rtype: requests.PreparedRequest
        
Constructs a :class:`Request <Request>`, prepares it and sends it.
        Returns :class:`Response <Response>` object.

        :param method: method for the new :class:`Request` object.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query
            string for the :class:`Request`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the
            :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the
            :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the
            :class:`Request`.
        :param files: (optional) Dictionary of ``'filename': file-like-objects``
            for multipart encoding upload.
        :param auth: (optional) Auth tuple or callable to enable
            Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Set to True by default.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol or protocol and
            hostname to the URL of the proxy.
        :param hooks: (optional) Dictionary mapping hook name to one event or
            list of events, event must be callable.
        :param stream: (optional) whether to immediately download the response
            content. Defaults to ``False``.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``. When set to
            ``False``, requests will accept any TLS certificate presented by
            the server, and will ignore hostname mismatches and/or expired
            certificates, which will make your application vulnerable to
            man-in-the-middle (MitM) attacks. Setting verify to ``False``
            may be useful during local development or testing.
        :param cert: (optional) if String, path to ssl client cert file (.pem).
            If Tuple, ('cert', 'key') pair.
        :rtype: requests.Response
        
Sends a GET request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Sends a OPTIONS request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Sends a HEAD request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Sends a POST request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Sends a PUT request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Sends a PATCH request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Sends a DELETE request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
Send a given PreparedRequest.

        :rtype: requests.Response
        

        Check the environment and merge it with some settings.

        :rtype: dict
        

        Returns the appropriate connection adapter for the given URL.

        :rtype: requests.adapters.BaseAdapter
        
Closes all adapters and as such the session
Registers a connection adapter to a prefix.

        Adapters are sorted in descending order by prefix length.
        

    Returns a :class:`Session` for context-management.

    .. deprecated:: 1.0.0

        This method has been deprecated since version 1.0.0 and is only kept for
        backwards compatibility. New code should use :class:`~requests.sessions.Session`
        to create a session. This may be removed at a future date.

    :rtype: Session
    

---


Requests HTTP Library
~~~~~~~~~~~~~~~~~~~~~

Requests is an HTTP library, written in Python, for human beings.
Basic GET usage:

   >>> import requests
   >>> r = requests.get('https://www.python.org')
   >>> r.status_code
   200
   >>> b'Python is a programming language' in r.content
   True

... or POST:

   >>> payload = dict(key1='value1', key2='value2')
   >>> r = requests.post('https://httpbin.org/post', data=payload)
   >>> print(r.text)
   {
     ...
     "form": {
       "key1": "value1",
       "key2": "value2"
     },
     ...
   }

The other HTTP methods are supported - see `requests.api`. Full documentation
is at <https://requests.readthedocs.io>.

:copyright: (c) 2017 by Kenneth Reitz.
:license: Apache 2.0, see LICENSE for more details.


---


The ``codes`` object defines a mapping from common names for HTTP statuses
to their numerical codes, accessible either as attributes or as dictionary
items.

Example::

    >>> import requests
    >>> requests.codes['temporary_redirect']
    307
    >>> requests.codes.teapot
    418
    >>> requests.codes['\o/']
    200

Some codes have multiple names, and both upper- and lower-case versions of
the names are allowed. For example, ``codes.ok``, ``codes.OK``, and
``codes.okay`` all correspond to the HTTP status code 200.


---


requests.certs
~~~~~~~~~~~~~~

This module returns the preferred default CA certificate bundle. There is
only one — the one from the certifi package.

If you are packaging Requests, e.g., for a Linux distribution or a managed
environment, you can change the definition of where() to return a separately
packaged CA bundle.


---


requests.compat
~~~~~~~~~~~~~~~

This module previously handled import compatibility issues
between Python 2 and Python 3. It remains for backwards
compatibility until the next major version.

Find supported character detection libraries.

---


requests.structures
~~~~~~~~~~~~~~~~~~~

Data structures that power Requests.

A case-insensitive ``dict``-like object.

    Implements all methods and operations of
    ``MutableMapping`` as well as dict's ``copy``. Also
    provides ``lower_items``.

    All keys are expected to be strings. The structure remembers the
    case of the last key to be set, and ``iter(instance)``,
    ``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
    will contain case-sensitive keys. However, querying and contains
    testing is case insensitive::

        cid = CaseInsensitiveDict()
        cid['Accept'] = 'application/json'
        cid['aCCEPT'] == 'application/json'  # True
        list(cid) == ['Accept']  # True

    For example, ``headers['content-encoding']`` will return the
    value of a ``'Content-Encoding'`` response header, regardless
    of how the header name was originally stored.

    If the constructor, ``.update``, or equality comparison
    operations are given keys that have equal ``.lower()``s, the
    behavior is undefined.
    
Like iteritems(), but with all lowercase keys.
Dictionary lookup object.

---

Module containing bug report helper(s).
Return a dict with the Python implementation and version.

    Provide both the name and the version of the Python implementation
    currently running. For example, on CPython 3.10.3 it will return
    {'name': 'CPython', 'version': '3.10.3'}.

    This function works best on CPython and PyPy: in particular, it probably
    doesn't work for Jython or IronPython. Future investigation should be done
    to work out the correct shape of the code for those platforms.
    
Generate information for a bug report.
Pretty-print the bug information as JSON.

---



---


requests.utils
~~~~~~~~~~~~~~

This module provides utility functions that are used within Requests
that are also useful for external consumption.

Return True, if the host should be bypassed.

        Checks proxy settings gathered from the environment, if specified,
        or the registry.
        
Returns an internal sequence dictionary update.
Returns the Requests tuple auth for a given url from netrc.
Tries to guess the filename of the given object.
Replace nonexistent paths that look like they refer to a member of a zip
    archive with the location of an extracted copy of the target, or else
    just return the provided path unchanged.
    
Write a file to the disk in an atomic fashion
Take an object and test to see if it can be represented as a
    dictionary. Unless it can not be represented as such, return an
    OrderedDict, e.g.,

    ::

        >>> from_key_val_list([('key', 'val')])
        OrderedDict([('key', 'val')])
        >>> from_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples
        >>> from_key_val_list({'key': 'val'})
        OrderedDict([('key', 'val')])

    :rtype: OrderedDict
    
Take an object and test to see if it can be represented as a
    dictionary. If it can be, return a list of tuples, e.g.,

    ::

        >>> to_key_val_list([('key', 'val')])
        [('key', 'val')]
        >>> to_key_val_list({'key': 'val'})
        [('key', 'val')]
        >>> to_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples

    :rtype: list
    
Parse lists as described by RFC 2068 Section 2.

    In particular, parse comma-separated lists where the elements of
    the list may include quoted-strings.  A quoted-string could
    contain a comma.  A non-quoted string could have quotes in the
    middle.  Quotes are removed automatically after parsing.

    It basically works like :func:`parse_set_header` just that items
    may appear multiple times and case sensitivity is preserved.

    The return value is a standard :class:`list`:

    >>> parse_list_header('token, "quoted value"')
    ['token', 'quoted value']

    To create a header from the :class:`list` again, use the
    :func:`dump_header` function.

    :param value: a string with a list header.
    :return: :class:`list`
    :rtype: list
    
Parse lists of key, value pairs as described by RFC 2068 Section 2 and
    convert them into a python dict:

    >>> d = parse_dict_header('foo="is a fish", bar="as well"')
    >>> type(d) is dict
    True
    >>> sorted(d.items())
    [('bar', 'as well'), ('foo', 'is a fish')]

    If there is no value for a key it will be `None`:

    >>> parse_dict_header('key_without_value')
    {'key_without_value': None}

    To create a header from the :class:`dict` again, use the
    :func:`dump_header` function.

    :param value: a string with a dict header.
    :return: :class:`dict`
    :rtype: dict
    
Unquotes a header value.  (Reversal of :func:`quote_header_value`).
    This does not use the real unquoting but what browsers are actually
    using for quoting.

    :param value: the header value to unquote.
    :rtype: str
    
Returns a key/value dictionary from a CookieJar.

    :param cj: CookieJar object to extract cookies from.
    :rtype: dict
    
Returns a CookieJar from a key/value dictionary.

    :param cj: CookieJar to insert cookies into.
    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :rtype: CookieJar
    
Returns encodings from given content string.

    :param content: bytestring to extract encodings from.
    
Returns content type and parameters from given header

    :param header: string
    :return: tuple containing content type and dictionary of
         parameters
    
Returns encodings from given HTTP Header Dict.

    :param headers: dictionary to extract encoding from.
    :rtype: str
    
Stream decodes an iterator.
Iterate over slices of a string.
Returns the requested content back in unicode.

    :param r: Response object to get unicode content from.

    Tried:

    1. charset from content-type
    2. fall back and replace all unicode characters

    :rtype: str
    
Un-escape any percent-escape sequences in a URI that are unreserved
    characters. This leaves all reserved, illegal and non-ASCII bytes encoded.

    :rtype: str
    
Re-quote the given URI.

    This function passes the given URI through an unquote/quote cycle to
    ensure that it is fully and consistently quoted.

    :rtype: str
    
This function allows you to check if an IP belongs to a network subnet

    Example: returns True if ip = 192.168.1.1 and net = 192.168.1.0/24
             returns False if ip = 192.168.1.1 and net = 192.168.100.0/24

    :rtype: bool
    
Converts mask from /xx format to xxx.xxx.xxx.xxx

    Example: if mask is 24 function returns 255.255.255.0

    :rtype: str
    

    :rtype: bool
    

    Very simple check of the cidr format in no_proxy variable.

    :rtype: bool
    
Set the environment variable 'env_name' to 'value'

    Save previous value, yield, and then restore the previous value stored in
    the environment variable 'env_name'.

    If 'value' is None, do nothing

    Returns whether we should bypass proxies or not.

    :rtype: bool
    

    Return a dict of environment proxies.

    :rtype: dict
    
Select a proxy for the url, if applicable.

    :param url: The url being for the request
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    
This method takes proxy information from a request and configuration
    input to resolve a mapping of target proxies. This will consider settings
    such as NO_PROXY to strip proxy configurations.

    :param request: Request or PreparedRequest
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    :param trust_env: Boolean declaring whether to trust environment configs

    :rtype: dict
    

    Return a string representing the default user agent.

    :rtype: str
    

    :rtype: requests.structures.CaseInsensitiveDict
    
Return a list of parsed link headers proxies.

    i.e. Link: <http:/.../front.jpeg>; rel=front; type="image/jpeg",<http://.../back.jpeg>; rel=back;type="image/jpeg"

    :rtype: list
    

    :rtype: str
    
Given a URL that may or may not have a scheme, prepend the given scheme.
    Does not replace a present scheme with the one provided as an argument.

    :rtype: str
    
Given a url with authentication components, extract them into a tuple of
    username,password.

    :rtype: (str,str)
    
Verifies that header parts don't contain leading whitespace
    reserved characters, or return characters.

    :param header: tuple, in the format (name, value).
    

    Given a url remove the fragment and the authentication part.

    :rtype: str
    
Move file pointer back to its recorded starting position
    so it can be read again on redirect.
    

---

Base exception for all IDNA-encoding related problems
Exception when bidirectional requirements are not satisfied
Exception when a disallowed or unallocated codepoint is used
Exception when the codepoint is not valid in the context it is used
Re-map the characters in the string according to UTS46 processing.

---



---



---



---


Given a list of integers, made up of (hopefully) a small number of long runs
of consecutive integers, compute a representation of the form
((start1, end1), (start2, end2) ...). Then answer the question "was x present
in the original list?" in time O(log(# runs)).

Represent a list of integers as a sequence of ranges:
    ((start_0, end_0), (start_1, end_1), ...), such that the original
    integers are exactly those x such that start_i <= x < end_i for some i.

    Ranges are encoded as single integers (start << 32 | end), not as tuples.
    
Determine if `int_` falls into one of the ranges in `ranges`.

---

IDNA Mapping Table from UTS46.

---



---



---


certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem or its contents.


---



---



---


    Convenience mixin for classes who implement a :meth:`urlopen` method, such
    as :class:`urllib3.HTTPConnectionPool` and
    :class:`urllib3.PoolManager`.

    Provides behavior for making common types of HTTP request methods and
    decides which type of request field encoding to use.

    Specifically,

    :meth:`.request_encode_url` is for sending requests whose fields are
    encoded in the URL (such as GET, HEAD, DELETE).

    :meth:`.request_encode_body` is for sending requests whose fields are
    encoded in the *body* of the request using multipart or www-form-urlencoded
    (such as for POST, PUT, PATCH).

    :meth:`.request` is for making any kind of request, it will look up the
    appropriate encoding format and use one of the above two methods to make
    the request.

    Initializer parameters:

    :param headers:
        Headers to include with all requests, unless other headers are given
        explicitly.
    

        Make a request using :meth:`urlopen` with the appropriate encoding of
        ``fields`` based on the ``method`` used.

        This is a convenience method that requires the least amount of manual
        effort. It can be used in most situations, while still having the
        option to drop down to more specific methods when necessary, such as
        :meth:`request_encode_url`, :meth:`request_encode_body`,
        or even the lowest level :meth:`urlopen`.

        :param method:
            HTTP request method (such as GET, POST, PUT, etc.)

        :param url:
            The URL to perform the request on.

        :param body:
            Data to send in the request body, either :class:`str`, :class:`bytes`,
            an iterable of :class:`str`/:class:`bytes`, or a file-like object.

        :param fields:
            Data to encode and send in the URL or request body, depending on ``method``.

        :param headers:
            Dictionary of custom headers to send, such as User-Agent,
            If-None-Match, etc. If None, pool headers are used. If provided,
            these headers completely replace any pool-specific headers.

        :param json:
            Data to encode and send as JSON with UTF-encoded in the request body.
            The ``"Content-Type"`` header will be set to ``"application/json"``
            unless specified otherwise.
        

        Make a request using :meth:`urlopen` with the ``fields`` encoded in
        the url. This is useful for request methods like GET, HEAD, DELETE, etc.

        :param method:
            HTTP request method (such as GET, POST, PUT, etc.)

        :param url:
            The URL to perform the request on.

        :param fields:
            Data to encode and send in the URL.

        :param headers:
            Dictionary of custom headers to send, such as User-Agent,
            If-None-Match, etc. If None, pool headers are used. If provided,
            these headers completely replace any pool-specific headers.
        

        Make a request using :meth:`urlopen` with the ``fields`` encoded in
        the body. This is useful for request methods like POST, PUT, PATCH, etc.

        When ``encode_multipart=True`` (default), then
        :func:`urllib3.encode_multipart_formdata` is used to encode
        the payload with the appropriate content type. Otherwise
        :func:`urllib.parse.urlencode` is used with the
        'application/x-www-form-urlencoded' content type.

        Multipart encoding must be used when posting files, and it's reasonably
        safe to use it in other times too. However, it may break request
        signing, such as with OAuth.

        Supports an optional ``fields`` parameter of key/value strings AND
        key/filetuple. A filetuple is a (filename, data, MIME type) tuple where
        the MIME type is optional. For example::

            fields = {
                'foo': 'bar',
                'fakefile': ('foofile.txt', 'contents of foofile'),
                'realfile': ('barfile.txt', open('realfile').read()),
                'typedfile': ('bazfile.bin', open('bazfile').read(),
                              'image/jpeg'),
                'nonamefile': 'contents of nonamefile field',
            }

        When uploading a file, providing a filename (the first parameter of the
        tuple) is optional but recommended to best mimic behavior of browsers.

        Note that if ``headers`` are supplied, the 'Content-Type' header will
        be overwritten because it depends on the dynamic random boundary string
        which is used to compose the body of the request. The random boundary
        string can be explicitly set with the ``multipart_boundary`` parameter.

        :param method:
            HTTP request method (such as GET, POST, PUT, etc.)

        :param url:
            The URL to perform the request on.

        :param fields:
            Data to encode and send in the request body.

        :param headers:
            Dictionary of custom headers to send, such as User-Agent,
            If-None-Match, etc. If None, pool headers are used. If provided,
            these headers completely replace any pool-specific headers.

        :param encode_multipart:
            If True, encode the ``fields`` using the multipart/form-data MIME
            format.

        :param multipart_boundary:
            If not specified, then a random boundary will be generated using
            :func:`urllib3.filepost.choose_boundary`.
        

---

Base exception used by this module.
Base warning used by this module.
Base exception for errors caused within a pool.
Base exception for PoolErrors that have associated URLs.
Raised when SSL certificate fails in an HTTPS connection.
Raised when the connection to a proxy fails.
Raised when automatic decoding based on Content-Type fails.
Raised when something unexpected happens mid-request/response.
Raised when the maximum number of retries is exceeded.

    :param pool: The connection pool
    :type pool: :class:`~urllib3.connectionpool.HTTPConnectionPool`
    :param str url: The requested Url
    :param reason: The underlying error
    :type reason: :class:`Exception`

    
Raised when an existing pool gets a request for a foreign host.
Raised when passing an invalid state to a timeout
Raised when a socket timeout error occurs.

    Catching this error will catch both :exc:`ReadTimeoutErrors
    <ReadTimeoutError>` and :exc:`ConnectTimeoutErrors <ConnectTimeoutError>`.
    
Raised when a socket timeout occurs while receiving data from a server
Raised when a socket timeout occurs while connecting to a server
Raised when we fail to establish a new connection. Usually ECONNREFUSED.
Raised when host name resolution fails.
Raised when a pool runs out of connections and no more are allowed.
Raised when we try to add a connection to a full pool in blocking mode.
Raised when a request enters a pool after the pool has been closed.
Raised when there is something wrong with a given URL input.
Raised when get_host or similar fails to parse the URL input.
Raised when a URL input has an unsupported scheme.
Used as a container for an error reason supplied in a MaxRetryError.
Warned when performing security reducing actions
Warned when making an unverified HTTPS request.
Warned when using unsupported SSL library
Warned when system time is suspected to be wrong
Warned when certain TLS/SSL configuration is not available on a platform.

    Warned when an attempt is made to import a module with missing optional
    dependencies.
    
Response needs to be chunked in order to read it as chunks.

    Body should be :class:`http.client.HTTPResponse` like
    (have an fp attribute which returns raw chunks) for read_chunked().
    

    Response length doesn't match expected Content-Length

    Subclass of :class:`http.client.IncompleteRead` to allow int value
    for ``partial`` to avoid creating large objects on streamed reads.
    
Invalid chunk length in a chunked response.
The header provided was somehow invalid.
ProxyManager does not support the supplied scheme
Fetching HTTPS resources through HTTPS proxies is unsupported
Raised by assert_header_parsing, but we convert it to a log.warning statement.
urllib3 encountered an error when trying to rewind a body

---


    Guess the "Content-Type" of a file.

    :param filename:
        The filename to guess the "Content-Type" of using :mod:`mimetypes`.
    :param default:
        If no "Content-Type" can be guessed, default to `default`.
    

    Helper function to format and quote a single header parameter using the
    strategy defined in RFC 2231.

    Particularly useful for header parameters which might contain
    non-ASCII values, like file names. This follows
    `RFC 2388 Section 4.4 <https://tools.ietf.org/html/rfc2388#section-4.4>`_.

    :param name:
        The name of the parameter, a string expected to be ASCII only.
    :param value:
        The value of the parameter, provided as ``bytes`` or `str``.
    :returns:
        An RFC-2231-formatted unicode string.

    .. deprecated:: 2.0.0
        Will be removed in urllib3 v2.1.0. This is not valid for
        ``multipart/form-data`` header parameters.
    

    Format and quote a single multipart header parameter.

    This follows the `WHATWG HTML Standard`_ as of 2021/06/10, matching
    the behavior of current browser and curl versions. Values are
    assumed to be UTF-8. The ``\\n``, ``\\r``, and ``"`` characters are
    percent encoded.

    .. _WHATWG HTML Standard:
        https://html.spec.whatwg.org/multipage/
        form-control-infrastructure.html#multipart-form-data

    :param name:
        The name of the parameter, an ASCII-only ``str``.
    :param value:
        The value of the parameter, a ``str`` or UTF-8 encoded
        ``bytes``.
    :returns:
        A string ``name="value"`` with the escaped value.

    .. versionchanged:: 2.0.0
        Matches the WHATWG HTML Standard as of 2021/06/10. Control
        characters are no longer percent encoded.

    .. versionchanged:: 2.0.0
        Renamed from ``format_header_param_html5`` and
        ``format_header_param``. The old names will be removed in
        urllib3 v2.1.0.
    

    .. deprecated:: 2.0.0
        Renamed to :func:`format_multipart_header_param`. Will be
        removed in urllib3 v2.1.0.
    

    .. deprecated:: 2.0.0
        Renamed to :func:`format_multipart_header_param`. Will be
        removed in urllib3 v2.1.0.
    

    A data container for request body parameters.

    :param name:
        The name of this request field. Must be unicode.
    :param data:
        The data/value body.
    :param filename:
        An optional filename of the request field. Must be unicode.
    :param headers:
        An optional dict-like object of headers to initially use for the field.

    .. versionchanged:: 2.0.0
        The ``header_formatter`` parameter is deprecated and will
        be removed in urllib3 v2.1.0.
    

        A :class:`~urllib3.fields.RequestField` factory from old-style tuple parameters.

        Supports constructing :class:`~urllib3.fields.RequestField` from
        parameter of key/value strings AND key/filetuple. A filetuple is a
        (filename, data, MIME type) tuple where the MIME type is optional.
        For example::

            'foo': 'bar',
            'fakefile': ('foofile.txt', 'contents of foofile'),
            'realfile': ('barfile.txt', open('realfile').read()),
            'typedfile': ('bazfile.bin', open('bazfile').read(), 'image/jpeg'),
            'nonamefile': 'contents of nonamefile field',

        Field names and filenames must be unicode.
        

        Override this method to change how each multipart header
        parameter is formatted. By default, this calls
        :func:`format_multipart_header_param`.

        :param name:
            The name of the parameter, an ASCII-only ``str``.
        :param value:
            The value of the parameter, a ``str`` or UTF-8 encoded
            ``bytes``.

        :meta public:
        

        Helper function to format and quote a single header.

        Useful for single headers that are composed of multiple items. E.g.,
        'Content-Disposition' fields.

        :param header_parts:
            A sequence of (k, v) tuples or a :class:`dict` of (k, v) to format
            as `k1="v1"; k2="v2"; ...`.
        

        Renders the headers for this request field.
        

        Makes this request field into a multipart request field.

        This method overrides "Content-Disposition", "Content-Type" and
        "Content-Location" headers to the request parameter.

        :param content_disposition:
            The 'Content-Disposition' of the request body. Defaults to 'form-data'
        :param content_type:
            The 'Content-Type' of the request body.
        :param content_location:
            The 'Content-Location' of the request body.

        

---


    Based on :class:`http.client.HTTPConnection` but provides an extra constructor
    backwards-compatibility layer between older and newer Pythons.

    Additional keyword parameters are used to configure attributes of the connection.
    Accepted parameters include:

    - ``source_address``: Set the source address for the current connection.
    - ``socket_options``: Set specific options on the underlying socket. If not specified, then
      defaults are loaded from ``HTTPConnection.default_socket_options`` which includes disabling
      Nagle's algorithm (sets TCP_NODELAY to 1) unless the connection is behind a proxy.

      For example, if you wish to enable TCP Keep Alive in addition to the defaults,
      you might pass:

      .. code-block:: python

         HTTPConnection.default_socket_options + [
             (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
         ]

      Or you may want to disable the defaults by passing an empty list (e.g., ``[]``).
    

        Getter method to remove any trailing dots that indicate the hostname is an FQDN.

        In general, SSL certificates don't include the trailing dot indicating a
        fully-qualified domain name, and thus, they don't validate properly when
        checked against a domain name that includes the dot. In addition, some
        servers may not expect to receive the trailing dot when provided.

        However, the hostname with trailing dot is critical to DNS resolution; doing a
        lookup with the trailing dot will properly only resolve the appropriate FQDN,
        whereas a lookup without a trailing dot will search the system's search domain
        list. Thus, it's important to keep the original host around for use only in
        those cases where it's appropriate (i.e., when doing DNS lookup to establish the
        actual TCP connection across which we're going to send HTTP requests).
        

        Setter for the `host` property.

        We assume that only urllib3 uses the _dns_host attribute; httplib itself
        only uses `host`, and it seems reasonable that other libraries follow suit.
        
Establish a socket connection and set nodelay settings on it.

        :return: New socket connection.
        

        Return True if a forwarding proxy is configured, else return False
        



        Alternative to the common request method, which sends the
        body with chunked encoding and not as one block
        

        Get the response from the server.

        If the HTTPConnection is in the correct state, returns an instance of HTTPResponse or of whatever object is returned by the response_class variable.

        If a request has not been sent or if a previous response has not be handled, ResponseNotReady is raised. If the HTTP response indicates that the connection should be closed, then it will be closed before the response is returned. When the connection is closed, the underlying socket is closed.
        

    Many of the parameters to this constructor are passed to the underlying SSL
    socket by means of :py:func:`urllib3.util.ssl_wrap_socket`.
    

        This method should only be called once, before the connection is used.
        

        Establish a TLS connection to the proxy using the provided SSL context.
        

    Wrapped socket and whether the connection is
    verified after the TLS handshake
    
Logic for constructing an SSLContext from all TLS parameters, passing
    that down into ssl_wrap_socket, and then doing certificate verification
    either via hostname or fingerprint. This function exists to guarantee
    that both proxies and targets have the same behavior when connecting via TLS.
    
Used to detect a failed ConnectionCls import.
Returns the URL from a given connection. This is mainly used for testing and logging.

---


    All known keyword arguments that could be provided to the pool manager, its
    pools, or the underlying connections.

    All custom key schemes should include the fields in this key at a minimum.
    

    Create a pool key out of a request context dictionary.

    According to RFC 3986, both the scheme and host are case-insensitive.
    Therefore, this function normalizes both before constructing the pool
    key for an HTTPS request. If you wish to change this behaviour, provide
    alternate callables to ``key_fn_by_scheme``.

    :param key_class:
        The class to use when constructing the key. This should be a namedtuple
        with the ``scheme`` and ``host`` keys at a minimum.
    :type  key_class: namedtuple
    :param request_context:
        A dictionary-like object that contain the context for a request.
    :type  request_context: dict

    :return: A namedtuple that can be used as a connection pool key.
    :rtype:  PoolKey
    

    Allows for arbitrary requests while transparently keeping track of
    necessary connection pools for you.

    :param num_pools:
        Number of connection pools to cache before discarding the least
        recently used pool.

    :param headers:
        Headers to include with all requests, unless other headers are given
        explicitly.

    :param \\**connection_pool_kw:
        Additional parameters are used to create fresh
        :class:`urllib3.connectionpool.ConnectionPool` instances.

    Example:

    .. code-block:: python

        import urllib3

        http = urllib3.PoolManager(num_pools=2)

        resp1 = http.request("GET", "https://google.com/")
        resp2 = http.request("GET", "https://google.com/mail")
        resp3 = http.request("GET", "https://yahoo.com/")

        print(len(http.pools))
        # 2

    

        Create a new :class:`urllib3.connectionpool.ConnectionPool` based on host, port, scheme, and
        any additional pool keyword arguments.

        If ``request_context`` is provided, it is provided as keyword arguments
        to the pool class used. This method is used to actually create the
        connection pools handed out by :meth:`connection_from_url` and
        companion methods. It is intended to be overridden for customization.
        

        Empty our store of pools and direct them all to close.

        This will not affect in-flight connections, but they will not be
        re-used after completion.
        

        Get a :class:`urllib3.connectionpool.ConnectionPool` based on the host, port, and scheme.

        If ``port`` isn't given, it will be derived from the ``scheme`` using
        ``urllib3.connectionpool.port_by_scheme``. If ``pool_kwargs`` is
        provided, it is merged with the instance's ``connection_pool_kw``
        variable and used to create the new connection pool, if one is
        needed.
        

        Get a :class:`urllib3.connectionpool.ConnectionPool` based on the request context.

        ``request_context`` must at least contain the ``scheme`` key and its
        value must be a key in ``key_fn_by_scheme`` instance variable.
        

        Get a :class:`urllib3.connectionpool.ConnectionPool` based on the provided pool key.

        ``pool_key`` should be a namedtuple that only contains immutable
        objects. At a minimum it must have the ``scheme``, ``host``, and
        ``port`` fields.
        

        Similar to :func:`urllib3.connectionpool.connection_from_url`.

        If ``pool_kwargs`` is not provided and a new pool needs to be
        constructed, ``self.connection_pool_kw`` is used to initialize
        the :class:`urllib3.connectionpool.ConnectionPool`. If ``pool_kwargs``
        is provided, it is used instead. Note that if a new pool does not
        need to be created for the request, the provided ``pool_kwargs`` are
        not used.
        

        Merge a dictionary of override values for self.connection_pool_kw.

        This does not modify self.connection_pool_kw and returns a new dict.
        Any keys in the override dictionary with a value of ``None`` are
        removed from the merged dictionary.
        

        Indicates if the proxy requires the complete destination URL in the
        request.  Normally this is only needed when not using an HTTP CONNECT
        tunnel.
        

        Same as :meth:`urllib3.HTTPConnectionPool.urlopen`
        with custom cross-host redirect logic and only sends the request-uri
        portion of the ``url``.

        The given ``url`` parameter must be absolute, such that an appropriate
        :class:`urllib3.connectionpool.ConnectionPool` can be chosen for it.
        

    Behaves just like :class:`PoolManager`, but sends all requests through
    the defined proxy, using the CONNECT method for HTTPS URLs.

    :param proxy_url:
        The URL of the proxy to be used.

    :param proxy_headers:
        A dictionary containing headers that will be sent to the proxy. In case
        of HTTP they are being sent with each request, while in the
        HTTPS/CONNECT case they are sent only once. Could be used for proxy
        authentication.

    :param proxy_ssl_context:
        The proxy SSL context is used to establish the TLS connection to the
        proxy when using HTTPS proxies.

    :param use_forwarding_for_https:
        (Defaults to False) If set to True will forward requests to the HTTPS
        proxy to be made on behalf of the client instead of creating a TLS
        tunnel via the CONNECT method. **Enabling this flag means that request
        and response headers and content will be visible from the HTTPS proxy**
        whereas tunneling keeps request and response headers and content
        private.  IP address, target hostname, SNI, and port are always visible
        to an HTTPS proxy even when this flag is disabled.

    :param proxy_assert_hostname:
        The hostname of the certificate to verify against.

    :param proxy_assert_fingerprint:
        The fingerprint of the certificate to verify against.

    Example:

    .. code-block:: python

        import urllib3

        proxy = urllib3.ProxyManager("https://localhost:3128/")

        resp1 = proxy.request("GET", "https://google.com/")
        resp2 = proxy.request("GET", "https://httpbin.org/")

        print(len(proxy.pools))
        # 1

        resp3 = proxy.request("GET", "https://httpbin.org/")
        resp4 = proxy.request("GET", "https://twitter.com/")

        print(len(proxy.pools))
        # 3

    

        Sets headers needed by proxies: specifically, the Accept and Host
        headers. Only sets headers not provided by the user.
        

---


    Our embarrassingly-simple replacement for mimetools.choose_boundary.
    

    Iterate over fields.

    Supports list of (k, v) tuples and dicts, and lists of
    :class:`~urllib3.fields.RequestField`.

    

    Encode a dictionary of ``fields`` using the multipart/form-data MIME format.

    :param fields:
        Dictionary of fields or list of (key, :class:`~urllib3.fields.RequestField`).
        Values are processed by :func:`urllib3.fields.RequestField.from_tuples`.

    :param boundary:
        If not specified, then a random boundary will be generated using
        :func:`urllib3.filepost.choose_boundary`.
    

---


    From RFC7231:
        If one or more encodings have been applied to a representation, the
        sender that applied the encodings MUST generate a Content-Encoding
        header field that lists the content codings in the order in which
        they were applied.
    
Memory-efficient bytes buffer

    To return decoded data in read() and still follow the BufferedIOBase API, we need a
    buffer to always return the correct amount of bytes.

    This buffer should be filled using calls to put()

    Our maximum memory usage is determined by the sum of the size of:

     * self.buffer, which contains the full data
     * the largest chunk that we will copy in get()

    The worst case scenario is a single chunk, in which case we'll make a full copy of
    the data inside get().
    

        Should we redirect and where to?

        :returns: Truthy redirect location string if we got a redirect status
            code and valid location. ``None`` if redirect status and no
            location. ``False`` if not a redirect status code.
        

        Deserializes the body of the HTTP response as a Python object.

        The body of the HTTP response must be encoded using UTF-8, as per
        `RFC 8529 Section 8.1 <https://www.rfc-editor.org/rfc/rfc8259#section-8.1>`_.

        To use a custom JSON decoder pass the result of :attr:`HTTPResponse.data` to
        your custom decoder instead.

        If the body of the HTTP response is not decodable to UTF-8, a
        `UnicodeDecodeError` will be raised. If the body of the HTTP response is not a
        valid JSON document, a `json.JSONDecodeError` will be raised.

        Read more :ref:`here <json_content>`.

        :returns: The body of the HTTP response as a Python object.
        

        Set-up the _decoder attribute if necessary.
        

        Decode the data passed in and potentially flush the decoder.
        

        Flushes the decoder. Should only be called if the decoder is actually
        being used.
        

    HTTP Response container.

    Backwards-compatible with :class:`http.client.HTTPResponse` but the response ``body`` is
    loaded and decoded on-demand when the ``data`` property is accessed.  This
    class is also compatible with the Python standard library's :mod:`io`
    module, and can hence be treated as a readable object in the context of that
    framework.

    Extra parameters for behaviour not present in :class:`http.client.HTTPResponse`:

    :param preload_content:
        If True, the response's body will be preloaded during construction.

    :param decode_content:
        If True, will attempt to decode the body based on the
        'content-encoding' header.

    :param original_response:
        When this HTTPResponse wrapper is generated from an :class:`http.client.HTTPResponse`
        object, it's convenient to include the original for debug purposes. It's
        otherwise unused.

    :param retries:
        The retries contains the last :class:`~urllib3.util.retry.Retry` that
        was used during the request.

    :param enforce_content_length:
        Enforce content length checking. Body returned by server must match
        value of Content-Length header, if present. Otherwise, raise error.
    

        Read and discard any remaining HTTP response data in the response connection.

        Unread data in the HTTPResponse connection blocks the connection from being released back to the pool.
        

        Obtain the number of bytes pulled over the wire so far. May differ from
        the amount of content returned by :meth:``urllib3.response.HTTPResponse.read``
        if bytes are encoded on the wire (e.g, compressed).
        

        Set initial length value for Response content if available.
        

        Catch low-level python exceptions, instead re-raising urllib3
        variants, so that low-level exceptions are not leaked in the
        high-level api.

        On exit, release the connection back to the pool.
        

        Read a response with the thought that reading the number of bytes
        larger than can fit in a 32-bit int at a time via SSL in some
        known cases leads to an overflow error that has to be prevented
        if `amt` or `self.length_remaining` indicate that a problem may
        happen.

        The known cases:
          * 3.8 <= CPython < 3.9.7 because of a bug
            https://github.com/urllib3/urllib3/issues/2513#issuecomment-1152559900.
          * urllib3 injected with pyOpenSSL-backed SSL-support.
          * CPython < 3.10 only when `amt` does not fit 32-bit int.
        

        Reads `amt` of bytes from the socket.
        

        Similar to :meth:`http.client.HTTPResponse.read`, but with two additional
        parameters: ``decode_content`` and ``cache_content``.

        :param amt:
            How much of the content to read. If specified, caching is skipped
            because it doesn't make sense to cache partial content as the full
            response.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.

        :param cache_content:
            If True, will save the returned data such that the same result is
            returned despite of the state of the underlying file object. This
            is useful if you want the ``.data`` property to continue working
            after having ``.read()`` the file object. (Overridden if ``amt`` is
            set.)
        

        Similar to ``http.client.HTTPResponse.read1`` and documented
        in :meth:`io.BufferedReader.read1`, but with an additional parameter:
        ``decode_content``.

        :param amt:
            How much of the content to read.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.
        

        A generator wrapper for the read() method. A call will block until
        ``amt`` bytes have been read from the connection or until the
        connection is closed.

        :param amt:
            How much of the content to read. The generator will return up to
            much data per iteration, but may return less. This is particularly
            likely when using compressed data. However, the empty string will
            never be returned.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.
        

        Checks if the underlying file-like object looks like a
        :class:`http.client.HTTPResponse` object. We do this by testing for
        the fp attribute. If it is present we assume it returns raw chunks as
        processed by read_chunked().
        

        Similar to :meth:`HTTPResponse.read`, but with an additional
        parameter: ``decode_content``.

        :param amt:
            How much of the content to read. If specified, caching is skipped
            because it doesn't make sense to cache partial content as the full
            response.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.
        

        Returns the URL that was the source of this response.
        If the request that generated this response redirected, this method
        will return the final redirect location.
        

---



---


    Provides a thread-safe dict-like container which maintains up to
    ``maxsize`` keys while throwing away the least-recently-used keys beyond
    ``maxsize``.

    :param maxsize:
        Maximum number of recent elements to retain.

    :param dispose_func:
        Every time an item is evicted from the container,
        ``dispose_func(value)`` is called.  Callback which will get called
    

    HTTPHeaderDict is unusual for a Mapping[str, str] in that it has two modes of
    address.

    If we directly try to get an item with a particular name, we will get a string
    back that is the concatenated version of all the values:

    >>> d['X-Header-Name']
    'Value1, Value2, Value3'

    However, if we iterate over an HTTPHeaderDict's items, we will optionally combine
    these values based on whether combine=True was called when building up the dictionary

    >>> d = HTTPHeaderDict({"A": "1", "B": "foo"})
    >>> d.add("A", "2", combine=True)
    >>> d.add("B", "bar")
    >>> list(d.items())
    [
        ('A', '1, 2'),
        ('B', 'foo'),
        ('B', 'bar'),
    ]

    This class conforms to the interface required by the MutableMapping ABC while
    also giving us the nonstandard iteration behavior we want; items with duplicate
    keys, ordered by time of first insertion.
    

    :param headers:
        An iterable of field-value pairs. Must not contain multiple field names
        when compared case-insensitively.

    :param kwargs:
        Additional field-value pairs to pass in to ``dict.update``.

    A ``dict`` like container for storing HTTP Headers.

    Field names are stored and compared case-insensitively in compliance with
    RFC 7230. Iteration provides the first case-sensitive key seen for each
    case-insensitive pair.

    Using ``__setitem__`` syntax overwrites fields that compare equal
    case-insensitively in order to maintain ``dict``'s api. For fields that
    compare equal, instead create a new ``HTTPHeaderDict`` and use ``.add``
    in a loop.

    If multiple fields that are equal case-insensitively are passed to the
    constructor or ``.update``, the behavior is undefined and some will be
    lost.

    >>> headers = HTTPHeaderDict()
    >>> headers.add('Set-Cookie', 'foo=bar')
    >>> headers.add('set-cookie', 'baz=quxx')
    >>> headers['content-length'] = '7'
    >>> headers['SET-cookie']
    'foo=bar, baz=quxx'
    >>> headers['Content-Length']
    '7'
    
Adds a (name, value) pair, doesn't overwrite the value if it already
        exists.

        If this is called with combine=True, instead of adding a new header value
        as a distinct item during iteration, this will instead append the value to
        any existing header value with a comma. If no existing header value exists
        for the key, then the value will simply be added, ignoring the combine parameter.

        >>> headers = HTTPHeaderDict(foo='bar')
        >>> headers.add('Foo', 'baz')
        >>> headers['foo']
        'bar, baz'
        >>> list(headers.items())
        [('foo', 'bar'), ('foo', 'baz')]
        >>> headers.add('foo', 'quz', combine=True)
        >>> list(headers.items())
        [('foo', 'bar, baz, quz')]
        
Generic import function for any type of header-like object.
        Adapted version of MutableMapping.update in order to insert items
        with self.add instead of self.__setitem__
        
Returns a list of all the values for the named field. Returns an
        empty list if the key doesn't exist.

        Remove content-specific header fields before changing the request
        method to GET or HEAD according to RFC 9110, Section 15.4.
        
Iterate over all header lines, including duplicate ones.
Iterate over all headers, merging duplicate ones together.

---


Python HTTP library with thread-safe connection pooling, file post support, user friendly, and more


    Helper for quickly adding a StreamHandler to the logger. Useful for
    debugging.

    Returns the handler after adding it.
    

    Helper for quickly disabling all urllib3 warnings.
    

    A convenience, top-level request method. It uses a module-global ``PoolManager`` instance.
    Therefore, its side effects could be shared across dependencies relying on it.
    To avoid side effects create a new ``PoolManager`` instance and use it instead.
    The method does not accept low-level ``**urlopen_kw`` keyword arguments.

    :param method:
        HTTP request method (such as GET, POST, PUT, etc.)

    :param url:
        The URL to perform the request on.

    :param body:
        Data to send in the request body, either :class:`str`, :class:`bytes`,
        an iterable of :class:`str`/:class:`bytes`, or a file-like object.

    :param fields:
        Data to encode and send in the request body.

    :param headers:
        Dictionary of custom headers to send, such as User-Agent,
        If-None-Match, etc.

    :param bool preload_content:
        If True, the response's body will be preloaded into memory.

    :param bool decode_content:
        If True, will attempt to decode the body based on the
        'content-encoding' header.

    :param redirect:
        If True, automatically handle redirects (status codes 301, 302,
        303, 307, 308). Each redirect counts as a retry. Disabling retries
        will disable redirect, too.

    :param retries:
        Configure the number of retries to allow before raising a
        :class:`~urllib3.exceptions.MaxRetryError` exception.

        If ``None`` (default) will retry 3 times, see ``Retry.DEFAULT``. Pass a
        :class:`~urllib3.util.retry.Retry` object for fine-grained control
        over different types of retries.
        Pass an integer number to retry connection errors that many times,
        but no other types of errors. Pass zero to never retry.

        If ``False``, then retries are disabled and any exception is raised
        immediately. Also, instead of raising a MaxRetryError on redirects,
        the redirect response will be returned.

    :type retries: :class:`~urllib3.util.retry.Retry`, False, or an int.

    :param timeout:
        If specified, overrides the default timeout for this one
        request. It may be a float (in seconds) or an instance of
        :class:`urllib3.util.Timeout`.

    :param json:
        Data to encode and send as JSON with UTF-encoded in the request body.
        The ``"Content-Type"`` header will be set to ``"application/json"``
        unless specified otherwise.
    

---

Whether the connection either is brand new or has been previously closed.
            If this property is True then both ``is_connected`` and ``has_connected_to_proxy``
            properties must be False.
            
Whether the connection is actively connected to any origin (proxy or target)
Whether the connection has successfully connected to its proxy.
            This returns False if no proxy is in use. Used to determine whether
            errors are coming from the proxy layer or from tunnelling to the target origin.
            

---


    Base class for all connection pools, such as
    :class:`.HTTPConnectionPool` and :class:`.HTTPSConnectionPool`.

    .. note::
       ConnectionPool.urlopen() does not normalize or percent-encode target URIs
       which is useful if your target server doesn't support percent-encoded
       target URIs.
    

        Close all pooled connections and disable the pool.
        

    Thread-safe connection pool for one host.

    :param host:
        Host used for this HTTP Connection (e.g. "localhost"), passed into
        :class:`http.client.HTTPConnection`.

    :param port:
        Port used for this HTTP Connection (None is equivalent to 80), passed
        into :class:`http.client.HTTPConnection`.

    :param timeout:
        Socket timeout in seconds for each individual connection. This can
        be a float or integer, which sets the timeout for the HTTP request,
        or an instance of :class:`urllib3.util.Timeout` which gives you more
        fine-grained control over request timeouts. After the constructor has
        been parsed, this is always a `urllib3.util.Timeout` object.

    :param maxsize:
        Number of connections to save that can be reused. More than 1 is useful
        in multithreaded situations. If ``block`` is set to False, more
        connections will be created but they will not be saved once they've
        been used.

    :param block:
        If set to True, no more than ``maxsize`` connections will be used at
        a time. When no free connections are available, the call will block
        until a connection has been released. This is a useful side effect for
        particular multithreaded situations where one does not want to use more
        than maxsize connections per host to prevent flooding.

    :param headers:
        Headers to include with all requests, unless other headers are given
        explicitly.

    :param retries:
        Retry configuration to use by default with requests in this pool.

    :param _proxy:
        Parsed proxy URL, should not be used directly, instead, see
        :class:`urllib3.ProxyManager`

    :param _proxy_headers:
        A dictionary with proxy headers, should not be used directly,
        instead, see :class:`urllib3.ProxyManager`

    :param \\**conn_kw:
        Additional parameters are used to create fresh :class:`urllib3.connection.HTTPConnection`,
        :class:`urllib3.connection.HTTPSConnection` instances.
    

        Return a fresh :class:`HTTPConnection`.
        

        Get a connection. Will return a pooled connection if one is available.

        If no connections are available and :prop:`.block` is ``False``, then a
        fresh connection is returned.

        :param timeout:
            Seconds to wait before giving up and raising
            :class:`urllib3.exceptions.EmptyPoolError` if the pool is empty and
            :prop:`.block` is ``True``.
        

        Put a connection back into the pool.

        :param conn:
            Connection object for the current host and port as returned by
            :meth:`._new_conn` or :meth:`._get_conn`.

        If the pool is already full, the connection is closed and discarded
        because we exceeded maxsize. If connections are discarded frequently,
        then maxsize should be increased.

        If the pool is closed, then the connection will be closed and discarded.
        

        Called right before a request is made, after the socket is created.
        
Helper that always returns a :class:`urllib3.util.Timeout`
Is the error actually a timeout? Will raise a ReadTimeout or pass

        Perform a request on a given urllib connection object taken from our
        pool.

        :param conn:
            a connection from one of our connection pools

        :param method:
            HTTP request method (such as GET, POST, PUT, etc.)

        :param url:
            The URL to perform the request on.

        :param body:
            Data to send in the request body, either :class:`str`, :class:`bytes`,
            an iterable of :class:`str`/:class:`bytes`, or a file-like object.

        :param headers:
            Dictionary of custom headers to send, such as User-Agent,
            If-None-Match, etc. If None, pool headers are used. If provided,
            these headers completely replace any pool-specific headers.

        :param retries:
            Configure the number of retries to allow before raising a
            :class:`~urllib3.exceptions.MaxRetryError` exception.

            Pass ``None`` to retry until you receive a response. Pass a
            :class:`~urllib3.util.retry.Retry` object for fine-grained control
            over different types of retries.
            Pass an integer number to retry connection errors that many times,
            but no other types of errors. Pass zero to never retry.

            If ``False``, then retries are disabled and any exception is raised
            immediately. Also, instead of raising a MaxRetryError on redirects,
            the redirect response will be returned.

        :type retries: :class:`~urllib3.util.retry.Retry`, False, or an int.

        :param timeout:
            If specified, overrides the default timeout for this one
            request. It may be a float (in seconds) or an instance of
            :class:`urllib3.util.Timeout`.

        :param chunked:
            If True, urllib3 will send the body using chunked transfer
            encoding. Otherwise, urllib3 will send the body using the standard
            content-length form. Defaults to False.

        :param response_conn:
            Set this to ``None`` if you will handle releasing the connection or
            set the connection to have the response release it.

        :param preload_content:
          If True, the response's body will be preloaded during construction.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.

        :param enforce_content_length:
            Enforce content length checking. Body returned by server must match
            value of Content-Length header, if present. Otherwise, raise error.
        

        Close all pooled connections and disable the pool.
        

        Check if the given ``url`` is a member of the same host as this
        connection pool.
        

        Get a connection from the pool and perform an HTTP request. This is the
        lowest level call for making a request, so you'll need to specify all
        the raw details.

        .. note::

           More commonly, it's appropriate to use a convenience method
           such as :meth:`request`.

        .. note::

           `release_conn` will only behave as expected if
           `preload_content=False` because we want to make
           `preload_content=False` the default behaviour someday soon without
           breaking backwards compatibility.

        :param method:
            HTTP request method (such as GET, POST, PUT, etc.)

        :param url:
            The URL to perform the request on.

        :param body:
            Data to send in the request body, either :class:`str`, :class:`bytes`,
            an iterable of :class:`str`/:class:`bytes`, or a file-like object.

        :param headers:
            Dictionary of custom headers to send, such as User-Agent,
            If-None-Match, etc. If None, pool headers are used. If provided,
            these headers completely replace any pool-specific headers.

        :param retries:
            Configure the number of retries to allow before raising a
            :class:`~urllib3.exceptions.MaxRetryError` exception.

            If ``None`` (default) will retry 3 times, see ``Retry.DEFAULT``. Pass a
            :class:`~urllib3.util.retry.Retry` object for fine-grained control
            over different types of retries.
            Pass an integer number to retry connection errors that many times,
            but no other types of errors. Pass zero to never retry.

            If ``False``, then retries are disabled and any exception is raised
            immediately. Also, instead of raising a MaxRetryError on redirects,
            the redirect response will be returned.

        :type retries: :class:`~urllib3.util.retry.Retry`, False, or an int.

        :param redirect:
            If True, automatically handle redirects (status codes 301, 302,
            303, 307, 308). Each redirect counts as a retry. Disabling retries
            will disable redirect, too.

        :param assert_same_host:
            If ``True``, will make sure that the host of the pool requests is
            consistent else will raise HostChangedError. When ``False``, you can
            use the pool on an HTTP proxy and request foreign hosts.

        :param timeout:
            If specified, overrides the default timeout for this one
            request. It may be a float (in seconds) or an instance of
            :class:`urllib3.util.Timeout`.

        :param pool_timeout:
            If set and the pool is set to block=True, then this method will
            block for ``pool_timeout`` seconds and raise EmptyPoolError if no
            connection is available within the time period.

        :param bool preload_content:
            If True, the response's body will be preloaded into memory.

        :param bool decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.

        :param release_conn:
            If False, then the urlopen call will not release the connection
            back into the pool once a response is received (but will release if
            you read the entire contents of the response such as when
            `preload_content=True`). This is useful if you're not preloading
            the response's content immediately. You will need to call
            ``r.release_conn()`` on the response ``r`` to return the connection
            back into the pool. If None, it takes the value of ``preload_content``
            which defaults to ``True``.

        :param bool chunked:
            If True, urllib3 will send the body using chunked transfer
            encoding. Otherwise, urllib3 will send the body using the standard
            content-length form. Defaults to False.

        :param int body_pos:
            Position to seek to in file-like body in the event of a retry or
            redirect. Typically this won't need to be set because urllib3 will
            auto-populate the value when needed.
        

    Same as :class:`.HTTPConnectionPool`, but HTTPS.

    :class:`.HTTPSConnection` uses one of ``assert_fingerprint``,
    ``assert_hostname`` and ``host`` in this order to verify connections.
    If ``assert_hostname`` is False, no verification is done.

    The ``key_file``, ``cert_file``, ``cert_reqs``, ``ca_certs``,
    ``ca_cert_dir``, ``ssl_version``, ``key_password`` are only used if :mod:`ssl`
    is available and are fed into :meth:`urllib3.util.ssl_wrap_socket` to upgrade
    the connection socket into an SSL socket.
    
Establishes a tunnel connection through HTTP CONNECT.

        Return a fresh :class:`urllib3.connection.HTTPConnection`.
        

        Called right before a request is made, after the socket is created.
        

    Given a url, return an :class:`.ConnectionPool` instance of its host.

    This is a shortcut for not having to parse out the scheme, host, and port
    of the url before creating an :class:`.ConnectionPool` instance.

    :param url:
        Absolute URL string that must include the scheme. Port is optional.

    :param \\**kw:
        Passes additional parameters to the constructor of the appropriate
        :class:`.ConnectionPool`. Useful for specifying things like
        timeout, maxsize, headers, etc.

    Example::

        >>> conn = connection_from_url('http://google.com/')
        >>> r = conn.request('GET', '/')
    

    Normalize hosts for comparisons and use with sockets.
    
Returns the URL from a given connection pool. This is mainly used for testing and logging.
Drains a queue of connections and closes each one.

---


Module for using pyOpenSSL as a TLS backend. This module was relevant before
the standard library ``ssl`` module supported SNI, but now that we've dropped
support for Python 2.7 all relevant Python versions support SNI so
**this module is no longer recommended**.

This needs the following packages installed:

* `pyOpenSSL`_ (tested with 16.0.0)
* `cryptography`_ (minimum 1.3.4, from pyopenssl)
* `idna`_ (minimum 2.0)

However, pyOpenSSL depends on cryptography, so while we use all three directly here we
end up having relatively few packages required.

You can install them with the following command:

.. code-block:: bash

    $ python -m pip install pyopenssl cryptography idna

To activate certificate checking, call
:func:`~urllib3.contrib.pyopenssl.inject_into_urllib3` from your Python code
before you begin making HTTP requests. This can be done in a ``sitecustomize``
module, or at any other time before your application begins using ``urllib3``,
like this:

.. code-block:: python

    try:
        import urllib3.contrib.pyopenssl
        urllib3.contrib.pyopenssl.inject_into_urllib3()
    except ImportError:
        pass

.. _pyopenssl: https://www.pyopenssl.org
.. _cryptography: https://cryptography.io
.. _idna: https://github.com/kjd/idna


    Verifies that PyOpenSSL's package-level dependencies have been met.
    Throws `ImportError` if they are not met.
    

    Converts a dNSName SubjectAlternativeName field to the form used by the
    standard library on the given Python version.

    Cryptography produces a dNSName as a unicode string that was idna-decoded
    from ASCII bytes. We need to idna-encode that string to get it back, and
    then on Python 3 we also need to convert to unicode via UTF-8 (the stdlib
    uses PyUnicode_FromStringAndSize on it, which decodes via UTF-8).

    If the name cannot be idna-encoded then we return None signalling that
    the name given should be skipped.
    

        Borrowed wholesale from the Python Cryptography Project. It turns out
        that we can't just safely call `idna.encode`: it can explode for
        wildcard names. This avoids that problem.
        

    Given an PyOpenSSL certificate, provides all the subject alternative names.
    
API-compatibility wrapper for Python OpenSSL's Connection-class.

    I am a wrapper class for the PyOpenSSL ``Context`` object. I am responsible
    for translating the interface of the standard library ``SSLContext`` object
    to calls into PyOpenSSL.
    

---


This module contains provisional support for SOCKS proxies from within
urllib3. This module supports SOCKS4, SOCKS4A (an extension of SOCKS4), and
SOCKS5. To enable its functionality, either install PySocks or install this
module with the ``socks`` extra.

The SOCKS implementation supports the full range of urllib3 features. It also
supports the following SOCKS features:

- SOCKS4A (``proxy_url='socks4a://...``)
- SOCKS4 (``proxy_url='socks4://...``)
- SOCKS5 with remote DNS (``proxy_url='socks5h://...``)
- SOCKS5 with local DNS (``proxy_url='socks5://...``)
- Usernames and passwords for the SOCKS proxy

.. note::
   It is recommended to use ``socks5h://`` or ``socks4a://`` schemes in
   your ``proxy_url`` to ensure that DNS resolution is done from the remote
   server instead of client-side when connecting to a domain name.

SOCKS4 supports IPv4 and domain names with the SOCKS4A extension. SOCKS5
supports IPv4, IPv6, and domain names.

When connecting to a SOCKS4 proxy the ``username`` portion of the ``proxy_url``
will be sent as the ``userid`` section of the SOCKS request:

.. code-block:: python

    proxy_url="socks4a://<userid>@proxy-host"

When connecting to a SOCKS5 proxy the ``username`` and ``password`` portion
of the ``proxy_url`` will be sent as the username/password to authenticate
with the proxy:

.. code-block:: python

    proxy_url="socks5h://<username>:<password>@proxy-host"



    A plain-text HTTP connection that connects via a SOCKS proxy.
    

        Establish a new connection via the SOCKS proxy.
        

    A version of the urllib3 ProxyManager that routes connections via the
    defined SOCKS proxy.
    

---



---

Whether the connection either is brand new or has been previously closed.
        If this property is True then both ``is_connected`` and ``has_connected_to_proxy``
        properties must be False.
        
Whether the connection is actively connected to any origin (proxy or target)
Whether the connection has successfully connected to its proxy.
        This returns False if no proxy is in use. Used to determine whether
        errors are coming from the proxy layer or from tunnelling to the target origin.
        

---


        A generator wrapper for the read() method. A call will block until
        ``amt`` bytes have been read from the connection or until the
        connection is closed.

        :param amt:
            How much of the content to read. The generator will return up to
            much data per iteration, but may return less. This is particularly
            likely when using compressed data. However, the empty string will
            never be returned.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.
        

        Deserializes the body of the HTTP response as a Python object.

        The body of the HTTP response must be encoded using UTF-8, as per
        `RFC 8529 Section 8.1 <https://www.rfc-editor.org/rfc/rfc8259#section-8.1>`_.

        To use a custom JSON decoder pass the result of :attr:`HTTPResponse.data` to
        your custom decoder instead.

        If the body of the HTTP response is not decodable to UTF-8, a
        `UnicodeDecodeError` will be raised. If the body of the HTTP response is not a
        valid JSON document, a `json.JSONDecodeError` will be raised.

        Read more :ref:`here <json_content>`.

        :returns: The body of the HTTP response as a Python object.
        

        Catch Emscripten specific exceptions thrown by fetch.py,
        instead re-raising urllib3 variants, so that low-level exceptions
        are not leaked in the high-level api.

        On exit, release the connection back to the pool.
        

---



---



---


Support for streaming http requests in emscripten.

A few caveats -

Firstly, you can't do streaming http in the main UI thread, because atomics.wait isn't allowed.
Streaming only works if you're running pyodide in a web worker.

Secondly, this uses an extra web worker and SharedArrayBuffer to do the asynchronous fetch
operation, so it requires that you have crossOriginIsolation enabled, by serving over https
(or from localhost) with the two headers below set:

    Cross-Origin-Opener-Policy: same-origin
    Cross-Origin-Embedder-Policy: require-corp

You can tell if cross origin isolation is successfully enabled by looking at the global crossOriginIsolated variable in
javascript console. If it isn't, streaming requests will fallback to XMLHttpRequest, i.e. getting the whole
request into a buffer and then returning it. it shows a warning in the javascript console in this case.

Finally, the webworker which does the streaming fetch is created on initial import, but will only be started once
control is returned to javascript. Call `await wait_for_streaming_ready()` to wait for streaming fetch.

NB: in this code, there are a lot of javascript objects. They are named js_*
to make it clear what type of object they are.


There are some headers that trigger unintended CORS preflight requests.
See also https://github.com/koenvo/pyodide-http/issues/22

 Streaming fetch worker isn't ready. If you want to be sure that streaming fetch
is working, you need to call: 'await urllib3.contrib.emscripten.fetch.wait_for_streaming_ready()`

---


    "An implementation that validates fields according to the definitions in Sections
    5.1 and 5.5 of [HTTP] only needs an additional check that field names do not
    include uppercase characters." (https://httpwg.org/specs/rfc9113.html#n-field-validity)

    `http.client._is_legal_header_name` does not validate the field name according to the
    HTTP 1.1 spec, so we do that here, in addition to checking for uppercase characters.

    This does not allow for the `:` character in the header name, so should not
    be used to validate pseudo-headers.
    

    "A field value MUST NOT contain the zero value (ASCII NUL, 0x00), line feed
    (ASCII LF, 0x0a), or carriage return (ASCII CR, 0x0d) at any position. A field
    value MUST NOT start or end with an ASCII whitespace character (ASCII SP or HTAB,
    0x20 or 0x09)." (https://httpwg.org/specs/rfc9113.html#n-field-validity)
    

    A wrapper class that hides a specific object behind a lock.
    The goal here is to provide a simple way to protect access to an object
    that cannot safely be simultaneously accessed from multiple threads. The
    intended use of this class is simple: take hold of it with a context
    manager, which returns the protected object.
    
putrequest
        This deviates from the HTTPConnection method signature since we never need to override
        sending accept-encoding headers or the host header.
        
Send data to the server.
        `data` can be: `str`, `bytes`, an iterable, or file-like objects
        that support a .read() method.
        
Send an HTTP/2 request

---

This function is for testing purposes only. Gets the current state of the probe cache
This function is for testing purposes only. Reset the cache values

---



---

The match_hostname() function from Python 3.5, essential when using SSL.
Matching according to RFC 6125, section 6.4.3

    http://tools.ietf.org/html/rfc6125#section-6.4.3
    
Exact matching of IP addresses.

    RFC 9110 section 4.3.5: "A reference identity of IP-ID contains the decoded
    bytes of the IP address. An IP version 4 address is 4 octets, and an IP
    version 6 address is 16 octets. [...] A reference identity of type IP-ID
    matches if the address is identical to an iPAddress value of the
    subjectAltName extension of the certificate."
    
Verify that *cert* (in decoded format as returned by
    SSLSocket.getpeercert()) matches the *hostname*.  RFC 2818 and RFC 6125
    rules are followed, but IP addresses are not accepted for *hostname*.

    CertificateError is raised on failure. On success, the function
    returns nothing.
    

---



---


    Returns True if the connection is dropped and should be closed.
    :param conn: :class:`urllib3.connection.HTTPConnection` object.
    
Connect to *address* and return the socket object.

    Convenience function.  Connect to *address* (a 2-tuple ``(host,
    port)``) and return the socket object.  Passing the optional
    *timeout* parameter will set the timeout on the socket instance
    before attempting to connect.  If no *timeout* is supplied, the
    global default timeout setting returned by :func:`socket.getdefaulttimeout`
    is used.  If *source_address* is set it must be a tuple of (host, port)
    for the socket to bind as a source address before making the connection.
    An host of '' or port 0 tells the OS to use the default.
    
This function is designed to work in the context of
    getaddrinfo, where family=socket.AF_UNSPEC is the default and
    will perform a DNS search for both IPv6 and IPv4 records.
Returns True if the system can bind an IPv6 address.

---

Timeout configuration.

    Timeouts can be defined as a default for a pool:

    .. code-block:: python

        import urllib3

        timeout = urllib3.util.Timeout(connect=2.0, read=7.0)

        http = urllib3.PoolManager(timeout=timeout)

        resp = http.request("GET", "https://example.com/")

        print(resp.status)

    Or per-request (which overrides the default for the pool):

    .. code-block:: python

       response = http.request("GET", "https://example.com/", timeout=Timeout(10))

    Timeouts can be disabled by setting all the parameters to ``None``:

    .. code-block:: python

       no_timeout = Timeout(connect=None, read=None)
       response = http.request("GET", "https://example.com/", timeout=no_timeout)


    :param total:
        This combines the connect and read timeouts into one; the read timeout
        will be set to the time leftover from the connect attempt. In the
        event that both a connect timeout and a total are specified, or a read
        timeout and a total are specified, the shorter timeout will be applied.

        Defaults to None.

    :type total: int, float, or None

    :param connect:
        The maximum amount of time (in seconds) to wait for a connection
        attempt to a server to succeed. Omitting the parameter will default the
        connect timeout to the system default, probably `the global default
        timeout in socket.py
        <http://hg.python.org/cpython/file/603b4d593758/Lib/socket.py#l535>`_.
        None will set an infinite timeout for connection attempts.

    :type connect: int, float, or None

    :param read:
        The maximum amount of time (in seconds) to wait between consecutive
        read operations for a response from the server. Omitting the parameter
        will default the read timeout to the system default, probably `the
        global default timeout in socket.py
        <http://hg.python.org/cpython/file/603b4d593758/Lib/socket.py#l535>`_.
        None will set an infinite timeout.

    :type read: int, float, or None

    .. note::

        Many factors can affect the total amount of time for urllib3 to return
        an HTTP response.

        For example, Python's DNS resolver does not obey the timeout specified
        on the socket. Other factors that can affect total request time include
        high CPU load, high swap, the program running at a low priority level,
        or other behaviors.

        In addition, the read and total timeouts only measure the time between
        read operations on the socket connecting the client and the server,
        not the total amount of time for the request to return a complete
        response. For most requests, the timeout is raised because the server
        has not sent the first byte in the specified time. This is not always
        the case; if a server streams one byte every fifteen seconds, a timeout
        of 20 seconds will not trigger, even though the request will take
        several minutes to complete.
    
Check that a timeout attribute is valid.

        :param value: The timeout value to validate
        :param name: The name of the timeout attribute to validate. This is
            used to specify in error messages.
        :return: The validated and casted version of the given value.
        :raises ValueError: If it is a numeric value less than or equal to
            zero, or the type is not an integer, float, or None.
        
Create a new Timeout from a legacy timeout value.

        The timeout value used by httplib.py sets the same timeout on the
        connect(), and recv() socket requests. This creates a :class:`Timeout`
        object that sets the individual timeouts to the ``timeout`` value
        passed to this function.

        :param timeout: The legacy timeout value.
        :type timeout: integer, float, :attr:`urllib3.util.Timeout.DEFAULT_TIMEOUT`, or None
        :return: Timeout object
        :rtype: :class:`Timeout`
        
Create a copy of the timeout object

        Timeout properties are stored per-pool but each request needs a fresh
        Timeout object to ensure each one has its own start/stop configured.

        :return: a copy of the timeout object
        :rtype: :class:`Timeout`
        
Start the timeout clock, used during a connect() attempt

        :raises urllib3.exceptions.TimeoutStateError: if you attempt
            to start a timer that has been started already.
        
Gets the time elapsed since the call to :meth:`start_connect`.

        :return: Elapsed time in seconds.
        :rtype: float
        :raises urllib3.exceptions.TimeoutStateError: if you attempt
            to get duration for a timer that hasn't been started.
        
Get the value to use when setting a connection timeout.

        This will be a positive float or integer, the value None
        (never timeout), or the default system timeout.

        :return: Connect timeout.
        :rtype: int, float, :attr:`Timeout.DEFAULT_TIMEOUT` or None
        
Get the value for the read timeout.

        This assumes some time has elapsed in the connection timeout and
        computes the read timeout appropriately.

        If self.total is set, the read timeout is dependent on the amount of
        time taken by the connect timeout. If the connection time has not been
        established, a :exc:`~urllib3.exceptions.TimeoutStateError` will be
        raised.

        :return: Value to use for the read timeout.
        :rtype: int, float or None
        :raises urllib3.exceptions.TimeoutStateError: If :meth:`start_connect`
            has not yet been called on this object.
        

---


    Checks whether a given file-like object is closed.

    :param obj:
        The file-like object to check.
    

    Asserts whether all headers have been successfully parsed.
    Extracts encountered errors from the result of parsing headers.

    Only works on Python 3.

    :param http.client.HTTPMessage headers: Headers to verify.

    :raises urllib3.exceptions.HeaderParsingError:
        If parsing errors are found.
    

    Checks whether the request of a response has been a HEAD-request.

    :param http.client.HTTPResponse response:
        Response to check if the originating request
        used 'HEAD' as a method.
    

---


    Returns True if the connection requires an HTTP CONNECT through the proxy.

    :param URL proxy_url:
        URL of the proxy.
    :param ProxyConfig proxy_config:
        Proxy configuration from poolmanager.py
    :param str destination_scheme:
        The scheme of the destination. (i.e https, http, etc)
    

---


    Data structure for representing an HTTP URL. Used as a return value for
    :func:`parse_url`. Both the scheme and host are normalized as they are
    both case-insensitive according to RFC 3986.
    
For backwards-compatibility with urlparse. We're nice like that.
Absolute path including the query string.

        Authority component as defined in RFC 3986 3.2.
        This includes userinfo (auth), host and port.

        i.e.
            userinfo@host:port
        

        Network location including host and port.

        If you need the equivalent of urllib.parse's ``netloc``,
        use the ``authority`` property instead.
        

        Convert self into a url

        This function should more or less round-trip with :func:`.parse_url`. The
        returned url may not be exactly the same as the url inputted to
        :func:`.parse_url`, but it should be equivalent by the RFC (e.g., urls
        with a blank port will have : removed).

        Example:

        .. code-block:: python

            import urllib3

            U = urllib3.util.parse_url("https://google.com/mail/")

            print(U.url)
            # "https://google.com/mail/"

            print( urllib3.util.Url("https", "username:password",
                                    "host.com", 80, "/path", "query", "fragment"
                                    ).url
                )
            # "https://username:password@host.com:80/path?query#fragment"
        
Percent-encodes a URI component without reapplying
    onto an already percent-encoded component.
    
Percent-encodes a request target so that there are no invalid characters

    Pre-condition for this function is that 'target' must start with '/'.
    If that is the case then _TARGET_RE will always produce a match.
    

    Given a url, return a parsed :class:`.Url` namedtuple. Best-effort is
    performed to parse incomplete urls. Fields not provided will be None.
    This parser is RFC 3986 and RFC 6874 compliant.

    The parser logic and helper functions are based heavily on
    work done in the ``rfc3986`` module.

    :param str url: URL to parse into a :class:`.Url` namedtuple.

    Partly backwards-compatible with :mod:`urllib.parse`.

    Example:

    .. code-block:: python

        import urllib3

        print( urllib3.util.parse_url('http://google.com/mail/'))
        # Url(scheme='http', host='google.com', port=None, path='/mail/', ...)

        print( urllib3.util.parse_url('google.com:80'))
        # Url(scheme=None, host='google.com', port=80, path=None, ...)

        print( urllib3.util.parse_url('/foo?bar'))
        # Url(scheme=None, host=None, port=None, path='/foo', query='bar', ...)
    

---


    The SSLTransport wraps an existing socket and establishes an SSL connection.

    Contrary to Python's implementation of SSLSocket, it allows you to chain
    multiple TLS connections together. It's particularly useful if you need to
    implement TLS within TLS.

    The class supports most of the socket API operations.
    

        Raises a ProxySchemeUnsupported if the provided ssl_context can't be used
        for TLS in TLS.

        The only requirement is that the ssl_context provides the 'wrap_bio'
        methods.
        

        Create an SSLTransport around socket using the provided ssl_context.
        

        Python's httpclient uses makefile and buffered io when reading HTTP
        messages and we need to support it.

        This is unfortunately a copy and paste of socket.py makefile with small
        changes to point to the socket directly.
        
Performs an I/O loop between incoming/outgoing and the socket.

---

Waits for reading to be available on a given socket.
    Returns True if the socket is readable, or False if the timeout expired.
    
Waits for writing to be available on a given socket.
    Returns True if the socket is readable, or False if the timeout expired.
    

---



---

Retry configuration.

    Each retry attempt will create a new Retry object with updated values, so
    they can be safely reused.

    Retries can be defined as a default for a pool:

    .. code-block:: python

        retries = Retry(connect=5, read=2, redirect=5)
        http = PoolManager(retries=retries)
        response = http.request("GET", "https://example.com/")

    Or per-request (which overrides the default for the pool):

    .. code-block:: python

        response = http.request("GET", "https://example.com/", retries=Retry(10))

    Retries can be disabled by passing ``False``:

    .. code-block:: python

        response = http.request("GET", "https://example.com/", retries=False)

    Errors will be wrapped in :class:`~urllib3.exceptions.MaxRetryError` unless
    retries are disabled, in which case the causing exception will be raised.

    :param int total:
        Total number of retries to allow. Takes precedence over other counts.

        Set to ``None`` to remove this constraint and fall back on other
        counts.

        Set to ``0`` to fail on the first retry.

        Set to ``False`` to disable and imply ``raise_on_redirect=False``.

    :param int connect:
        How many connection-related errors to retry on.

        These are errors raised before the request is sent to the remote server,
        which we assume has not triggered the server to process the request.

        Set to ``0`` to fail on the first retry of this type.

    :param int read:
        How many times to retry on read errors.

        These errors are raised after the request was sent to the server, so the
        request may have side-effects.

        Set to ``0`` to fail on the first retry of this type.

    :param int redirect:
        How many redirects to perform. Limit this to avoid infinite redirect
        loops.

        A redirect is a HTTP response with a status code 301, 302, 303, 307 or
        308.

        Set to ``0`` to fail on the first retry of this type.

        Set to ``False`` to disable and imply ``raise_on_redirect=False``.

    :param int status:
        How many times to retry on bad status codes.

        These are retries made on responses, where status code matches
        ``status_forcelist``.

        Set to ``0`` to fail on the first retry of this type.

    :param int other:
        How many times to retry on other errors.

        Other errors are errors that are not connect, read, redirect or status errors.
        These errors might be raised after the request was sent to the server, so the
        request might have side-effects.

        Set to ``0`` to fail on the first retry of this type.

        If ``total`` is not set, it's a good idea to set this to 0 to account
        for unexpected edge cases and avoid infinite retry loops.

    :param Collection allowed_methods:
        Set of uppercased HTTP method verbs that we should retry on.

        By default, we only retry on methods which are considered to be
        idempotent (multiple requests with the same parameters end with the
        same state). See :attr:`Retry.DEFAULT_ALLOWED_METHODS`.

        Set to a ``None`` value to retry on any verb.

    :param Collection status_forcelist:
        A set of integer HTTP status codes that we should force a retry on.
        A retry is initiated if the request method is in ``allowed_methods``
        and the response status code is in ``status_forcelist``.

        By default, this is disabled with ``None``.

    :param float backoff_factor:
        A backoff factor to apply between attempts after the second try
        (most errors are resolved immediately by a second try without a
        delay). urllib3 will sleep for::

            {backoff factor} * (2 ** ({number of previous retries}))

        seconds. If `backoff_jitter` is non-zero, this sleep is extended by::

            random.uniform(0, {backoff jitter})

        seconds. For example, if the backoff_factor is 0.1, then :func:`Retry.sleep` will
        sleep for [0.0s, 0.2s, 0.4s, 0.8s, ...] between retries. No backoff will ever
        be longer than `backoff_max`.

        By default, backoff is disabled (factor set to 0).

    :param bool raise_on_redirect: Whether, if the number of redirects is
        exhausted, to raise a MaxRetryError, or to return a response with a
        response code in the 3xx range.

    :param bool raise_on_status: Similar meaning to ``raise_on_redirect``:
        whether we should raise an exception, or return a response,
        if status falls in ``status_forcelist`` range and retries have
        been exhausted.

    :param tuple history: The history of the request encountered during
        each call to :meth:`~Retry.increment`. The list is in the order
        the requests occurred. Each list item is of class :class:`RequestHistory`.

    :param bool respect_retry_after_header:
        Whether to respect Retry-After header on status codes defined as
        :attr:`Retry.RETRY_AFTER_STATUS_CODES` or not.

    :param Collection remove_headers_on_redirect:
        Sequence of headers to remove from the request when a response
        indicating a redirect is returned before firing off the redirected
        request.
    
Backwards-compatibility for the old retries format.
Formula for computing the current backoff

        :rtype: float
        
Get the value of Retry-After in seconds.
Sleep between retry attempts.

        This method will respect a server's ``Retry-After`` response header
        and sleep the duration of the time requested. If that is not present, it
        will use an exponential backoff. By default, the backoff factor is 0 and
        this method will return immediately.
        
Errors when we're fairly sure that the server did not receive the
        request, so it should be safe to retry.
        
Errors that occur after the request has been started, so we should
        assume that the server began processing it.
        
Checks if a given HTTP method should be retried upon, depending if
        it is included in the allowed_methods
        
Is this method/status code retryable? (Based on allowlists and control
        variables such as the number of total retries to allow, whether to
        respect the Retry-After header, whether this header is present, and
        whether the returned status code is on the list of status codes to
        be retried upon on the presence of the aforementioned header)
        
Are we out of retries?
Return a new Retry object with incremented retry counters.

        :param response: A response object, or None, if the server did not
            return a response.
        :type response: :class:`~urllib3.response.BaseHTTPResponse`
        :param Exception error: An error encountered during the request, or
            None if the response was received successfully.

        :return: A new ``Retry`` object.
        

---


    Shortcuts for generating request headers.

    :param keep_alive:
        If ``True``, adds 'connection: keep-alive' header.

    :param accept_encoding:
        Can be a boolean, list, or string.
        ``True`` translates to 'gzip,deflate'.  If either the ``brotli`` or
        ``brotlicffi`` package is installed 'gzip,deflate,br' is used instead.
        List will get joined by comma.
        String will be used as provided.

    :param user_agent:
        String representing the user-agent you want, such as
        "python-urllib3/0.6"

    :param basic_auth:
        Colon-separated username:password string for 'authorization: basic ...'
        auth header.

    :param proxy_basic_auth:
        Colon-separated username:password string for 'proxy-authorization: basic ...'
        auth header.

    :param disable_cache:
        If ``True``, adds 'cache-control: no-cache' header.

    Example:

    .. code-block:: python

        import urllib3

        print(urllib3.util.make_headers(keep_alive=True, user_agent="Batman/1.0"))
        # {'connection': 'keep-alive', 'user-agent': 'Batman/1.0'}
        print(urllib3.util.make_headers(accept_encoding=True))
        # {'accept-encoding': 'gzip,deflate'}
    

    If a position is provided, move file to that point.
    Otherwise, we'll attempt to record a position for future use.
    

    Attempt to rewind body to a certain position.
    Primarily used for request redirects and retries.

    :param body:
        File-like object that supports seek.

    :param int pos:
        Position to seek to in file.
    
Takes the HTTP request method, body, and blocksize and
    transforms them into an iterable of chunks to pass to
    socket.sendall() and an optional 'Content-Length' header.

    A 'Content-Length' of 'None' indicates the length of the body
    can't be determined so should use 'Transfer-Encoding: chunked'
    for framing instead.
    

---

Return True for CPython 3.8.9+, 3.9.3+ or 3.10+ and PyPy 7.3.8+ where
    setting SSLContext.hostname_checks_common_name to False works.

    Outside of CPython and PyPy we don't know which implementations work
    or not so we conservatively use our hostname matching as we know that works
    on all implementations.

    https://github.com/urllib3/urllib3/issues/2192#issuecomment-821832963
    https://foss.heptapod.net/pypy/pypy/-/issues/3539
    

    Checks if given fingerprint matches the supplied certificate.

    :param cert:
        Certificate as bytes object.
    :param fingerprint:
        Fingerprint as string of hexdigits, can be interspersed by colons.
    

    Resolves the argument to a numeric constant, which can be passed to
    the wrap_socket function/method from the ssl module.
    Defaults to :data:`ssl.CERT_REQUIRED`.
    If given a string it is assumed to be the name of the constant in the
    :mod:`ssl` module or its abbreviation.
    (So you can specify `REQUIRED` instead of `CERT_REQUIRED`.
    If it's neither `None` nor a string we assume it is already the numeric
    constant which can directly be passed to wrap_socket.
    

    like resolve_cert_reqs
    
Creates and configures an :class:`ssl.SSLContext` instance for use with urllib3.

    :param ssl_version:
        The desired protocol version to use. This will default to
        PROTOCOL_SSLv23 which will negotiate the highest protocol that both
        the server and your installation of OpenSSL support.

        This parameter is deprecated instead use 'ssl_minimum_version'.
    :param ssl_minimum_version:
        The minimum version of TLS to be used. Use the 'ssl.TLSVersion' enum for specifying the value.
    :param ssl_maximum_version:
        The maximum version of TLS to be used. Use the 'ssl.TLSVersion' enum for specifying the value.
        Not recommended to set to anything other than 'ssl.TLSVersion.MAXIMUM_SUPPORTED' which is the
        default value.
    :param cert_reqs:
        Whether to require the certificate verification. This defaults to
        ``ssl.CERT_REQUIRED``.
    :param options:
        Specific OpenSSL options. These default to ``ssl.OP_NO_SSLv2``,
        ``ssl.OP_NO_SSLv3``, ``ssl.OP_NO_COMPRESSION``, and ``ssl.OP_NO_TICKET``.
    :param ciphers:
        Which cipher suites to allow the server to select. Defaults to either system configured
        ciphers if OpenSSL 1.1.1+, otherwise uses a secure default set of ciphers.
    :returns:
        Constructed SSLContext object with specified options
    :rtype: SSLContext
    

    All arguments except for server_hostname, ssl_context, tls_in_tls, ca_cert_data and
    ca_cert_dir have the same meaning as they do when using
    :func:`ssl.create_default_context`, :meth:`ssl.SSLContext.load_cert_chain`,
    :meth:`ssl.SSLContext.set_ciphers` and :meth:`ssl.SSLContext.wrap_socket`.

    :param server_hostname:
        When SNI is supported, the expected hostname of the certificate
    :param ssl_context:
        A pre-made :class:`SSLContext` object. If none is provided, one will
        be created using :func:`create_urllib3_context`.
    :param ciphers:
        A string of ciphers we wish the client to support.
    :param ca_cert_dir:
        A directory containing CA certificates in multiple separate files, as
        supported by OpenSSL's -CApath flag or the capath argument to
        SSLContext.load_verify_locations().
    :param key_password:
        Optional password if the keyfile is encrypted.
    :param ca_cert_data:
        Optional string containing CA certificates in PEM format suitable for
        passing as the cadata parameter to SSLContext.load_verify_locations()
    :param tls_in_tls:
        Use SSLTransport to wrap the existing socket.
    
Detects whether the hostname given is an IPv4 or IPv6 address.
    Also detects IPv6 addresses with Zone IDs.

    :param str hostname: Hostname to examine.
    :return: True if the hostname is an IP address, False otherwise.
    
Detects if a key file is encrypted or not.

---



---

(.*?)

---



---



---

