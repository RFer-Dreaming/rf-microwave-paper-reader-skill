# RF Microwave Paper Reader Skill

一个用于 Codex 的 RF / Microwave / Antenna 文献阅读 Skill，适合整理天线、LPDA、宽带天线、小型化天线、匹配网络、CST/HFSS/ADS 电磁仿真相关论文。

这个 skill 的目标不是只做摘要，而是把论文整理成可以支持工程复现和研究设计的资料，包括结构、参数、公式、仿真/测试设置、性能指标、图表读数、CST/HFSS 复现建议和对自己课题的启发。

## 功能特点

- 按固定结构整理单篇 RF/天线论文。
- 提取天线结构、馈电、匹配、加载、寄生、地结构、终端负载等工程信息。
- 提取材料、尺寸、频段、S11、VSWR、增益、效率、波束宽度、交叉极化等指标。
- 对 LPDA/log-periodic 结构额外关注 `tau`、`sigma`、`alpha`、阵元数、阵元尺寸、馈线阻抗和终端方式。
- 使用 PyMuPDF 将 PDF 关键页以 300 dpi 渲染为 PNG，辅助读取文本层无法抽取的表格和图中曲线。
- 对只能从图中目视读取的数值强制标注“估读”，避免把估读值写成论文精确原文。
- 输出 CST/HFSS 复现步骤和主要不确定项。
- 默认建议将每篇文献整理到 `E:\文献整理codex\<paper_slug>\` 的独立文件夹中。

## 适用场景

可以在 Codex 中这样使用：

```text
使用 rf-antenna-literature-reader 读这篇 LPDA 天线论文，按我的文献阅读要求整理，并给出 CST 复现建议。
```

或者：

```text
帮我阅读这篇 RF / antenna paper，重点提取结构参数、S11、增益、效率曲线和可复现建模步骤。
```

## 文件结构

```text
rf-antenna-literature-reader/
  SKILL.md
  agents/
    openai.yaml
  scripts/
    render_pdf_pages.py
```

## 安装方式

### 方式 1：Git clone 安装

在 PowerShell 中运行：

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\skills" | Out-Null
git clone https://github.com/RFer-Dreaming/rf-microwave-paper-reader-skill.git "$env:USERPROFILE\.codex\skills\rf-antenna-literature-reader"
```

如果已经存在旧版本，可以先手动备份或删除旧文件夹，再重新 clone。

注意：不要在不确认内容的情况下批量删除自己的文件夹。若你已经有同名 skill，请先备份：

```powershell
Rename-Item "$env:USERPROFILE\.codex\skills\rf-antenna-literature-reader" "rf-antenna-literature-reader-backup"
```

然后再执行 clone。

### 方式 2：下载 ZIP 压缩包安装

1. 打开 GitHub 仓库页面。
2. 点击 `Code` -> `Download ZIP`。
3. 解压 ZIP。
4. 将解压后的仓库内容复制到：

```text
C:\Users\<你的用户名>\.codex\skills\rf-antenna-literature-reader
```

最终路径应该长这样：

```text
C:\Users\<你的用户名>\.codex\skills\rf-antenna-literature-reader\SKILL.md
C:\Users\<你的用户名>\.codex\skills\rf-antenna-literature-reader\scripts\render_pdf_pages.py
C:\Users\<你的用户名>\.codex\skills\rf-antenna-literature-reader\agents\openai.yaml
```

不要让文件多套一层目录。下面这种结构是不对的：

```text
C:\Users\<你的用户名>\.codex\skills\rf-antenna-literature-reader\rf-microwave-paper-reader-skill-main\SKILL.md
```

如果出现这种情况，把 `rf-microwave-paper-reader-skill-main` 里面的文件移动到 `rf-antenna-literature-reader` 目录下即可。

## Python 依赖

渲染 PDF 页面需要 PyMuPDF：

```powershell
python -m pip install PyMuPDF
```

如果 Codex 使用的是自己的 Python 运行时，可能需要用 Codex 运行时的 Python 安装：

```powershell
& "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m pip install PyMuPDF
```

## 页面渲染脚本用法

脚本位于：

```text
scripts/render_pdf_pages.py
```

