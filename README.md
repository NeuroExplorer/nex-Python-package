# nex-Python-package
Python package for running NeuroExplorer Python scripts an any Python development environment (VS Code, Spyder, etc.)

## Description

Provides a simple way to run Python scripts that control [NeuroExplorer](https://www.neuroexplorer.com) (open data file, get file data, run analysis, save results, etc.) in any Python IDE.

See [NeuroExplorer Python Scripting Documentation](https://www.neuroexplorer.com/docs/reference/scripting/index.html) for detailed information about Python scripting in NeuroExplorer.

To install the package, open Windows Command Prompt, type `pip install -U nex` and press Enter.

If you are using Anaconda:

- Type `Anaconda Prompt` in the Windows Search Bar, select Anaconda version and then click on it
- Type `pip install -U nex` in Anaconda Prompt window and press Enter

After the package is installed, you can run NeuroExplorer Python scripts in any Python development environment. 

For example, to run PSTH analysis saved in the template `PerieventHistograms.ntp`, run this Python code:

```python
import nex
doc = nex.GetActiveDocument()
# run PSTH analysis saved in the template PerieventHistograms
nex.ApplyTemplate(doc, "PerieventHistograms")
``````

The package also provides classes to read and write .nex and .nex5 data files.

```python
import nex.nexfile
reader = nex.nexfile.Reader()
fileData = reader.ReadNexFile(r"C:\path\to\file.nex5")
```


