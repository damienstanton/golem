path_root = '/home/mplebanski/Projects/golem/apps/blender/benchmark/test_task'
start_task = 1
end_task = 1
total_tasks = 1
outfilebasename = 'tmp4rzd9hnsblender_benchmark'
scene_file = '/golem/resources/bmw27_cpu.blend'
script_src = '# This template is rendered by\n# apps.blender.resources.scenefileeditor.generate_blender_crop_file(),\n# written to tempfile and passed as arg to blender.\nimport bpy\n\nclass EngineWarning(bpy.types.Operator):\n    bl_idname = "wm.engine_warning"\n    bl_label = "Inform about not supported rendering engine"\n\n    def execute(self, context):\n        self.report({"ERROR"}, "Engine " + bpy.context.scene.render.engine + \\\n                               " not supported by Golem")\n        return {"FINISHED"}\n\nclass ShowInformation(bpy.types.Operator):\n    bl_idname = "wm.scene_information"\n    bl_label = "Inform user about scene settings"\n\n\n    def execute(self, context):\n        self.report({"INFO"}, "Engine: " +\n                              str(bpy.context.scene.render.engine))\n        if bpy.context.scene.render.engine == "CYCLES":\n            self.report({"INFO"}, "Samples: " + str(bpy.context.scene.cycles.samples))\n        self.report({"INFO"}, "Resolution: " +\n                              str(bpy.context.scene.render.resolution_x) +\n                               " x " +\n                               str(bpy.context.scene.render.resolution_y))\n        self.report({"INFO"}, "File format: " +\n                               str(bpy.context.scene.render.file_extension))\n        self.report({"INFO"}, "Filepath: " +\n                              str(bpy.context.scene.render.filepath))\n        self.report({"INFO"}, "Frames: " +\n                              str(bpy.context.scene.frame_start) + "-" +\n                              str(bpy.context.scene.frame_end) + ";" +\n                              str(bpy.context.scene.frame_step))\n\n        return {"FINISHED"}\n\n\nbpy.utils.register_class(EngineWarning)\nengine = bpy.context.scene.render.engine\nif engine not in ("BLENDER_RENDER", "CYCLES"):\n    bpy.ops.wm.engine_warning()\n\nbpy.utils.register_class(ShowInformation)\nbpy.ops.wm.scene_information()\n\nbpy.context.scene.render.tile_x = 0\nbpy.context.scene.render.tile_y = 0\nbpy.context.scene.render.resolution_x = 200\nbpy.context.scene.render.resolution_y = 100\nbpy.context.scene.render.resolution_percentage = 100\nbpy.context.scene.render.use_border = True\nbpy.context.scene.render.use_crop_to_border = True\nbpy.context.scene.render.border_max_x = 1.0\nbpy.context.scene.render.border_min_x = 0.0\nbpy.context.scene.render.border_min_y = 0.0\nbpy.context.scene.render.border_max_y = 1.0\nbpy.context.scene.render.use_compositing = bool(False)\nif engine == "CYCLES":\n    samples = 0\n    if samples != 0:\n        bpy.context.scene.cycles.samples = samples\n\n#and check if additional files aren\'t missing\nbpy.ops.file.report_missing_files()\n'
frames = [1]
output_format = 'png'
RESOURCES_DIR = '/golem/resources'
WORK_DIR = '/golem/work'
OUTPUT_DIR = '/golem/output'
