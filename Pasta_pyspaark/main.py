SELECT
  ws_cast(
    id_produto AS INT,
    preco AS DECIMAL(10,2),
    quantidade AS INT,
    data_venda AS DATE
  )
FROM dataset.silver_git.atacadao;
