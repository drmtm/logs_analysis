--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6 (Ubuntu 10.6-0ubuntu0.18.10.1)
-- Dumped by pg_dump version 10.6 (Ubuntu 10.6-0ubuntu0.18.10.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: bad_req; Type: VIEW; Schema: public; Owner: zredpile
--

CREATE VIEW public.bad_req AS
 SELECT date(log."time") AS date,
    count(log.status) AS bad_req
   FROM public.log
  WHERE (log.status <> '200 OK'::text)
  GROUP BY (date(log."time"));




--
-- Name: total_req; Type: VIEW; Schema: public; Owner: zredpile
--

CREATE VIEW public.total_req AS
 SELECT date(log."time") AS date,
    count(log.status) AS total_req
   FROM public.log
  GROUP BY (date(log."time"));




--
-- PostgreSQL database dump complete
--

