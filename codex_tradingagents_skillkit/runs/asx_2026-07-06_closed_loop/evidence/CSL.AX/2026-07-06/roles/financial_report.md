# Codex Role Evidence Packet: CSL.AX / financial_report

- Trade date: `2026-07-06`
- Instrument identity: `CSL Limited`
- Skill: `tradingagents-financial-report-analyst`

Read only this packet when acting this analyst role. Do not inspect other analyst role packets until the workflow advances to a downstream debate stage.

## Role: financial_report

### Tool: collect_financial_document_sources

- Status: `ok`

```text
## Financial Document Source Packet: CSL.AX

- Trade date: `2026-07-06`
- Collection status: `ok`
- Market: `ASX`
- ASX code: `CSL`
- As-of rule: Only ASX announcements with announcement/lodgement date <= trade_date are included.

| Source | Status | Filing date | Form | URL / reason |
|---|---:|---:|---:|---|
| asx_fallback_document | available | 2025-12-31 | Full Year Results | https://www.csl.com/pdf/56bf77f4-8eff-40ff-bb67-c890e3a3476e/CSL-FY25-Results-and-Major-Strategic-Initiatives.pdf |
| asx_fallback_document | available | 2025-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/ |
| asx_fallback_document | available | 2025-12-31 | Cash Flow Statement | https://investors.csl.com/annualreport/2025/95/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/99/ |

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: revenue, income, NPAT

```text
revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming financial year, these measures will drive further growth through transforming our approach to R&D, our portfolio and re-establishing the organisation with a leaner, more agile design. We must accelerate initiatives across a smaller number of sites and with fewer layers of management. We recognise that we must embark on these changes whilst preserving our underlying performance for you, our shareholders, next financial year and in the years to come. One of the key initiatives is the proposal to demerge CSL Seqirus to shareholders, as a substantial ASX-listed entity. There is a clear benefit for both entities in doing this, providing autonomy and allowing each of them to pursue separate growth strategies and focus on their core capabilities. CSL can be proud of the value it has created for shareholders with a decade long commitment to Seqirus but the time is right to free them to chart a successful, independent future. This also will assist us streamlining how our core CSL organisation looks and works. While these changes are among the most significant for our company in the last 20 years, the Board and management team are unified in our optimism in the outlook for both CSL and Seqirus. We remain confident we have the right settings to ensure we deliver sustainable growth for our shareholders and life-changing treatments for our patients. Governance and board renewal Part of my role is to ensure the CSL Board is regularly renewed and this year we were pleased to welcome two more new directors. Dr Brian Daniels is seeking election as a director. He has been a director since December 2024 and has more than 30 years’ experience in clinical development, commercialisation and biotech investing. Dr Daniels led development and medical affairs at Bristol-Myers Squibb and served as director of Danish pharmaceutical company Novo Nordisk until 2021. In June we announced that Cameron Price would join the board as a Non-executive Director effective 1 October. Cameron is a highly respected executive with extensive experience in the risk and legal fields. He has more than 35 years’ experience and from 2014 he was the General Counsel & Chief Risk Officer at the Future Fund, Australia’s sovereign wealth fund, which invests more than $300 billion globally. These new directors bring invaluable skills and expertise to your Board. Dear Shareholders, I am pleased to have this opportunity to share our results and operating review for the 2024/25 financial year on behalf
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: EPS, DPS, dividends

```text
dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming financial year, these measures will drive further growth through transforming our approach to R&D, our portfolio and re-establishing the organisation with a leaner, more agile design. We must accelerate initiatives across a smaller number of sites and with fewer layers of management. We recognise that we must embark on these changes whilst preserving our underlying performance for you, our shareholders, next financial year and in the years to come. One of the key initiatives is the proposal to demerge CSL Seqirus to shareholders, as a substantial ASX-listed entity. There is a clear benefit for both entities in doing this, providing autonomy and allowing each of them to pursue separate growth strategies and focus on their core capabilities. CSL can be proud of the value it has created for shareholders with a decade long commitment to Seqirus but the time is right to free them to chart a successful, independent future. This also will assist us streamlining how our core CSL organisation looks and works. While these changes are among the most significant for our company in the last 20 years, the Board and management team are unified in our optimism in the outlook for both CSL and Seqirus. We remain confident we have the right settings to ensure we deliver sustainable growth for our shareholders and life-changing treatments for our patients. Governance and board renewal Part of my role is to ensure the CSL Board is regularly renewed and this year we were pleased to welcome two more new directors. Dr Brian Daniels is seeking election as a director. He has been a director since December 2024 and has more than 30 years’ experience in clinical development, commercialisation and biotech investing. Dr Daniels led development and medical affairs at Bristol-Myers Squibb and served as director of Danish pharmaceutical company Novo Nordisk until 2021. In June we announced that Cameron Price would join the board as a Non-executive Director effective 1 October. Cameron is a highly respected executive with extensive experience in the risk and legal fields. He has more than 35 years’ experience and from 2014 he was the General Counsel & Chief Risk Officer at the Future Fund, Australia’s sovereign wealth fund, which invests more than $300 billion globally. These new directors bring invaluable skills and expertise to your Board. Dear Shareholders, I am pleased to have this opportunity to share our results and operating review for the 2024/25 financial year on behalf of your Board. I am proud to report that CSL has stayed true to our mission of
```

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: management discussion, MD&A, outlook

