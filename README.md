To add these functions to the bash shell, add this section to your ~/.bashrc

```sh
#=================================================================================================#
# BASH SOURCE
#=================================================================================================#
#Source bash shell from .shell/ 
if [ -f ~/.shell/_env ]; then
   . ~/.shell/_env
fi
```sh
