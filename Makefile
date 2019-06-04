#
# ultimate-discord-smash-bot/Makefile ---
#

ifeq (${ULTIMATE_DISCORD_SMASH_BOT_DIR},)
  $(error source ht-setup.env)
endif

SHELL:=bash
.SUFFIXES:

#####

_default: _ve_build

#####

_apt_get_install:
# For python3
	sudo apt-get install -y python3 python3-venv python3-setuptools python3-wheel

_brew_install:
# For python3 for OSX
	brew install python3
# Use brew pip3 to install packages
	/usr/local/bin/pip3 install wheel setuptools

#####

sys_python3_exe=$(shell PATH=/usr/bin:/usr/local/bin:${PATH} type -p python3)

# check they are set.
ifeq (${sys_python3_exe},)
  $(error the system python3 was not found.)
endif

sys_virtualenv_cmd:=${sys_python3_exe} -m venv

ve_python3_exe:=${ULTIMATE_DISCORD_SMASH_BOT_VE_DIR}/bin/python3
ve_pip3_cmd:=${ve_python3_exe} -m pip

ultimate-discord-smash-bot_pip_install_cmd:=${ve_pip3_cmd} install --editable ${ULTIMATE_DISCORD_SMASH_BOT_DIR}

#####

_ve_build:
# create
	${sys_virtualenv_cmd} ${ULTIMATE_DISCORD_SMASH_BOT_VE_DIR}
# pip update
	${ve_pip3_cmd} install --upgrade pip setuptools wheel
# extra packages
	${ve_pip3_cmd} install -r requirements.txt
# install ourselves.
#	${ve_pip3_cmd} install -e .

_ve_rm:
	rm -rf ${ULTIMATE_DISCORD_SMASH_BOT_VE_DIR}

_ve_rebuild: _ve_rm _ve_build

#####
