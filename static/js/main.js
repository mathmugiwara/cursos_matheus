/* ═══════════════════════════════════════════
   MATHEUSDEV PLATFORM — MAIN JS v2
═══════════════════════════════════════════ */

// ── Theme Toggle ──
function toggleTheme() {
  const html = document.documentElement;
  const current = html.getAttribute('data-theme');
  const next = current === 'light' ? 'dark' : 'light';
  html.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
  updateThemeIcons();
}

function updateThemeIcons() {
  const isLight = document.documentElement.getAttribute('data-theme') === 'light';
  document.querySelectorAll('.theme-icon-light').forEach(el => el.style.display = isLight ? 'none' : 'inline');
  document.querySelectorAll('.theme-icon-dark').forEach(el => el.style.display = isLight ? 'inline' : 'none');
  document.querySelectorAll('.theme-label').forEach(el => el.textContent = isLight ? 'Escuro' : 'Claro');
}

document.addEventListener('DOMContentLoaded', updateThemeIcons);

// ── Mobile Sidebar Toggle ──
function toggleSidebar() {
  document.querySelector('.sidebar')?.classList.toggle('open');
}

// ── Flash auto-dismiss ──
document.querySelectorAll('.flash-msg').forEach(el => {
  setTimeout(() => el.style.opacity = '0', 4000);
  setTimeout(() => el.remove(), 4500);
});

// ── Modal helpers ──
function openModal(id) {
  document.getElementById(id)?.classList.add('open');
}

function closeModal(id) {
  document.getElementById(id)?.classList.remove('open');
}

// Close modal clicking backdrop
document.querySelectorAll('.modal-backdrop').forEach(el => {
  el.addEventListener('click', e => {
    if (e.target === el) el.classList.remove('open');
  });
});

// ── Exercise Tabs ──
function switchTab(lessonId, exIndex) {
  document.querySelectorAll(`.ex-tab[data-lesson="${lessonId}"]`).forEach(t => t.classList.remove('active'));
  document.querySelectorAll(`.ex-content[data-lesson="${lessonId}"]`).forEach(c => c.classList.remove('active'));

  document.querySelector(`.ex-tab[data-lesson="${lessonId}"][data-index="${exIndex}"]`)?.classList.add('active');
  document.querySelector(`.ex-content[data-lesson="${lessonId}"][data-index="${exIndex}"]`)?.classList.add('active');
}

// ── Code Submission ──
async function submitExercise(exerciseId, editorInstance) {
  const btn = document.getElementById(`run-btn-${exerciseId}`);
  const output = document.getElementById(`output-${exerciseId}`);
  const banner = document.getElementById(`banner-${exerciseId}`);

  if (!btn || !editorInstance) return;

  const code = editorInstance.getValue();
  btn.disabled = true;
  btn.innerHTML = '⏳ Executando...';

  try {
    const res = await fetch('/submit-exercise', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ exercise_id: exerciseId, code })
    });

    const data = await res.json();

    // Show output
    output.classList.add('show');
    if (data.error && !data.output) {
      output.style.color = '#f87171';
      output.textContent = `❌ Erro:\n${data.error}`;
    } else {
      output.style.color = '';
      output.textContent = data.output || '(sem saída)';
      if (data.error) {
        output.textContent += `\n\n❌ Erro: ${data.error}`;
      }
    }

    // Show result banner
    banner.className = 'result-banner show';
    if (data.passed) {
      banner.classList.add('passed');
      banner.innerHTML = '✅ Exercício resolvido! Parabéns!';
      // Update tab to show checkmark
      const tab = document.querySelector(`.ex-tab[data-ex="${exerciseId}"]`);
      if (tab) { tab.classList.add('passed'); tab.querySelector('.tab-icon').textContent = '✓'; }
      checkAllExercisesDone();
    } else if (!data.success) {
      banner.classList.add('error');
      banner.innerHTML = `⚠️ Erro de execução. Verifique seu código.`;
    } else {
      banner.classList.add('failed');
      const expected = data.expected ? `\nEsperado: "${data.expected}"` : '';
      banner.innerHTML = `❌ Saída incorreta.${expected ? `<br><small style="opacity:0.7">Esperado: <code>${data.expected}</code></small>` : ''}`;
    }

  } catch (err) {
    banner.className = 'result-banner show error';
    banner.innerHTML = '⚠️ Erro de conexão. Tente novamente.';
  } finally {
    btn.disabled = false;
    btn.innerHTML = '▶ Executar';
  }
}

