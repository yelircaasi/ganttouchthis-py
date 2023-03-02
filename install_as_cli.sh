#!/usr/bin/bash

# requires pyenv
pyenv install 3.11.2
pyenv virtualenv 3.11.2 ganttouchthis
pyenv activate ganttouchthis
pip install ganttouchthis
deactivate

GTT_EXEC="$PYENV_ROOT/versions/ganttouchthis/bin/ganttouchthis"
GTT_GLOBAL="$HOME/.local/bin/ganttouchthis"
touch $GTT_GLOBAL
echo "#!/usr/bin/bash" >> $GTT_GLOBAL
echo "" >> $GTT_GLOBAL
#echo "pyenv activate ganttouchthis" >> $GTT_GLOBAL
echo "ganttouchthis $@" >> $GTT_GLOBAL
#echo "pyenv deactivate" >> $GTT_GLOBAL
echo "" >> $GTT_GLOBAL