```text
Outlook 16 Global Manufacturing Presence 19 Platforms, Therapeutic Areas and Product Portfolio 20 Material Risks 24 Healthier World Healthier Communities 27 Healthier Environment 35 IN THIS REPORT ANNUAL GENERAL MEETING The 2025 Annual General Meeting (AGM) of CSL Limited (ABN 99 051 588 348) will be held on Tuesday, 28 October 2025 at 10 a.m. (Melbourne time) at RACV City Club, Level 17, 501 Bourke St, Melbourne 3000. Governance Governance 40 Directors’ Report Remuneration Report 61 Financial Report Financial Report 90 Shareholder Information Shareholder Information 138 Key Performance Data Summary 141 Glossary 143 Corporate Directory 144 Sections which are read as part of the Operating and Financial Review (see page 52) 2025 19/8 Annual results and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming
```

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: cash, debt, gearing, capital

```text
Cash, equity and debt for future growth 14 Performance WHAT CSL DOES THE VALUE CSL CREATES Provide a safe, rewarding and productive workplace for promising futures Powered by research and development to identify new indications for CSL’s existing products, and innovative new products for patients and public health Collaborative partnerships Partnering to expand CSL’s global impact and reach Driven by safety, quality, reliability, and innovation in CSL’s operations, while embedding environmental and social considerations into work practices and responsibly sourcing materials and inputs Seek to provide sustainable financial growth with a focus on revenue and margins Empowering CSL’s people through rewarding jobs, career development opportunities and professional training, while creating economic opportunities for CSL’s people and their communities. A healthier society, with enhanced scientific knowledge and skills through strong collaborations and positive outcomes, leading partnerships and high standards of integrity in development of CSL’s products. Creating economic opportunities for CSL’s business partners and the communities they operate in. CSL works with partners allowing the Company to create shared value, while extending capabilities throughout the value chain. Producing life-saving and life-protecting products for public health. CSL’s facilities are critical for the development and manufacture of CSL’s products, while providing a safe and productive workplace. Protecting global health and the wellbeing of individuals, families, businesses and communities from life‑threatening and/or complications resulting from influenza. Saving and/or improving the quality of life of hundreds and thousands of people with rare and serious diseases. Healthier people are able to participate and contribute to society, both socially and economically. See Healthier World page 26 for more. Delivering consistent, profitable and responsible growth for CSL’s investors, which fuels innovation and economic prosperity for multiple stakeholders. 15 CSL Limited Annual Report 2024/25 CSL Behring exists to meet the needs of patients with rare and serious diseases, and those suffering from trauma-related bleeding. Plasma-derived therapies (PDTs) form the core of the portfolio. Patients are the core focus. CSL Behring consists of three vertically integrated components that span the journey from donor to patient. In plasma collection the focus is on three areas; enhancing collection efficiency, reducing the unit acquisition cost and providing a world-class experience for donors and communities. CSL Behring’s manufacturing capability is focused on: • fractionating and transforming plasma into a portfolio of innovative PDTs, and • delivering supply of CSL’s recombinant medicines. CSL Behring’s commercial and medical teams around the world are engaged with healthcare providers, payers and key stakeholders, working to meet patient needs and to deliver successful launches of CSL’s life-saving therapies. This helps provide access to more people with rare and serious diseases. One of CSL Behring’s key priorities is sourcing sufficient and sustainable volumes of plasma to meet the growing need for CSL’s medicines. PDTs have a 9–12 month manufacturing cycle, which is more complex than other pharmaceutical products. These products are vital for patients in need, and can transform their lives. CSL Behring commits to reducing the cost per litre of plasma. The aim to increase yield for immunoglobulins (Ig) and albumin through data analytics, smarter plasma allocation and implementing an operational excellence program. In plasma collection, the Rika collection device and individualised nomogram, iNomi™, enables CSL to collect the optimal amount of plasma from donors. These avenues to yield improvement through technology and innovation are critical to CSL’s ability to increase the supply of therapies to patients. There is significant opportunity for continued global immunoglobulin (lg) growth as the market expands. Within this growing market, PRIVIGEN® and HIZENTRA® are expected to gain share. CSL Behring plays a leading role in Ig and will continue to identify expansion opportunities. CSL expects the global haemophilia B market to grow in coming years due to the steady prevalence of the disease and the launch of novel treatments, including gene therapies. As this market grows, CSL Behring will look to expand its portfolio. The hereditary angioedema (HAE) market may also grow due to improved diagnosis rates and new prophylaxis therapies. ANDEMBRY® (garadacimab), CSL’s next generation HAE therapy, is now approved in US, European Union (EU), United Kingdom (UK), Japan, Switzerland, Australia and the United Arab Emirates. It is available in US, Japan, Germany and Greece. CSL Behring has built on its leadership position and continues to innovate across rare and serious diseases. + READ MORE AT INVESTORS.CSL.COM CSL’s Businesses and Outlook US$11,158m CSL Behring revenue 16 Performance The FY2025 financial year was dynamic for the vaccine market and CSL Seqirus generated positive growth. Over the short term, two current trends will likely continue. First, the exciting acceleration of new vaccine technologies. CSL Seqirus is well positioned with its technology platforms (cell-based, adjuvants, and sa‑mRNA). The second trend is reduced rates of immunisation following the pandemic, particularly in the United States. However, the European vaccination market is stabilising. Against this backdrop, CSL Seqirus maintained commercial discipline in a competitive market. The business expects to continue to drive growth through life cycle management, which will allow CSL to deliver ongoing value to public health systems. Seasonal influenza remains one of the most consequential vaccine preventable diseases due to its significant morbidity and mortality, with unmet need across all populations, and with particular risk to the very young, due to
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: segment performance, sector metrics

```text
segment. This growth is driven by demographic trends such as an aging population, the increasing prevalence of CKD risk factors – including diabetes, hypertension, and cardiovascular disease – and the rising demand for innovative treatment options. Looking ahead, CSL continues to launch excellence in nephrology and to expand its position in the renal disease market. Strategic partnerships have remained a cornerstone of CSL Vifor’s growth model throughout fiscal year 2025. Internal and external collaborations continue to play a pivotal role in advancing CSL’s objectives. Joint efforts with CSL Behring have unlocked new opportunities, including the launch of FERINJECT® in Canada and the introduction of new vial sizes for ZEMAIRA® in the United States. Similarly collaboration with CSL Seqirus in Europe has leveraged CSL’s global capabilities while adapting to local market needs delivering meaningful value to patients and contributing to enterprise-wide sustainable growth. + READ MORE AT INVESTORS.CSL.COM CSL’s Businesses and Outlook US$2,234m CSL Vifor revenue 18 Performance 19 CSL Limited Annual Report 2024/25 Global Manufacturing Presence St. Gallen, Switzerland Across the three businesses, CSL operates the following highly advanced manufacturing facilities. Holly Springs NC, US Liverpool, UK Parkville, Australia Tullamarine, Australia Broadmeadows, Australia Bern, Switzerland Kankakee IL, US Marburg, Germany Platforms, Therapeutic Areas and Product Portfolio CSL research and development leverages its expertise in four strategic platforms – plasma protein technology; recombinant protein technology; cell and genetic medicines; and vaccines technology. PLATFORMS Plasma Protein Technology Recombinant Protein Technology Genetic Medicine Vaccines Technology THERAPEUTIC AREAS These platforms underpin CSL’s five therapeutic areas: 20 Performance Immunoglobulins Building on CSL’s long heritage of providing patients with immunoglobulin products, CSL continues to optimise the patient experience by developing more convenient and flexible ways to dose and administer immunoglobulin products. CSL’s focus is on serving patients with serious immunologic and neurologic diseases, including primary and secondary immunodeficiencies (PID/SID) and chronic inflammatory demyelinating polyneuropathy (CIDP). CSL’s commitment to innovation is reflected in its exploration of inhaled immunoglobulin as a potential treatment for patients with bronchiectasis, complementing the established ZEMAIRA®/RESPREEZA® product for Alpha-1 Antitrypsin deficiency. Guided by the needs and experiences of patients, CSL is advancing an integrated, patient-centric approach that offers greater convenience and improved patient outcomes. Transplant and Immunology In Transplant and Immunology, CSL is leveraging its deep scientific expertise in immunomodulatory mechanisms to unlock synergies between alloimmune and autoimmune diseases. The goal is to bring life-changing solutions to patients in both transplant and immunology. In Immunology, CSL continues to build on its 40-year legacy in hereditary angioedema (HAE) by expanding our portfolio of therapies to provide optimal treatments for the full range of HAE patients. This includes the recent regulatory approval of ANDEMBRY®, a first-in-class, home-grown recombinant monoclonal antibody, in major markets including the United States, European Union, United Kingdom, Japan, Switzerland, Australia and the United Arab Emirates. Looking ahead, CSL is focused on advancing its leadership in immunology with innovative treatments for select autoimmune diseases of high unmet need, reinforcing its commitment to improving patient outcomes across chronic, complex immune-mediated conditions. Despite advances in transplantation improving short‑term survival, long-term survival remains suboptimal. Therefore, CSL is committed to developing therapies to address conditions that may lead to transplant failure. In haematopoietic stem cell transplantation, acute graft‑versus‑host disease (GvHD) is a life-threatening type of rejection and a leading cause of post-transplant morbidity and mortality. There remains a significant unmet need for more effective, less toxic GvHD therapies and CSL is investigating ZEMAIRA® (Alpha-1 Antitrypsin, AAT) for the prevention and treatment of acute GvHD. For solid organ transplant recipients, CSL is advancing therapies to address immune responses that may lead to transplant organ failure, ideally with less toxic treatment regimens and addressing ischemia reperfusion injury (IRI) which can damage the allograft when blood flow is re-introduced. Haematology Improving and extending the lives of patients with rare bleeding disorders is the focus of CSL’s haematology therapeutic area. Significant progress has been achieved in recent years in the treatment of haemophilia A and B through the introduction of innovative recombinant coagulation factor medicines and HEMGENIX® (etranacogene dezaparvovec), an AAV5 (adeno‑associated virus) gene therapy for the treatment of haemophilia B. CSL’s efforts in haematology focus on addressing the high unmet needs of patients with sickle cell disease, with a dual focus on acute treatment of vaso-occlusive crises and effective prophylaxis to reduce the frequency of sickle cell related events. Additionally, CSL is advancing innovative therapies targeting benign haematological conditions, particularly in haemostasis and thrombosis where there is a high unmet need. With a suite of therapies, CSL is also focused on patient blood management (PBM), aiming to reduce reliance on allogeneic blood product transfusions with the use of coagulation factor concentrates wherever available. CSL’s R&D studies include fibrinogen and prothrombin factor concentrates for use in surgical settings with high risk of major bleeding, as well as intravenous iron therapies to support pre- and post-operative anaemia management. Cardiovascular and Renal Extending the lives of patients
```

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: outlook, management commentary

```text
Outlook 16 Global Manufacturing Presence 19 Platforms, Therapeutic Areas and Product Portfolio 20 Material Risks 24 Healthier World Healthier Communities 27 Healthier Environment 35 IN THIS REPORT ANNUAL GENERAL MEETING The 2025 Annual General Meeting (AGM) of CSL Limited (ABN 99 051 588 348) will be held on Tuesday, 28 October 2025 at 10 a.m. (Melbourne time) at RACV City Club, Level 17, 501 Bourke St, Melbourne 3000. Governance Governance 40 Directors’ Report Remuneration Report 61 Financial Report Financial Report 90 Shareholder Information Shareholder Information 138 Key Performance Data Summary 141 Glossary 143 Corporate Directory 144 Sections which are read as part of the Operating and Financial Review (see page 52) 2025 19/8 Annual results and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming
```

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: dividends, capital management

```text
dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming financial year, these measures will drive further growth through transforming our approach to R&D, our portfolio and re-establishing the organisation with a leaner, more agile design. We must accelerate initiatives across a smaller number of sites and with fewer layers of management. We recognise that we must embark on these changes whilst preserving our underlying performance for you, our shareholders, next financial year and in the years to come. One of the key initiatives is the proposal to demerge CSL Seqirus to shareholders, as a substantial ASX-listed entity. There is a clear benefit for both entities in doing this, providing autonomy and allowing each of them to pursue separate growth strategies and focus on their core capabilities. CSL can be proud of the
```

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: capex, commitments

```text
commitment to Seqirus but the time is right to free them to chart a successful, independent future. This also will assist us streamlining how our core CSL organisation looks and works. While these changes are among the most significant for our company in the last 20 years, the Board and management team are unified in our optimism in the outlook for both CSL and Seqirus. We remain confident we have the right settings to ensure we deliver sustainable growth for our shareholders and life-changing treatments for our patients. Governance and board renewal Part of my role is to ensure the CSL Board is regularly renewed and this year we were pleased to welcome two more new directors. Dr Brian Daniels is seeking election as a director. He has been a director since December 2024 and has more than 30 years’ experience in clinical development, commercialisation and biotech investing. Dr Daniels led development and medical affairs at Bristol-Myers Squibb and served as director of Danish pharmaceutical company Novo Nordisk until 2021. In June we announced that Cameron Price would join the board as a Non-executive Director effective 1 October. Cameron is a highly respected executive with extensive experience in the risk and legal fields. He has more than 35 years’ experience and from 2014 he was the General Counsel & Chief Risk Officer at the Future Fund, Australia’s sovereign wealth fund, which invests more than $300 billion globally. These new directors bring invaluable skills and expertise to your Board. Dear Shareholders, I am pleased to have this opportunity to share our results and operating review for the 2024/25 financial year on behalf of your Board. I am proud to report that CSL has stayed true to our mission of delivering for patients, communities and shareholders and encourage you to read our Chief Executive Officer’s communication and also that from Dr Megan Clark AC, who chairs our Human Resources and Remuneration Committee. 4 Engagement The Board of Directors has a strong focus on engaging with a broad range of stakeholders both within CSL and externally. To support engagement with these diverse parties the Board always takes time to visit different locations throughout CSL’s global network. In September 2024 the Board visited CSL’s European operations, including manufacturing plants and research and development facilities in Liverpool (UK), Bern (Switzerland) and Marburg (Germany). In June 2025 the Board held its meeting in Amsterdam, Netherlands, where it met with key external stakeholders including health economists, supply chain partners and researchers. We also celebrated the 25th anniversary of our manufacturing facility in Bern. This event underlined how integral CSL’s acquisition of ZLB in 2000 was to our growth and how important the company’s ongoing contribution is to the Swiss economy. I and some of my colleagues spend time each year meeting with our shareholders. These meetings allow us to listen to feedback from our investors, which we value greatly. One topic we know is top of mind for our shareholders is remuneration. Our investors sent a message at the Annual General Meeting in October – and we continue to listen. You can find the details on remuneration on page 61 of this report. We will continue to listen and respond to feedback in relation to our remuneration approach as well as any other issues important to our shareholders. Your Board is confident in the outlook for CSL and for our ability to deliver enduring patient impact in areas of high unmet medical need. Achieving this will allow us to provide sustainable, profitable growth for our shareholders. Once again, on behalf of the Board, I’d like to extend my thanks for your support. “The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done.” Dr Brian McNamee AO Chairman 5 CSL Limited Annual Report 2024/25 CSL Message from the CEO CSL Vifor grew sales, underpinned by our nephrology products and new country launches. Whilst CSL Seqirus was negatively impacted by low influenza immunisation rates, particularly in the United States, this was partially offset by strong demand for avian influenza vaccine for pandemic protection. Throughout this report, you will find detailed information regarding the financial and operating highlights of CSL throughout the financial year. I will also add a few personal reflections of my own. Refocused strategy Having been Chief Executive Officer for two years, I’ve had time to work with my management team to laser focus our priorities and develop our ambition to deliver enduring patient impact in areas of high unmet medical need and to provide durable returns to our shareholders. CSL has a strong track record of sustainable, profitable growth. However, our operating environment has grown increasingly complex with a dynamic geopolitical backdrop and competitive pressures. We need to accelerate our innovation with our current commercial and clinical portfolio to ensure we’re successful through the next decade and our structure is fit for purpose. After many years of significant growth, it is important we stay committed to a winning formula that can deliver for years to come. I believe a simple and focused CSL is best for patients, our people and our shareholders and we have outlined plans to evolve our strategy to re-focus on what makes us unique: Patients: who need durable, effective treatments for, and protection from, serious diseases. Diseases: where we have a fundamental advantage in understanding the disease and science. Medicines: with a high degree of specialist expertise or manufacturing differentiation. My Priorities To achieve this, I’ve laid out three key priorities for the 2026 financial year and I’m pleased to report we are making good progress on them all. The first priority is to drive growth through the
```

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: risks

```text
risk and legal fields. He has more than 35 years’ experience and from 2014 he was the General Counsel & Chief Risk Officer at the Future Fund, Australia’s sovereign wealth fund, which invests more than $300 billion globally. These new directors bring invaluable skills and expertise to your Board. Dear Shareholders, I am pleased to have this opportunity to share our results and operating review for the 2024/25 financial year on behalf of your Board. I am proud to report that CSL has stayed true to our mission of delivering for patients, communities and shareholders and encourage you to read our Chief Executive Officer’s communication and also that from Dr Megan Clark AC, who chairs our Human Resources and Remuneration Committee. 4 Engagement The Board of Directors has a strong focus on engaging with a broad range of stakeholders both within CSL and externally. To support engagement with these diverse parties the Board always takes time to visit different locations throughout CSL’s global network. In September 2024 the Board visited CSL’s European operations, including manufacturing plants and research and development facilities in Liverpool (UK), Bern (Switzerland) and Marburg (Germany). In June 2025 the Board held its meeting in Amsterdam, Netherlands, where it met with key external stakeholders including health economists, supply chain partners and researchers. We also celebrated the 25th anniversary of our manufacturing facility in Bern. This event underlined how integral CSL’s acquisition of ZLB in 2000 was to our growth and how important the company’s ongoing contribution is to the Swiss economy. I and some of my colleagues spend time each year meeting with our shareholders. These meetings allow us to listen to feedback from our investors, which we value greatly. One topic we know is top of mind for our shareholders is remuneration. Our investors sent a message at the Annual General Meeting in October – and we continue to listen. You can find the details on remuneration on page 61 of this report. We will continue to listen and respond to feedback in relation to our remuneration approach as well as any other issues important to our shareholders. Your Board is confident in the outlook for CSL and for our ability to deliver enduring patient impact in areas of high unmet medical need. Achieving this will allow us to provide sustainable, profitable growth for our shareholders. Once again, on behalf of the Board, I’d like to extend my thanks for your support. “The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done.” Dr Brian McNamee AO Chairman 5 CSL Limited Annual Report 2024/25 CSL Message from the CEO CSL Vifor grew sales, underpinned by our nephrology products and new country launches. Whilst CSL Seqirus was negatively impacted by low influenza immunisation rates, particularly in the United States, this was partially offset by strong demand for avian influenza vaccine for pandemic protection. Throughout this report, you will find detailed information regarding the financial and operating highlights of CSL throughout the financial year. I will also add a few personal reflections of my own. Refocused strategy Having been Chief Executive Officer for two years, I’ve had time to work with my management team to laser focus our priorities and develop our ambition to deliver enduring patient impact in areas of high unmet medical need and to provide durable returns to our shareholders. CSL has a strong track record of sustainable, profitable growth. However, our operating environment has grown increasingly complex with a dynamic geopolitical backdrop and competitive pressures. We need to accelerate our innovation with our current commercial and clinical portfolio to ensure we’re successful through the next decade and our structure is fit for purpose. After many years of significant growth, it is important we stay committed to a winning formula that can deliver for years to come. I believe a simple and focused CSL is best for patients, our people and our shareholders and we have outlined plans to evolve our strategy to re-focus on what makes us unique: Patients: who need durable, effective treatments for, and protection from, serious diseases. Diseases: where we have a fundamental advantage in understanding the disease and science. Medicines: with a high degree of specialist expertise or manufacturing differentiation. My Priorities To achieve this, I’ve laid out three key priorities for the 2026 financial year and I’m pleased to report we are making good progress on them all. The first priority is to drive growth through the evolution of our portfolio development and commercialisation process. We will build an optimal portfolio of new therapies in our pipeline through an integrated approach. This will include closer collaboration between our R&D, business development and commercialisation teams. We will focus on areas where we are uniquely positioned to outperform our competitors and decide where we support our internal capabilities and where we seek to complete our portfolio through external partnerships. We can’t do everything on our own, in some areas we’re going to need partners. This will require changes in how we conduct R&D as we simplify our operating model, reduce duplication, improve efficiencies and consolidate our footprint around key global biotech hubs. We also announced plans to combine the commercial and medical functions of the Behring and Vifor businesses. We will continue to develop and deliver initiatives in our existing businesses like Ig and albumin yield enhancements and launch new products like Hemgenix, Andembry and Filspari. We will also continue to defend and grow Ig and iron volumes and CSL Seqirus will continue to expand geographic and customers segments in influenza. During the year there was no
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: segment table, product table, sector metrics