function toggleHint(exerciseId) {
  const hint = document.getElementById(`hint-${exerciseId}`);
  hint?.classList.toggle('visible');
}

function checkAllExercisesDone() {
  const completeBtn = document.getElementById('btn-complete-lesson');
  if (!completeBtn) return;

  // Case 1: tab-based exercise view
  const tabs = document.querySelectorAll('.ex-tab');
  if (tabs.length) {
    if (Array.from(tabs).every(t => t.classList.contains('passed'))) {
      completeBtn.disabled = false;
    }
    return;
  }

  // Case 2: card-based exercise view (exercises page)
  const banners = document.querySelectorAll('.result-banner');
  if (!banners.length) return;
  if (Array.from(banners).every(b => b.classList.contains('passed'))) {
    completeBtn.disabled = false;
  }
}

// ── Complete Lesson ──
async function completeLesson(lessonId) {
  const btn = document.getElementById('btn-complete-lesson');
  if (!btn) return;

  btn.disabled = true;
  btn.innerHTML = '⏳ Salvando...';

  try {
    const res = await fetch(`/complete-lesson/${lessonId}`, { method: 'POST' });
    const data = await res.json();

    if (data.success) {
      btn.closest('.complete-lesson-bar').innerHTML = `
        <div class="lesson-completed-badge">
          ✅ Aula concluída! Ótimo trabalho!
        </div>
      `;
      // Update sidebar if needed
      setTimeout(() => { window.location.reload(); }, 1500);
    }
  } catch (err) {
    btn.disabled = false;
    btn.innerHTML = '✓ Marcar como Concluída';
  }
}

// ── Progress Bars Animation ──
document.querySelectorAll('.progress-bar-fill').forEach(bar => {
  const target = bar.getAttribute('data-width') || bar.style.width;
  bar.style.width = '0';
  requestAnimationFrame(() => {
    setTimeout(() => { bar.style.width = target; }, 100);
  });
});

// ── Admin: Assign Module Price Auto-fill ──
const moduleSelect = document.getElementById('modal-module-select');
const priceInput = document.getElementById('modal-price-input');

if (moduleSelect && priceInput) {
  moduleSelect.addEventListener('change', () => {
    const opt = moduleSelect.selectedOptions[0];
    if (opt?.dataset.price) priceInput.value = opt.dataset.price;
  });
}

// ── Keyboard shortcuts ──
document.addEventListener('keydown', e => {
  // Ctrl+Enter to submit current exercise
  if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
    const activeContent = document.querySelector('.ex-content.active');
    if (activeContent) {
      const btn = activeContent.querySelector('[id^="run-btn-"]');
      if (btn && !btn.disabled) btn.click();
    }
  }
});

// ── Interactive Checks (Lesson Content) ──
function checkAnswer(btn) {
  const container = btn.closest('.interactive-check');
  const input = container.querySelector('.check-input');
  const feedback = container.querySelector('.check-feedback');
  const answer = input.dataset.answer;
  const userVal = input.value.trim();

  if (!userVal) {
    feedback.className = 'check-feedback wrong';
    feedback.textContent = 'Digite uma resposta primeiro.';
    return;
  }

  if (userVal.toLowerCase() === answer.toLowerCase()) {
    feedback.className = 'check-feedback correct';
    feedback.textContent = '✓ Correto! Muito bem!';
    input.style.borderColor = 'var(--green)';
    btn.disabled = true;
    btn.textContent = '✓ Correto';
    btn.style.background = 'var(--green)';
  } else {
    feedback.className = 'check-feedback wrong';
    feedback.textContent = '✗ Incorreto. Tente novamente!';
    input.style.borderColor = 'var(--red)';
    input.focus();
  }
}

function checkChoice(btn) {
  const container = btn.closest('.interactive-check');
  const feedback = container.querySelector('.check-feedback');
  const options = container.querySelectorAll('.check-option');
  const isCorrect = btn.dataset.correct === 'true';

  options.forEach(o => {
    o.classList.add('disabled');
    if (o.dataset.correct === 'true') {
      o.classList.add('correct');
    } else if (o === btn && !isCorrect) {
      o.classList.add('wrong');
    }
  });

  if (isCorrect) {
    feedback.className = 'check-feedback correct';
    feedback.textContent = '✓ Correto! Muito bem!';
  } else {
    feedback.className = 'check-feedback wrong';
    feedback.textContent = '✗ Incorreto. A resposta correta está destacada em verde.';
  }
}
