import readline as _
import inspect
import traceback

def repl():
    frames_info = inspect.stack()
    outer_frame = frames_info[1].frame
    while True:
        try:
            i = input(">>> ")
        except KeyboardInterrupt:
            print()
            break
        if not i:
            continue
        while i.endswith("\\"):
            i = i[:-1]
            i += input("  > ")
        try:
            try:
                print(eval(i, outer_frame.f_globals, outer_frame.f_locals))
            except SyntaxError:
                print(exec(i, outer_frame.f_globals, outer_frame.f_locals))
        except:
            traceback.print_exc(chain=False)