```text
Product Portfolio 20 Material Risks 24 Healthier World Healthier Communities 27 Healthier Environment 35 IN THIS REPORT ANNUAL GENERAL MEETING The 2025 Annual General Meeting (AGM) of CSL Limited (ABN 99 051 588 348) will be held on Tuesday, 28 October 2025 at 10 a.m. (Melbourne time) at RACV City Club, Level 17, 501 Bourke St, Melbourne 3000. Governance Governance 40 Directors’ Report Remuneration Report 61 Financial Report Financial Report 90 Shareholder Information Shareholder Information 138 Key Performance Data Summary 141 Glossary 143 Corporate Directory 144 Sections which are read as part of the Operating and Financial Review (see page 52) 2025 19/8 Annual results and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming financial year, these measures will drive further growth through transforming our
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in selected eligible ASX financial documents.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: R&D

```text
+ READ MORE ABOUT CSL’S R&D PIPELINE AT WWW.CSL.COM/RESEARCH-ANDDEVELOPMENT/PRODUCT-PIPELINE NPATA attributable to equity holders of US$3.2 billion for the year ended 30 June 2025, up 11% on a reported currency basis when compared to the
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: plasma collections

```text
In plasma collection the focus is on three areas; enhancing collection efficiency, reducing the unit acquisition cost and providing a world-class experience for donors and
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: margins

```text
CODE OF RESPONSIBLE BUSINESS PRACTICE SALES, MARKETING, POLICY EARLY STAGE RESEARCH MANUFACTURING PRODUCT DEVELOPMENT & COLLABORATION & DISTRIBUTION & CLINICAL TRIALS POLICY ADVOCACY & PATIENT SUPPORT + READ MORE AT INVESTORS.CSL.COM CSL’s
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: debt, liquidity

