# Find Community Help

> 技能：`find-community-help` · 版本：`0.4.0` · 协议：MIT  
> English: [README.md](README.md)

**纯 Markdown skill**：只在任务明显卡住时，输出当前回合的脱敏 dry-run 外部求助计划。不联网、不执行网页命令、不跨轮保留 hint、不写持久记忆。

## 何时使用

- 本地排查后没有清晰下一步
- 任务停滞 / 同一修复路径循环
- 版本漂移，或很可能已有官方/社区成熟解法
- 用户针对**当前卡住任务**要求官方/社区帮助

不要用于：健康任务、泛研究、新闻、比价。

## 发布包

- `SKILL.md` + `LICENSE` + `agents/*.yaml` + `references/*.md`
- 不含脚本、测试夹具、运行时服务

历史名称 `agent-travel` 仅作兼容 marker 说明。