示例：

```powershell
python scripts/render_pdf_pages.py "E:\paper.pdf" --out "E:\文献整理codex\paper-name\extracted_pages" --pages 1 3 5 6 7 --dpi 300
```

参数说明：

- `pdf`：PDF 路径。
- `--out`：PNG 输出目录。
- `--pages`：要渲染的页码，1-based。不写则渲染全文。
- `--dpi`：渲染 DPI，默认 300。

## 默认整理输出位置

Skill 中建议默认归档到：

```text
E:\文献整理codex
```

每篇文献建立一个独立小文件夹：

```text
E:\文献整理codex\<paper_slug>\
  summary.md
  extracted_pages\
  tables\
  notes\
  tasks\
```

如果 Codex 当前沙箱不能写入 E 盘，它会请求权限；如果仍不能写入，则应退回当前 workspace 的 `outputs/` 目录，并明确说明。

## 可能遇到的问题

### 1. Skill 没有触发

可能原因：

- 文件没有放到正确目录。
- `SKILL.md` 外面多套了一层文件夹。
- Codex 还没有重新加载 skill。

检查路径是否为：

```text
C:\Users\<你的用户名>\.codex\skills\rf-antenna-literature-reader\SKILL.md
```

然后重启 Codex 或开启新线程再试。

### 2. PyMuPDF / fitz 找不到

报错可能类似：

```text
ModuleNotFoundError: No module named 'fitz'
```

解决：

```powershell
python -m pip install PyMuPDF
```

如果 Codex 使用内置 Python，使用：

```powershell
& "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m pip install PyMuPDF
```

### 3. PDF 文本抽取乱码或表格缺失

这是正常情况，尤其 IEEE / Elsevier / LaTeX PDF 中，表格、公式、希腊字母、负号可能无法被普通文本抽取正确读取。

本 skill 的处理方式是：

- 用 PyMuPDF 渲染 300 dpi 页面截图。
- 对参数表、S11 曲线、增益/效率曲线、结构图进行截图阅读。
- 从图中目视读取的数值标注“估读”。

### 4. 图中曲线数值和正文数值不一致

优先使用正文或表格明确给出的数值。  
曲线目视读取的值只能作为“估读”。  
如果摘要、正文、表格之间存在不一致，应在 critical evaluation 中单独指出。

### 5. 无法写入 `E:\文献整理codex`

可能原因：

- E 盘不存在。
- 文件夹不存在。
- Codex 沙箱没有写权限。

手动创建目录：

```powershell
New-Item -ItemType Directory -Force -Path "E:\文献整理codex"
```

如果 Codex 仍无法写入，应允许它请求权限，或者让它先输出到当前 workspace 的 `outputs/`。

### 6. ZIP 安装后目录名不一致

GitHub ZIP 默认解压成类似：

```text
rf-microwave-paper-reader-skill-main
```

Codex 技能目录建议命名为：

```text
rf-antenna-literature-reader
```

请把 ZIP 解压后的内容复制到：

```text
C:\Users\<你的用户名>\.codex\skills\rf-antenna-literature-reader
```

而不是直接保留 `rf-microwave-paper-reader-skill-main` 作为最终技能目录。

## 输出摘要结构

Skill 默认要求单篇论文按以下 12 个部分整理：

1. Basic Information
2. Research Problem
3. Core Method
4. Geometry and Material Parameters
5. Key Equations
6. Simulation and Measurement Setup
7. Performance Metrics
8. Figures and Current Distribution
9. Reproducibility for CST/HFSS
10. Relation to the User's Research
11. Critical Evaluation
12. Final Concise Conclusion

## 适合提取的天线论文信息

- 天线几何图
- 参数表
- 基板材料和金属层
- 馈电方式和端口
- 匹配网络 / tapered line / balun / load
- S11 / VSWR
- 增益 / realized gain
- radiation efficiency / total efficiency
- HPBW / beamwidth
- F/B ratio
- cross-polarization
- surface current distribution
- 参数扫描
- CST/HFSS 仿真设置
- 测量夹具、暗室、VNA、校准方式

## License

No license is currently specified. Add a license file if you want others to reuse or modify this skill under explicit terms.