```text
CODE OF RESPONSIBLE BUSINESS PRACTICE SALES, MARKETING, POLICY EARLY STAGE RESEARCH MANUFACTURING PRODUCT DEVELOPMENT & COLLABORATION & DISTRIBUTION & CLINICAL TRIALS POLICY ADVOCACY & PATIENT SUPPORT + READ MORE AT INVESTORS.CSL.COM CSL’s
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: guidance, outlook

```text
+ READ MORE AT INVESTORS.CSL.COM CSL’s Businesses and Outlook US$11,158m CSL Behring revenue 16 Performance The FY2025 financial year was dynamic for the vaccine market and CSL Seqirus generated positive
```

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/

```text
CSL 2025 Annual Report Table of Contents 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 CSL 2025 Annual Report Driven by Our Promise Annual Report 2024/25 Our ambition is to deliver enduring patient impact in areas of high unmet medical need. CSL provides lifesaving products to patients in more than 100 countries and employs over 29,000 people. + READ MORE PAGE 18 INNOVATION EXCELLENCE AND INNOVATION CSL is one of the world’s largest collectors of human plasma CSL Plasma operates one of the world’s largest and most sophisticated plasma collection networks, with collection centres in the US and Europe. Plasma collected at CSL Plasma facilities is used by CSL Behring for the purpose of manufacturing and delivering its life-saving therapies to people in more than 100 countries. + READ MORE PAGES 32–33 CSL Message from the Chair 4 Message from the CEO 6 Performance Year in Review 8 CSL’s Strategy 10 CSL’s Sustainability Strategy 12 Value Creation 14 CSL’s Businesses and Outlook 16 Global Manufacturing Presence 19 Platforms, Therapeutic Areas and Product Portfolio 20 Material Risks 24 Healthier World Healthier Communities 27 Healthier Environment 35 IN THIS REPORT ANNUAL GENERAL MEETING The 2025 Annual General Meeting (AGM) of CSL Limited (ABN 99 051 588 348) will be held on Tuesday, 28 October 2025 at 10 a.m. (Melbourne time) at RACV City Club, Level 17, 501 Bourke St, Melbourne 3000. Governance Governance 40 Directors’ Report Remuneration Report 61 Financial Report Financial Report 90 Shareholder Information Shareholder Information 138 Key Performance Data Summary 141 Glossary 143 Corporate Directory 144 Sections which are read as part of the Operating and Financial Review (see page 52) 2025 19/8 Annual results and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: revenue, income, NPAT

