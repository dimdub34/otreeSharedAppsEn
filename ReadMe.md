# oTree Applications

This directory contains "standard" oTree applications. The interfaces are in English.  
oTree version used: 5.11.1  
The list of Python packages is available in `python_packages.txt`.

## **Applications**

### **BART : Balloon Analogue Risk Task**

The BART, introduced by Lejuez et al. (2002), is a widely used behavioral measure of risk-taking.
Participants are asked to inflate a virtual balloon, earning rewards with each pump, but facing the risk of the
balloon bursting at an unknown threshold. The task captures individual differences in risk preferences by assessing
the trade-off between potential gains and losses.

🔍 **Key Findings:**

- The BART correlates with real-world risk behaviors such as substance use and gambling.
- It distinguishes between adaptive and maladaptive risk-taking tendencies.
- The task provides a dynamic measure of risk propensity, improving upon traditional self-report questionnaires.

📄 **Reference:**

Lejuez CW, Read JP, Kahler CW, Richards JB, Ramsey SE, Stuart GL, Strong DR, Brown RA.
Evaluation of a behavioral measure of risk taking: the Balloon Analogue Risk Task (BART).
J Exp Psychol Appl. 2002 Jun;8(2):75-84. doi: 10.1037//1076-898x.8.2.75. PMID: 12075692.


--- 

### **BRET: Bomb Risk Elicitation Task**

The BRET, introduced by Crosetto & Filippin (2013), is a widely used tool to measure individual risk preferences in an
incentive-compatible manner.
Participants select a number of boxes to collect, each containing monetary rewards, while facing the risk that one of
the boxes contains a hidden bomb that would wipe out their earnings.

🔍 **Key Findings:**

- The BRET provides a continuous measure of risk preferences.
- It avoids distortions found in traditional lottery-based risk elicitation methods.
- Risk-taking behavior varies across contexts, incentives, and demographics.

📄 **Reference:**  

Crosetto, P., & Filippin, A. (2013). The "Bomb" Risk Elicitation Task. Journal of Risk and Uncertainty, 47(1), 31-65.



---

### **Eckel & Grossman**

This repository provides an oTree implementation of the Eckel & Grossman Risk Elicitation Task, a widely used method 
for measuring risk preferences in experimental economics. Originally based on Binswanger (1980), this approach was 
adapted and refined by Eckel & Grossman (2002, 2008) to offer a simpler, incentive-compatible mechanism for 
eliciting individual risk attitudes.

Participants choose between a set of lotteries with varying risk levels, allowing researchers to classify them along 
the risk-aversion spectrum. The task is commonly used in behavioral and experimental economics due to its clarity and 
ease of implementation.

🔍 Key Features:

- The lottery values used in this implementation are based on Dave et al. (2010), scaled down by a factor of 10 to 
represent Euros for control tasks.
- Provides a simple yet robust measure of risk preferences.
- Can be easily customized to adjust lottery payoffs, probabilities, and framing.

📄 **References:**

- Binswanger, H. P. (1980). Attitudes toward Risk: Experimental Measurement in Rural India.
- Dave, C., Eckel, C. C., Johnson, C. A., et al. (2010). Eliciting risk preferences: When is simple better? 
- Journal of Risk and Uncertainty, 41(3), 219–243. DOI:10.1007/s11166-010-9103-z
- Eckel, C. C., & Grossman, P. J. (2002, 2008). Forecasting Risk Attitudes: An Experimental Study Using Incentives.

---

### **NLE: Number Line Estimation**

This repository provides an oTree implementation of the Number Line Estimation (NLE) Task, a widely used cognitive 
test in numerical cognition research. The task requires participants to estimate the position of a given number on a 
visual number line, assessing their numerical representation and estimation accuracy.

📄 **Reference**:

Siegler, R. S., & Opfer, J. E. (2003). The development of numerical estimation: Evidence for multiple representations of numerical quantity. Psychological Science, 14(3), 237–243.

🔍 **Key Findings**:

- The task reveals individual differences in numerical estimation strategies (linear vs. logarithmic representation).
- Performance on the NLE task is correlated with mathematical achievement and cognitive development.
- Variations of the task can assess intuitive number sense and symbolic number processing.

---

### **Public Goods**

