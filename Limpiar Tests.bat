for /d %%p in (".\Tests\*.*") do rmdir "%%p" /s /q
del /q .\Tests\*.*