```text
income tax expense 3,724 3,375 Adjustments for: Depreciation and amortisation 1,017 938 Inventory provisions 163 177 Share-based payment expense 149 169 Provision for expected credit losses 6 4 Finance costs, net 410 437 Net gain on business disposals 2 (30) — Loss/(gain) on disposal of property, plant and equipment 11 (2) Unrealised foreign exchange losses 25 53 Changes in operating assets and liabilities: Increase in receivables and contract assets (314) (766) Increase in inventories (628) (780) Increase in trade and other payables 319 445 Decrease in provisions and other liabilities (242) (70) Income tax paid (637) (784) Finance costs paid, net (412) (432) Net cash inflow from operating activities 3,561 2,764 Cash flows from Investing Activities Payments for property, plant and equipment (636) (847) Payments for intangible assets (362) (409) Net proceeds from business disposals 2 180 — Payments for financial assets (13) (3) Payments for other assets (19) — Net cash outflow from investing activities (850) (1,259) Cash flows from Financing Activities Proceeds from issue of shares 17 40 Dividends paid to CSL Limited shareholders 10 (1,334) (1,192) Dividends paid to non-controlling interests 22 (100) (74) Proceeds from borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: cash flow statement, operating cash flow

```text
Cash Flows from Operating Activities Profit before income tax expense 3,724 3,375 Adjustments for: Depreciation and amortisation 1,017 938 Inventory provisions 163 177 Share-based payment expense 149 169 Provision for expected credit losses 6 4 Finance costs, net 410 437 Net gain on business disposals 2 (30) — Loss/(gain) on disposal of property, plant and equipment 11 (2) Unrealised foreign exchange losses 25 53 Changes in operating assets and liabilities: Increase in receivables and contract assets (314) (766) Increase in inventories (628) (780) Increase in trade and other payables 319 445 Decrease in provisions and other liabilities (242) (70) Income tax paid (637) (784) Finance costs paid, net (412) (432) Net cash inflow from operating activities 3,561 2,764 Cash flows from Investing Activities Payments for property, plant and equipment (636) (847) Payments for intangible assets (362) (409) Net proceeds from business disposals 2 180 — Payments for financial assets (13) (3) Payments for other assets (19) — Net cash outflow from investing activities (850) (1,259) Cash flows from Financing Activities Proceeds from issue of shares 17 40 Dividends paid to CSL Limited shareholders 10 (1,334) (1,192) Dividends paid to non-controlling interests 22 (100) (74) Proceeds from borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: free cash flow, cash movement

