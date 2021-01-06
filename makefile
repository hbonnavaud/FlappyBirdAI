open_window_editor:
	designer-qt4 src/ui/ui_editor/main_window.ui

generate_output:
	pyuic5 -x src/ui/ui_editor/main_window.ui -o src/ui/ui_output/main_window.py