This repository provides an oTree implementation of a repeated Public Goods Game, a core paradigm in experimental
economics to study cooperation in groups.
Participants decide how many tokens to keep in their private account versus contribute to a collective account, with
returns determined by a marginal per capita return (MPCR) and optional threshold rules.

📄 **Reference**:

Ledyard, J. O. (1995). Public Goods: A Survey of Experimental Research.
In J. H. Kagel & A. E. Roth (Eds.), The Handbook of Experimental Economics, Princeton University Press.

🔍 **Key Findings**:

- Contributions are typically above the free-riding prediction in early rounds, then often decline over time.
- Communication opportunities can increase cooperation and sustain higher contribution levels.
- Group-level incentives (e.g., MPCR and thresholds) strongly affect contribution behavior.

---

### **SVO: Social Value Orientation**

This repository provides an oTree implementation of the Social Value Orientation (SVO) Task, a widely used tool in 
behavioral and experimental economics to measure individual social preferences. The task evaluates how participants 
allocate resources between themselves and others, identifying their prosocial, individualistic, or competitive 
orientation.

📄 **Reference**:

Murphy, R. O., Ackermann, K. A., & Handgraaf, M. J. J. (2011). Measuring Social Value Orientation. 
Judgment and Decision Making, 6(8), 771–781.

🔍 **Key Findings**:

- Identifies individual differences in social preferences, distinguishing prosocials, individualists, and competitors.
- Strongly correlated with cooperative behavior in economic and social dilemmas.
- Used to predict trust, reciprocity, and fairness in decision-making contexts.

---

### **Mach IV Test**

This repository provides an oTree implementation of the Mach IV Test, a classic instrument developed to assess
Machiavellianism as a personality trait.
Participants respond to statements about manipulation, morality, and interpersonal trust, producing a global score of
Machiavellian orientation.

📄 **Reference**:

Christie, R., & Geis, F. (1970). Studies in Machiavellianism. Academic Press.

🔍 **Key Findings**:

- Higher Machiavellianism is associated with more strategic and manipulative social behavior.
- The scale is widely used to study distrust, cynical beliefs, and instrumental decision-making.
- In behavioral settings, Mach scores are often linked to lower cooperation and stronger self-interest.

---

### **HEXACO Personality Inventory**

This repository provides an oTree implementation of the HEXACO personality framework, measuring six broad dimensions:
Honesty-Humility, Emotionality, eXtraversion, Agreeableness, Conscientiousness, and Openness to Experience.
The questionnaire is used to profile socio-behavioral tendencies and connect personality to experimental choices.

📄 **Reference**:

Lee, K., & Ashton, M. C. (2004). Psychometric Properties of the HEXACO Personality Inventory.
Multivariate Behavioral Research, 39(2), 329-358.

🔍 **Key Findings**:

- The Honesty-Humility factor improves prediction of unethical and exploitative behavior.
- HEXACO dimensions are informative for cooperation, prosociality, and conflict styles.
- The model provides a robust alternative to Big Five-based personality measurement.

---

### **Short Dark Triad Test (SD3)**

This repository provides an oTree implementation of the Short Dark Triad (SD3), a brief measure of Machiavellianism,
narcissism, and psychopathy.
Participants answer 27 items and obtain separate subscale scores for each dark trait dimension.

📄 **Reference**:

Jones, D. N., & Paulhus, D. L. (2014). Introducing the Short Dark Triad (SD3): A Brief Measure of Dark Personality Traits.
Assessment, 21(1), 28-41.

🔍 **Key Findings**:

- The SD3 captures three distinct but related socially aversive personality traits.
- Machiavellianism, narcissism, and psychopathy predict different forms of competitive and exploitative behavior.
- The short format is practical for experiments while preserving good psychometric quality.

---

## Slider Task

This repository provides an oTree implementation of the Slider Task, originally developed by Gill & Prowse (2012) 
as a measure of real effort in experimental economics. Participants are required to adjust sliders to specified target 
positions within a limited time, allowing researchers to assess effort provision, performance incentives, 
and cognitive/motor skills.

📄 **Reference**:

Gill, D., & Prowse, V. (2012). A Structural Analysis of Disappointment Aversion in a Real Effort Competition. American Economic Review, 102(1), 469-503.

🔍 **Key Findings**:

- Used to measure effort exertion in economic experiments.
- Provides a real-effort task that is incentive-compatible and easy to implement.
- Can be used in tournaments, individual effort settings, and team-based designs.

--- 