```text
Net cash inflow from operating activities 3,561 2,764 Cash flows from Investing Activities Payments for property, plant and equipment (636) (847) Payments for intangible assets (362) (409) Net proceeds from business disposals 2 180 — Payments for financial assets (13) (3) Payments for other assets (19) — Net cash outflow from investing activities (850) (1,259) Cash flows from Financing Activities Proceeds from issue of shares 17 40 Dividends paid to CSL Limited shareholders 10 (1,334) (1,192) Dividends paid to non-controlling interests 22 (100) (74) Proceeds from borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: cash, debt, gearing, capital

```text
Cash Flows from Operating Activities Profit before income tax expense 3,724 3,375 Adjustments for: Depreciation and amortisation 1,017 938 Inventory provisions 163 177 Share-based payment expense 149 169 Provision for expected credit losses 6 4 Finance costs, net 410 437 Net gain on business disposals 2 (30) — Loss/(gain) on disposal of property, plant and equipment 11 (2) Unrealised foreign exchange losses 25 53 Changes in operating assets and liabilities: Increase in receivables and contract assets (314) (766) Increase in inventories (628) (780) Increase in trade and other payables 319 445 Decrease in provisions and other liabilities (242) (70) Income tax paid (637) (784) Finance costs paid, net (412) (432) Net cash inflow from operating activities 3,561 2,764 Cash flows from Investing Activities Payments for property, plant and equipment (636) (847) Payments for intangible assets (362) (409) Net proceeds from business disposals 2 180 — Payments for financial assets (13) (3) Payments for other assets (19) — Net cash outflow from investing activities (850) (1,259) Cash flows from Financing Activities Proceeds from issue of shares 17 40 Dividends paid to CSL Limited shareholders 10 (1,334) (1,192) Dividends paid to non-controlling interests 22 (100) (74) Proceeds from borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement

