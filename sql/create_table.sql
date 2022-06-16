-- 既存テーブルの削除
DROP TABLE IF EXISTS btc_orderbook_table;
DROP TABLE IF EXISTS btc_orderbook_table2;

-- テーブル作成
CREATE TABLE btc_orderbook_table (
  id serial,
  orderbook jsonb not null,
  ticker jsonb,
  rate jsonb,
  created_at timestamp,
  PRIMARY KEY (id)
);

CREATE TABLE btc_orderbook_table2 (
  id serial,
  orderbook jsonb not null,
  created_at timestamp,
  PRIMARY KEY (id)
);

-- 権限追加
GRANT ALL ON ALL TABLES IN SCHEMA public TO coincheck;