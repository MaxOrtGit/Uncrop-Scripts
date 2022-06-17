import os

if __name__ == "__main__":
  # Render up to the Saver1 tool, but nothing further downstream.
  comp.Render({"Tool": comp.OriginalSaver, "Wait": True})
  comp.Render({"Tool": comp.ExportSaver, "Wait": True})
  inp = comp.ExportSaver.FindMainInput(1)
  out = inp.GetConnectedOutput()
  pan_tool = out.GetTool()
  
  print("\n\n\n")
  path = comp.OriginalSaver.Clip[1]
  
  s_path = path.split("\\")
  dir_path = "\\".join(s_path[:-1])
  
  dir_list = os.listdir(dir_path) 
  
  max_val = 1
  for file in dir_list:
    val = (file.split(".")[0].split("-")[0])
    if val.isdigit():
      num = int(val)
      if num >= max_val:
        max_val = num + 1
        
  for file in dir_list:
    name_ext = file.split(".")
    name_ext[0] = ''.join([i for i in name_ext[0] if not i.isdigit()])
    
    if name_ext[0] == "Original":
      print(pan_tool.Center, type(pan_tool.Center))
      new_name = f"{max_val}-{pan_tool.Center[1][1]}-{pan_tool.Center[1][2]}-{pan_tool.Size[1]}.png"
      print(new_name)
      os.rename(f"{dir_path}\\{file}", f"{dir_path}\\{new_name}")