```text
Cash Flows from Operating Activities Profit before income tax expense 3,724 3,375 Adjustments for: Depreciation and amortisation 1,017 938 Inventory provisions 163 177 Share-based payment expense 149 169 Provision for expected credit losses 6 4 Finance costs, net 410 437 Net gain on business disposals 2 (30) — Loss/(gain) on disposal of property, plant and equipment 11 (2) Unrealised foreign exchange losses 25 53 Changes in operating assets and liabilities: Increase in receivables and contract assets (314) (766) Increase in inventories (628) (780) Increase in trade and other payables 319 445 Decrease in provisions and other liabilities (242) (70) Income tax paid (637) (784) Finance costs paid, net (412) (432) Net cash inflow from operating activities 3,561 2,764 Cash flows from Investing Activities Payments for property, plant and equipment (636) (847) Payments for intangible assets (362) (409) Net proceeds from business disposals 2 180 — Payments for financial assets (13) (3) Payments for other assets (19) — Net cash outflow from investing activities (850) (1,259) Cash flows from Financing Activities Proceeds from issue of shares 17 40 Dividends paid to CSL Limited shareholders 10 (1,334) (1,192) Dividends paid to non-controlling interests 22 (100) (74) Proceeds from borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/95/

```text
CSL 2025 Annual Report – Page 95 1 94 Table of Contents 96 148 CSL 2025 Annual Report Consolidated Entity 2025 2024 Notes US$m US$m Cash Flows from Operating Activities Profit before income tax expense 3,724 3,375 Adjustments for: Depreciation and amortisation 1,017 938 Inventory provisions 163 177 Share-based payment expense 149 169 Provision for expected credit losses 6 4 Finance costs, net 410 437 Net gain on business disposals 2 (30) — Loss/(gain) on disposal of property, plant and equipment 11 (2) Unrealised foreign exchange losses 25 53 Changes in operating assets and liabilities: Increase in receivables and contract assets (314) (766) Increase in inventories (628) (780) Increase in trade and other payables 319 445 Decrease in provisions and other liabilities (242) (70) Income tax paid (637) (784) Finance costs paid, net (412) (432) Net cash inflow from operating activities 3,561 2,764 Cash flows from Investing Activities Payments for property, plant and equipment (636) (847) Payments for intangible assets (362) (409) Net proceeds from business disposals 2 180 — Payments for financial assets (13) (3) Payments for other assets (19) — Net cash outflow from investing activities (850) (1,259) Cash flows from Financing Activities Proceeds from issue of shares 17 40 Dividends paid to CSL Limited shareholders 10 (1,334) (1,192) Dividends paid to non-controlling interests 22 (100) (74) Proceeds from borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: revenue, income, NPAT

```text
profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: segment performance, sector metrics

```text
Segment information has been adjusted to exclude impairment and amortisation of acquired intellectual property (IP) and non-recurring items resulting from business acquisition and disposals. NPATA represents the statutory net profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: risks

```text
impairment and amortisation of acquired intellectual property (IP) and non-recurring items resulting from business acquisition and disposals. NPATA represents the statutory net profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: one-off items

```text
impairment and amortisation of acquired intellectual property (IP) and non-recurring items resulting from business acquisition and disposals. NPATA represents the statutory net profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: segment table, product table, sector metrics

```text
Segment information has been adjusted to exclude impairment and amortisation of acquired intellectual property (IP) and non-recurring items resulting from business acquisition and disposals. NPATA represents the statutory net profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/99/

```text
CSL 2025 Annual Report – Page 99 1 98 Table of Contents 100 148 CSL 2025 Annual Report Segment information has been adjusted to exclude impairment and amortisation of acquired intellectual property (IP) and non-recurring items resulting from business acquisition and disposals. NPATA represents the statutory net profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

```
