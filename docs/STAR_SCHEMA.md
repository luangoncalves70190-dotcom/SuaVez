# Star Schema do SuaVez

## Grão
Uma linha da tabela fato representa uma entrada de um paciente em uma fila de atendimento.

## Tabela fato
`fato_atendimento_fila`

## Dimensões
- `dim_paciente`
- `dim_hospital`
- `dim_especialidade`
- `dim_convenio`
- `dim_data`
- `dim_hora`
- `dim_status`

```text
                  dim_paciente
                       |
dim_data --------------|
dim_hora --------------|
dim_hospital ---- fato_atendimento_fila ---- dim_status
dim_especialidade -----|
dim_convenio ----------|
```
