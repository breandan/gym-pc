FROM dorowu/ubuntu-desktop-lxde-vnc

COPY autostart /root/.config/lxsession/LXDE/autostart
COPY LXTerminal.desktop /root/Desktop/LXTerminal.desktop
COPY lubuntu-rc.xml /root/.config/openbox/lubuntu-rc.xml
COPY xinitrc /root/.xinitrc
RUN /bin/bash -c "echo '@LXTerminal' >> /etc/xdg/lxsession/LXDE/autostart"
RUN /bin/bash -c "echo 'exec lxterminal' >> /startup.sh"
RUN /bin/bash -c "echo 'pushd /tmp; python -m SimpleHTTPServer &> /tmp/exit_code_server.log &' >> /root/.bashrc"
ENV PROMPT_COMMAND='echo $? > /tmp/exit_code.txt'

ENTRYPOINT ["/startup.sh"]
