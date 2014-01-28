function command_exists () {
    type "$1" &> /dev/null ;
}

if command_exists py.test2; then
    PYTHONPATH="." py.test2 --tb=short -r=sx
else
    python2 -m unittest discover
fi
